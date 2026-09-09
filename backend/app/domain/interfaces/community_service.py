from abc import ABC, abstractmethod
from uuid import UUID


class ICommunityService(ABC):
    @abstractmethod
    async def create_post(self, request, author_id: UUID):
        raise NotImplementedError

    @abstractmethod
    async def comment(self, post_id: UUID, request, author_id: UUID):
        raise NotImplementedError

    @abstractmethod
    async def react(self, post_id: UUID, reaction_type: str, user_id: UUID):
        raise NotImplementedError