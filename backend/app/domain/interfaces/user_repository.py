from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID
from app.domain.interfaces.repository_base import BaseRepository
from app.domain.models.dtos import UserDTO

class IUserRepository(BaseRepository[UserDTO], ABC):
    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[UserDTO]:
        pass

    @abstractmethod
    async def exists_by_email(self, email: str) -> bool:
        pass