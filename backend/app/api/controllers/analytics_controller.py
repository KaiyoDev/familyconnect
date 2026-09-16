"""Family analytics & report endpoints — aggregate live family data for DSH screens.

Frontend `analyticsApi`:
  GET  /families/{id}/analytics                 → {total_members, total_events, total_documents, total_posts, ...}
  GET  /families/{id}/analytics/demographics    → {age: [{range, male, female}], by_gender, alive, deceased}
  GET  /families/{id}/analytics/events          → {terms: [...], upcoming, past}
  POST /families/{id}/reports                    → snapshot object (not persisted yet)
  GET  /families/{id}/reports/{report_id}        → fresh snapshot (persistence not wired; documented)
  GET  /families/{id}/reports/{report_id}/export → JSON blob download
"""
import json
from datetime import datetime, timezone
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user, get_db, require_family_access
from app.infrastructure.models.community import Post
from app.infrastructure.models.event import Event
from app.infrastructure.models.genealogy import Family, FamilyBranch, FamilyMember, Relationship
from app.infrastructure.models.heritage import HeritageItem

router = APIRouter(tags=["Analytics"])

AGE_BUCKETS = [
    ("<18", 0, 17),
    ("18-35", 18, 35),
    ("36-55", 36, 55),
    ("56-75", 56, 75),
    ("76+", 76, None),
]


def _age_of(member: FamilyMember) -> int | None:
    if not member.date_of_birth:
        return None
    try:
        dob = datetime.strptime(str(member.date_of_birth)[:10], "%Y-%m-%d")
    except (ValueError, TypeError):
        return None
    return (datetime.now(timezone.utc) - dob.replace(tzinfo=timezone.utc)).days // 365


def _event_to_dict(e: Event) -> dict:
    return {"id": str(e.id), "title": e.title, "type": e.type, "status": e.status,
            "start_time": e.start_time.isoformat() if e.start_time else None,
            "end_time": e.end_time.isoformat() if e.end_time else None,
            "location": e.location}


async def _snapshot(db: AsyncSession, family_id: UUID) -> dict:
    from sqlalchemy import or_
    family = await db.get(Family, family_id)
    if family is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Family not found")
    counts = {}
    for key, model in (("members", FamilyMember), ("posts", Post), ("events", Event),
                       ("branches", FamilyBranch), ("documents", HeritageItem)):
        counts[key] = (await db.execute(
            select(func.count()).select_from(model).where(model.family_id == family_id)
        )).scalar() or 0
    # Relationship has no family_id column — count via the family's member ids
    member_ids = (await db.execute(
        select(FamilyMember.id).where(FamilyMember.family_id == family_id)
    )).scalars().all()
    counts["relationships"] = 0
    if member_ids:
        counts["relationships"] = (await db.execute(
            select(func.count()).select_from(Relationship)
            .where(or_(Relationship.from_member_id.in_(member_ids),
                       Relationship.to_member_id.in_(member_ids)))
        )).scalar() or 0
    now = datetime.now(timezone.utc)
    upcoming = (await db.execute(
        select(func.count()).select_from(Event).where(Event.family_id == family_id,
                                                      Event.start_time >= now.replace(tzinfo=None))
    )).scalar() or 0
    return {
        "family_id": str(family_id),
        "family_name": family.family_name,
        "total_members": counts["members"],
        "total_events": counts["events"],
        "total_documents": counts["documents"],
        "total_posts": counts["posts"],
        "total_branches": counts["branches"],
        "total_relationships": counts["relationships"],
        "upcoming_events": upcoming,
    }


@router.get("/families/{family_id}/analytics")
async def family_analytics(family_id: UUID = Depends(require_family_access), db: AsyncSession = Depends(get_db)):
    """DSH-01 getStats — top-line counters for the family dashboard."""
    snap = await _snapshot(db, family_id)
    members = (await db.execute(
        select(FamilyMember).where(FamilyMember.family_id == family_id)
    )).scalars().all()
    alive = sum(1 for m in members if m.is_alive)
    return {
        "total_members": snap["total_members"],
        "total_events": snap["total_events"],
        "total_documents": snap["total_documents"],
        "total_posts": snap["total_posts"],
        "total_branches": snap["total_branches"],
        "total_relationships": snap["total_relationships"],
        "alive_members": alive,
        "deceased_members": snap["total_members"] - alive,
        "upcoming_events": snap["upcoming_events"],
    }


@router.get("/families/{family_id}/analytics/demographics")
async def family_demographics(family_id: UUID = Depends(require_family_access), db: AsyncSession = Depends(get_db)):
    """DSH-01/02 getDemographics — DSH-01 reads `data.age[].range/male/female`."""
    members = (await db.execute(
        select(FamilyMember).where(FamilyMember.family_id == family_id)
    )).scalars().all()
    by_gender: dict[str, int] = {}
    for m in members:
        g = (m.gender or "UNKNOWN").upper()
        by_gender[g] = by_gender.get(g, 0) + 1
    age = []
    for label, lo, hi in AGE_BUCKETS:
        male = female = 0
        for m in members:
            if not m.is_alive:
                continue
            a = _age_of(m)
            if a is None or a < lo or (hi is not None and a > hi):
                continue
            if (m.gender or "").upper() == "MALE":
                male += 1
            elif (m.gender or "").upper() == "FEMALE":
                female += 1
        age.append({"range": label, "male": male, "female": female, "total": male + female})
    return {
        "age": age,
        "by_gender": by_gender,
        "alive": sum(1 for m in members if m.is_alive),
        "deceased": sum(1 for m in members if not m.is_alive),
    }


@router.get("/families/{family_id}/analytics/events")
async def family_analytics_events(family_id: UUID = Depends(require_family_access), db: AsyncSession = Depends(get_db)):
    """DSH-01/03 getEvents — DSH-01 reads `data.terms`."""
    events = (await db.execute(
        select(Event).where(Event.family_id == family_id).order_by(Event.start_time.desc())
    )).scalars().all()
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    upcoming = [_event_to_dict(e) for e in events if e.start_time and e.start_time >= now]
    past = [_event_to_dict(e) for e in events if e.start_time and e.start_time < now]
    return {"terms": upcoming + past, "upcoming": len(upcoming), "past": len(past)}


@router.post("/families/{family_id}/reports", status_code=status.HTTP_201_CREATED)
async def create_report(family_id: UUID = Depends(require_family_access), db: AsyncSession = Depends(get_db)):
    """DSH-03 createReport — snapshot is returned in-memory; report persistence not wired yet."""
    snap = await _snapshot(db, family_id)
    report_id = uuid4()
    return {
        "id": str(report_id),
        "family_id": str(family_id),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "data": snap,
        "message": "Report snapshot generated (persistence not wired yet)",
    }


@router.get("/families/{family_id}/reports/{report_id}")
async def get_report(family_id: UUID, report_id: UUID, db: AsyncSession = Depends(get_db)):
    """Reports are not persisted yet — recompute a fresh snapshot under the requested id."""
    snap = await _snapshot(db, family_id)
    return {"id": str(report_id), "family_id": str(family_id), "data": snap}


@router.get("/families/{family_id}/reports/{report_id}/export")
async def export_report(family_id: UUID, report_id: UUID, db: AsyncSession = Depends(get_db)):
    """DSH-03 exportReport — JSON blob download (CSV pipeline not wired yet)."""
    snap = await _snapshot(db, family_id)
    body = json.dumps({"id": str(report_id), "family_id": str(family_id), "data": snap})
    return Response(
        content=body,
        media_type="application/json",
        headers={"Content-Disposition": f'attachment; filename="family-report-{report_id}.json"'},
    )
