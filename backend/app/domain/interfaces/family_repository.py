from abc import abstractmethod
from typing import Generic, TypeVar
from uuid import UUID

from app.domain.interfaces.repository_base import BaseRepository

TFamily = TypeVar("TFamily")


class IFamilyRepository(BaseRepository[TFamily], Generic[TFamily]):
    @abstractmethod
    async def get_by_creator(self, creator_id: UUID):
        raise NotImplementedError

    @abstractmethod
    async def get_members(self, family_id: UUID):
        raise NotImplementedError