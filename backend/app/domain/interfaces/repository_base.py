from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from uuid import UUID

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    async def get_by_id(self, id: UUID) -> T | None:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    async def create(self, obj: T) -> T:
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: UUID, obj: T) -> T | None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: UUID) -> bool:
        raise NotImplementedError