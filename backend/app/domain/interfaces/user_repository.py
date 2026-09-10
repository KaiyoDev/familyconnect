from abc import abstractmethod
from typing import Generic, TypeVar

from app.domain.interfaces.repository_base import BaseRepository

TUser = TypeVar("TUser")


class IUserRepository(BaseRepository[TUser], Generic[TUser]):
    @abstractmethod
    async def get_by_email(self, email: str):
        raise NotImplementedError

    @abstractmethod
    async def exists_by_email(self, email: str) -> bool:
        raise NotImplementedError