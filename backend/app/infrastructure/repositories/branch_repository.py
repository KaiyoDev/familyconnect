"""SQLAlchemy repository adapter for family branches."""
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.interfaces.branch_repository import IBranchRepository
from app.infrastructure.models.genealogy import FamilyBranch


class BranchRepository(IBranchRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, branch_id: UUID) -> FamilyBranch | None:
        return await self.session.get(FamilyBranch, branch_id)

    async def get_by_family(self, family_id: UUID) -> list[FamilyBranch]:
        result = await self.session.execute(
            select(FamilyBranch).where(FamilyBranch.family_id == family_id)
        )
        return list(result.scalars().all())

    async def create(self, branch: FamilyBranch) -> FamilyBranch:
        self.session.add(branch)
        await self.session.flush()
        return branch

    async def update(self, branch: FamilyBranch) -> FamilyBranch:
        await self.session.flush()
        return branch

    async def delete(self, branch: FamilyBranch) -> None:
        await self.session.delete(branch)
        await self.session.flush()
