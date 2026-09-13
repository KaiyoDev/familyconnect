from uuid import UUID
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.infrastructure.models.event import RSVP


class RSVPRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def upsert_rsvp(self, event_id: UUID, user_id: UUID, status: str) -> RSVP:
        result = await self.db.execute(
            select(RSVP).where(RSVP.event_id == event_id, RSVP.user_id == user_id)
        )
        rsvp = result.scalars().first()
        if rsvp:
            rsvp.status = status
        else:
            rsvp = RSVP(event_id=event_id, user_id=user_id, status=status)
            self.db.add(rsvp)
        await self.db.commit()
        await self.db.refresh(rsvp)
        return rsvp

    async def get_attendees(self, event_id: UUID, status: Optional[str] = None) -> List[RSVP]:
        query = select(RSVP).where(RSVP.event_id == event_id)
        if status:
            query = query.where(RSVP.status == status)
        result = await self.db.execute(query)
        return list(result.scalars().all())