"""Repository contract for family branches."""
from abc import ABC, abstractmethod
from typing import Generic, Sequence, TypeVar
from uuid import UUID

TBranch = TypeVar("TBranch")


class IBranchRepository(ABC, Generic[TBranch]):
    @abstractmethod
    async def get_by_id(self, branch_id: UUID) -> TBranch | None: ...

    @abstractmethod
    async def get_by_family(self, family_id: UUID) -> Sequence[TBranch]: ...

    @abstractmethod
    async def create(self, branch: TBranch) -> TBranch: ...

    @abstractmethod
    async def update(self, branch: TBranch) -> TBranch: ...

    @abstractmethod
    async def delete(self, branch: TBranch) -> None: ...
