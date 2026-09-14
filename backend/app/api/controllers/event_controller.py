"""Event API endpoints (stub — full implementation TBD)."""
from uuid import UUID
from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, status
from app.api.dependencies import get_current_user

# ── Family-scoped events:  /families/{family_id}/events* ─────────────────
family_router = APIRouter(prefix="/families", tags=["Event Services"])

# ── Single-event endpoints:  /events/{event_id}* ──────────────────────────
event_router = APIRouter(prefix="/events", tags=["Event Services"])


class EventCreateSchema(BaseModel):
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    start_time: str  # ISO format


class RSVPSchema(BaseModel):
    status: str  # going | maybe | not_going


def check_family_access(user: dict, family_id: UUID):
    user_id = user.get("id")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    # TODO: verify user belongs to family


# ── Family-scoped routes ───────────────────────────────────────────────────

@family_router.post("/{family_id}/events", status_code=status.HTTP_201_CREATED)
async def create_event(
    family_id: UUID,
    payload: EventCreateSchema,
    current_user: dict = Depends(get_current_user),
):
    check_family_access(current_user, family_id)
    return {"message": "Event created", "family_id": str(family_id), "title": payload.title}


@family_router.get("/{family_id}/events")
async def get_events(
    family_id: UUID,
    current_user: dict = Depends(get_current_user),
):
    check_family_access(current_user, family_id)
    return []


# ── Single-event routes ────────────────────────────────────────────────────

@event_router.get("/{event_id}")
async def get_event(event_id: UUID, current_user: dict = Depends(get_current_user)):
    return {"event_id": str(event_id)}


@event_router.put("/{event_id}")
async def update_event(
    event_id: UUID,
    payload: EventCreateSchema,
    current_user: dict = Depends(get_current_user),
):
    return {"message": "Event updated", "event_id": str(event_id)}


@event_router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def cancel_event(event_id: UUID, current_user: dict = Depends(get_current_user)):
    return {"message": "Event cancelled", "event_id": str(event_id)}


@event_router.post("/{event_id}/rsvp", status_code=status.HTTP_201_CREATED)
async def rsvp_event(
    event_id: UUID,
    payload: RSVPSchema,
    current_user: dict = Depends(get_current_user),
):
    allowed = {"going", "maybe", "not_going"}
    if payload.status not in allowed:
        raise HTTPException(status_code=400, detail=f"Invalid RSVP status. Allowed: {allowed}")
    return {"message": f"RSVP recorded: {payload.status}", "event_id": str(event_id)}


@event_router.get("/{event_id}/attendees")
async def get_attendees(
    event_id: UUID,
    status: Optional[str] = None,
    current_user: dict = Depends(get_current_user),
):
    return []
