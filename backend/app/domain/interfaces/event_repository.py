from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from backend.app.domain.interfaces.repository_base import BaseRepository
from backend.app.domain.models.dtos import EventDTO

class IEventRepository(BaseRepository[EventDTO], ABC):
    @abstractmethod
    async def get_upcoming(self) -> List[EventDTO]:
        pass

    @abstractmethod
    async def get_by_family(self, family_id: UUID) -> List[EventDTO]:
        pass