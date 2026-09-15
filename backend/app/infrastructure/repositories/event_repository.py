from uuid import UUID
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.infrastructure.models.event import Event


class EventRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, event_data: dict) -> Event:
        event = Event(**event_data)
        self.db.add(event)
        await self.db.commit()
        await self.db.refresh(event)
        return event

    async def get_by_id(self, event_id: UUID) -> Optional[Event]:
        result = await self.db.execute(select(Event).where(Event.id == event_id))
        return result.scalars().first()

    async def get_by_family(self, family_id: UUID) -> List[Event]:
        result = await self.db.execute(select(Event).where(Event.family_id == family_id))
        return list(result.scalars().all())

    async def update(self, event_id: UUID, update_data: dict) -> Optional[Event]:
        event = await self.get_by_id(event_id)
        if not event:
            return None
        for key, value in update_data.items():
            setattr(event, key, value)
        await self.db.commit()
        await self.db.refresh(event)
        return event

    async def delete(self, event_id: UUID) -> bool:
        event = await self.get_by_id(event_id)
        if not event:
            return False
        await self.db.delete(event)
        await self.db.commit()
        return True