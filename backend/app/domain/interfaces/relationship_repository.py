"""Repository contract for genealogy relationships."""
from abc import ABC, abstractmethod
from typing import Generic, Sequence, TypeVar
from uuid import UUID

TRelationship = TypeVar("TRelationship")


class IRelationshipRepository(ABC, Generic[TRelationship]):
    @abstractmethod
    async def get_by_id(self, relationship_id: UUID) -> TRelationship | None: ...

    @abstractmethod
    async def get_by_family_members(self, member_ids: set[str]) -> Sequence[TRelationship]: ...

    @abstractmethod
    async def create(self, relationship: TRelationship) -> TRelationship: ...

    @abstractmethod
    async def update(self, relationship: TRelationship) -> TRelationship: ...

    @abstractmethod
    async def delete(self, relationship: TRelationship) -> None: ...
