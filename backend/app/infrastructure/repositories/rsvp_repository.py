from uuid import UUID
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.infrastructure.models.event import EventRSVP


class RSVPRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def upsert_rsvp(
        self,
        event_id: UUID,
        member_id: UUID,
        response: str,
    ) -> EventRSVP:
        """Create or update an RSVP for a family member on an event."""
        result = await self.db.execute(
            select(EventRSVP).where(
                EventRSVP.event_id == event_id,
                EventRSVP.member_id == member_id,
            )
        )
        rsvp = result.scalars().first()
        if rsvp:
            rsvp.response = response
        else:
            rsvp = EventRSVP(
                event_id=event_id,
                member_id=member_id,
                response=response,
                responded_at=__import__("datetime").datetime.utcnow(),
            )
            self.db.add(rsvp)
        await self.db.commit()
        await self.db.refresh(rsvp)
        return rsvp

    async def get_attendees(
        self,
        event_id: UUID,
        response: Optional[str] = None,
    ) -> List[EventRSVP]:
        query = select(EventRSVP).where(EventRSVP.event_id == event_id)
        if response:
            query = query.where(EventRSVP.response == response)
        result = await self.db.execute(query)
        return list(result.scalars().all())
