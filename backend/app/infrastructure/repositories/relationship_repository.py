"""Persistence operations for member relationships."""
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.models.genealogy import Relationship
from app.domain.interfaces.relationship_repository import IRelationshipRepository


class RelationshipRepository(IRelationshipRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, relationship_id: UUID) -> Relationship | None:
        return await self.session.get(Relationship, relationship_id)

    async def get_by_family_members(self, member_ids: set[str]) -> list[Relationship]:
        result = await self.session.execute(
            select(Relationship).where(
                Relationship.from_member_id.in_(member_ids),
                Relationship.to_member_id.in_(member_ids),
            )
        )
        return list(result.scalars().all())

    async def create(self, relationship: Relationship) -> Relationship:
        self.session.add(relationship)
        await self.session.flush()
        return relationship

    async def update(self, relationship: Relationship) -> Relationship:
        await self.session.flush()
        return relationship

    async def delete(self, relationship: Relationship) -> None:
        await self.session.delete(relationship)
        await self.session.flush()
