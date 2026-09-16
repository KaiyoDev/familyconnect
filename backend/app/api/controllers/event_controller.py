"""Event API endpoints — wired to EventService (FR: EVT services)."""
from uuid import UUID
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter, Depends, File, HTTPException, Query, Response, UploadFile, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user, get_event_service
from app.infrastructure.databases.database import get_db
from app.infrastructure.models.heritage import MediaAsset
from app.infrastructure.repositories.user_repository import UserRepository
from app.services.event_service import EventService

# ── Family-scoped events:  /families/{family_id}/events* ─────────────────
family_router = APIRouter(prefix="/families", tags=["Event Services"])

# ── Single-event endpoints:  /events/{event_id}* ──────────────────────────
event_router = APIRouter(prefix="/events", tags=["Event Services"])


class EventCreateSchema(BaseModel):
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    start_time: datetime  # ISO format, parsed to datetime
    end_time: Optional[datetime] = None
    type: Optional[str] = None  # defaults to GENERAL


class EventUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    type: Optional[str] = None
    status: Optional[str] = None


class RSVPSchema(BaseModel):
    status: str  # going | maybe | not_going


def check_family_access(user: dict, family_id: UUID):
    user_id = user.get("id") or user.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    # TODO: verify user belongs to family (security hardening tracked separately)


def _user_id(user: dict) -> UUID:
    uid = user.get("id") or user.get("sub")
    if not uid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not resolve user id")
    return UUID(str(uid))


async def _user_email(db: AsyncSession, user: dict) -> str:
    user_obj = await UserRepository(db).get_by_id(_user_id(user))
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user_obj.email


# ── Family-scoped routes ───────────────────────────────────────────────────

@family_router.post("/{family_id}/events", status_code=status.HTTP_201_CREATED)
async def create_event(
    family_id: UUID,
    payload: EventCreateSchema,
    current_user: dict = Depends(get_current_user),
    svc: EventService = Depends(get_event_service),
):
    check_family_access(current_user, family_id)
    data = payload.model_dump(exclude_none=True)
    return await svc.create_event(family_id, _user_id(current_user), data)


@family_router.get("/{family_id}/events")
async def get_events(
    family_id: UUID,
    current_user: dict = Depends(get_current_user),
    svc: EventService = Depends(get_event_service),
):
    check_family_access(current_user, family_id)
    return await svc.get_events(family_id)


# ── Single-event routes ────────────────────────────────────────────────────

@event_router.get("/{event_id}")
async def get_event(event_id: UUID, current_user: dict = Depends(get_current_user),
                    svc: EventService = Depends(get_event_service)):
    return await svc.get_event(event_id)


@event_router.put("/{event_id}")
async def update_event(
    event_id: UUID,
    payload: EventUpdateSchema,
    current_user: dict = Depends(get_current_user),
    svc: EventService = Depends(get_event_service),
):
    return await svc.update_event(event_id, payload.model_dump(exclude_none=True))


@event_router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def cancel_event(event_id: UUID, current_user: dict = Depends(get_current_user),
                       svc: EventService = Depends(get_event_service)):
    await svc.cancel_event(event_id)


@event_router.post("/{event_id}/rsvp", status_code=status.HTTP_201_CREATED)
async def rsvp_event(
    event_id: UUID,
    payload: RSVPSchema,
    current_user: dict = Depends(get_current_user),
    svc: EventService = Depends(get_event_service),
    db: AsyncSession = Depends(get_db),
):
    guest_email = await _user_email(db, current_user)
    return await svc.rsvp(event_id, guest_email, payload.status)


@event_router.get("/{event_id}/attendees")
async def get_attendees(
    event_id: UUID,
    status: Optional[str] = None,
    current_user: dict = Depends(get_current_user),
    svc: EventService = Depends(get_event_service),
):
    return await svc.get_attendees(event_id, status)


# Frontend `eventApi` calls /events/{id}/participants — alias of attendees
@event_router.get("/{event_id}/participants")
async def get_participants(
    event_id: UUID,
    status: Optional[str] = None,
    current_user: dict = Depends(get_current_user),
    svc: EventService = Depends(get_event_service),
):
    return await svc.get_attendees(event_id, status)


# Frontend `eventApi.sendReminder` — EVT-04 (service logs a deferred reminder; no mailer wired yet)
@event_router.post("/{event_id}/remind")
async def remind_event(
    event_id: UUID,
    current_user: dict = Depends(get_current_user),
    svc: EventService = Depends(get_event_service),
):
    return await svc.send_reminder(event_id)


# ── Event gallery (frontend EVT-05: GET/POST /events/{id}/gallery) ───────

def _media_to_dict(a: MediaAsset) -> dict:
    return {"id": str(a.id), "url": a.url, "caption": a.caption, "media_type": a.media_type,
            "uploaded_by": str(a.uploaded_by)}


@event_router.get("/{event_id}/gallery")
async def list_gallery(event_id: UUID, current_user: dict = Depends(get_current_user),
                       db: AsyncSession = Depends(get_db)):
    rows = (await db.execute(select(MediaAsset).where(MediaAsset.event_id == event_id))).scalars().all()
    return [_media_to_dict(a) for a in rows]


@event_router.post("/{event_id}/gallery", status_code=status.HTTP_201_CREATED)
async def upload_gallery(
    event_id: UUID,
    file: UploadFile = File(...),
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Persist the asset record; binary storage (S3/local) not wired yet, url is a placeholder."""
    media_type = (file.content_type or "image/jpeg").split("/")[-1][:20]
    import uuid as _uuid
    asset = MediaAsset(
        id=_uuid.uuid4(),
        event_id=event_id,
        uploaded_by=_user_id(current_user),
        caption=file.filename or None,
        url=f"/media/events/{event_id}/{_uuid.uuid4().hex[:8]}_{file.filename or 'upload'}",
        media_type=media_type,
    )
    db.add(asset)
    await db.commit()
    await db.refresh(asset)
    return _media_to_dict(asset)


# ── Attendee export (frontend eventApi.exportAttendees — blob download) ───
@event_router.get("/{event_id}/export")
async def export_attendees(
    event_id: UUID,
    current_user: dict = Depends(get_current_user),
    svc: EventService = Depends(get_event_service),
):
    """Return participants as a JSON download (CSV storage pipeline not wired yet)."""
    import json as _json
    event = await svc.get_event(event_id)
    participants = await svc.get_attendees(event_id)
    body = _json.dumps({"event": event, "participants": participants}, default=str)
    return Response(
        content=body,
        media_type="application/json",
        headers={"Content-Disposition": f'attachment; filename="event-{event_id}-participants.json"'},
    )
