from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from backend.app.domain.interfaces.repository_base import BaseRepository
from backend.app.domain.models.dtos import PostDTO

class ICommunityRepository(BaseRepository[PostDTO], ABC):
    @abstractmethod
    async def get_posts_by_family(self, family_id: UUID) -> List[PostDTO]:
        pass

    @abstractmethod
    async def get_feed(self, user_id: UUID) -> List[PostDTO]:
        pass