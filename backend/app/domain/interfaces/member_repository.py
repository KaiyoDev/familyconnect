"""Repository contract for genealogy members."""
from abc import ABC, abstractmethod
from typing import Generic, Sequence, TypeVar
from uuid import UUID

TMember = TypeVar("TMember")


class IMemberRepository(ABC, Generic[TMember]):
    @abstractmethod
    async def get_by_id(self, member_id: UUID) -> TMember | None: ...

    @abstractmethod
    async def get_by_family(self, family_id: UUID) -> Sequence[TMember]: ...

    @abstractmethod
    async def create(self, member: TMember) -> TMember: ...

    @abstractmethod
    async def update(self, member: TMember) -> TMember: ...

    @abstractmethod
    async def delete(self, member: TMember) -> None: ...
