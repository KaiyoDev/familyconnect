"""Repository contract for the Family aggregate."""
from abc import ABC, abstractmethod
from typing import Generic, Sequence, TypeVar
from uuid import UUID

TFamily = TypeVar("TFamily")
TMember = TypeVar("TMember")
TBranch = TypeVar("TBranch")


class IFamilyRepository(ABC, Generic[TFamily, TMember, TBranch]):
    @abstractmethod
    async def get_by_id(self, family_id: UUID) -> TFamily | None: ...

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> Sequence[TFamily]: ...

    @abstractmethod
    async def create(self, family: TFamily) -> TFamily: ...

    @abstractmethod
    async def update(self, family: TFamily) -> TFamily: ...

    @abstractmethod
    async def delete(self, family: TFamily) -> None: ...

    @abstractmethod
    async def get_by_creator(self, creator_id: UUID) -> Sequence[TFamily]: ...

    @abstractmethod
    async def get_members(self, family_id: UUID) -> Sequence[TMember]: ...

    @abstractmethod
    async def get_branches(self, family_id: UUID) -> Sequence[TBranch]: ...
