from abc import abstractmethod
from datetime import datetime
from typing import Generic, TypeVar
from uuid import UUID

from app.domain.interfaces.repository_base import BaseRepository

TEvent = TypeVar("TEvent")


class IEventRepository(BaseRepository[TEvent], Generic[TEvent]):
    @abstractmethod
    async def get_upcoming(self, family_id: UUID, from_time: datetime | None = None):
        raise NotImplementedError

    @abstractmethod
    async def get_by_family(self, family_id: UUID, skip: int = 0, limit: int = 100):
        raise NotImplementedError