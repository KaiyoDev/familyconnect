from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from app.domain.models.dtos import CreateEventRequest, EventDTO, RSVPDTO

class IEventService(ABC):
    @abstractmethod
    async def create(self, creator_id: UUID, request: CreateEventRequest) -> EventDTO:
        pass

    @abstractmethod
    async def rsvp(self, event_id: UUID, user_id: UUID, status: str) -> RSVPDTO:
        pass

    @abstractmethod
    async def get_attendees(self, event_id: UUID) -> List[RSVPDTO]:
        pass