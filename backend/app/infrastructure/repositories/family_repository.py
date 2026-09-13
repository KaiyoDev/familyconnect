"""SQLAlchemy repository adapter for the family aggregate."""
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.interfaces.family_repository import IFamilyRepository
from app.infrastructure.models.genealogy import Family, FamilyBranch, FamilyMember


class FamilyRepository(IFamilyRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, family_id: UUID) -> Family | None:
        return await self.session.get(Family, family_id)

    async def get_all(self, skip: int = 0, limit: int = 100) -> list[Family]:
        result = await self.session.execute(
            select(Family).offset(skip).limit(limit).order_by(Family.created_at.desc())
        )
        return list(result.scalars().all())

    async def create(self, family: Family) -> Family:
        self.session.add(family)
        await self.session.flush()
        return family

    async def update(self, family: Family) -> Family:
        await self.session.flush()
        return family

    async def delete(self, family: Family) -> None:
        await self.session.delete(family)
        await self.session.flush()

    async def get_by_creator(self, creator_id: UUID) -> list[Family]:
        result = await self.session.execute(
            select(Family).where(Family.created_by == creator_id)
        )
        return list(result.scalars().all())

    async def get_members(self, family_id: UUID) -> list[FamilyMember]:
        result = await self.session.execute(
            select(FamilyMember).where(FamilyMember.family_id == family_id)
        )
        return list(result.scalars().all())

    async def get_branches(self, family_id: UUID) -> list[FamilyBranch]:
        result = await self.session.execute(
            select(FamilyBranch).where(FamilyBranch.family_id == family_id)
        )
        return list(result.scalars().all())
