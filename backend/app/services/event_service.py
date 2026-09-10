import logging
from uuid import UUID
from typing import List, Optional
from fastapi import HTTPException, status
from app.infrastructure.repositories.event_repository import EventRepository
from app.infrastructure.repositories.rsvp_repository import RSVPRepository

logger = logging.getLogger(__name__)


class EventService:
    def __init__(self, event_repo: EventRepository, rsvp_repo: RSVPRepository):
        self.event_repo = event_repo
        self.rsvp_repo = rsvp_repo

    async def create_event(self, family_id: UUID, creator_id: UUID, data: dict) -> dict:
        data["family_id"] = family_id
        data["created_by"] = creator_id
        event = await self.event_repo.create(data)
        return {"message": "Event created successfully", "event_id": str(event.id)}

    async def get_events(self, family_id: UUID) -> List[dict]:
        events = await self.event_repo.get_by_family(family_id)
        return [{"id": str(e.id), "title": e.title, "start_time": e.start_time} for e in events]

    async def get_event(self, event_id: UUID) -> dict:
        event = await self.event_repo.get_by_id(event_id)
        if not event:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
        return {"id": str(event.id), "title": event.title, "description": event.description}

    async def update_event(self, event_id: UUID, data: dict) -> dict:
        event = await self.event_repo.update(event_id, data)
        if not event:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
        return {"message": "Event updated successfully"}

    async def cancel_event(self, event_id: UUID) -> dict:
        success = await self.event_repo.delete(event_id)
        if not success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
        return {"message": "Event cancelled successfully"}

    async def rsvp(self, event_id: UUID, user_id: UUID, rsvp_status: str) -> dict:
        allowed = ["going", "maybe", "not_going"]
        if rsvp_status not in allowed:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid RSVP status")
        await self.rsvp_repo.upsert_rsvp(event_id, user_id, rsvp_status)
        return {"message": f"RSVP updated to {rsvp_status}"}

    async def get_attendees(self, event_id: UUID, rsvp_status: Optional[str] = None) -> List[dict]:
        attendees = await self.rsvp_repo.get_attendees(event_id, rsvp_status)
        return [{"user_id": str(a.user_id), "status": a.status} for a in attendees]

    async def send_reminder(self, event_id: UUID) -> dict:
        logger.info(f"[DEFERRED REMINDER] Notification logged for event_id: {event_id}")
        return {"message": "Reminder logged successfully"}