from abc import abstractmethod
from typing import Generic, TypeVar
from uuid import UUID

from app.domain.interfaces.repository_base import BaseRepository

TCommunity = TypeVar("TCommunity")


class ICommunityRepository(BaseRepository[TCommunity], Generic[TCommunity]):
    @abstractmethod
    async def get_posts_by_family(self, family_id: UUID, skip: int = 0, limit: int = 100):
        raise NotImplementedError

    @abstractmethod
    async def get_feed(self, family_id: UUID, skip: int = 0, limit: int = 100):
        raise NotImplementedError