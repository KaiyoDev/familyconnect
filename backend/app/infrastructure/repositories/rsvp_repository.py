from uuid import UUID
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.infrastructure.models.event import EventRSVP


class RSVPRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def upsert_rsvp(self, event_id: UUID, guest_email: str, status: str) -> EventRSVP:
        """Upsert an RSVP keyed by guest email (EventRSVP XOR: member_id OR guest_email)."""
        result = await self.db.execute(
            select(EventRSVP).where(EventRSVP.event_id == event_id, EventRSVP.guest_email == guest_email)
        )
        rsvp = result.scalars().first()
        if rsvp:
            rsvp.response = status
        else:
            rsvp = EventRSVP(event_id=event_id, guest_email=guest_email, response=status)
            self.db.add(rsvp)
        await self.db.commit()
        await self.db.refresh(rsvp)
        return rsvp

    async def get_attendees(self, event_id: UUID, status: Optional[str] = None) -> List[EventRSVP]:
        query = select(EventRSVP).where(EventRSVP.event_id == event_id)
        if status:
            query = query.where(EventRSVP.response == status)
        result = await self.db.execute(query)
        return list(result.scalars().all())
