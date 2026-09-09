from abc import ABC, abstractmethod
from uuid import UUID


class IEventService(ABC):
    @abstractmethod
    async def create(self, request, creator_id: UUID):
        raise NotImplementedError

    @abstractmethod
    async def rsvp(self, event_id: UUID, request, member_id: UUID):
        raise NotImplementedError

    @abstractmethod
    async def get_attendees(self, event_id: UUID):
        raise NotImplementedError