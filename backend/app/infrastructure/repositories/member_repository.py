"""SQLAlchemy repository adapter for genealogy members."""
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.interfaces.member_repository import IMemberRepository
from app.infrastructure.models.genealogy import FamilyMember


class MemberRepository(IMemberRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, member_id: UUID) -> FamilyMember | None:
        return await self.session.get(FamilyMember, member_id)

    async def get_by_family(self, family_id: UUID) -> list[FamilyMember]:
        result = await self.session.execute(
            select(FamilyMember).where(FamilyMember.family_id == family_id)
        )
        return list(result.scalars().all())

    async def create(self, member: FamilyMember) -> FamilyMember:
        self.session.add(member)
        await self.session.flush()
        return member

    async def update(self, member: FamilyMember) -> FamilyMember:
        await self.session.flush()
        return member

    async def delete(self, member: FamilyMember) -> None:
        await self.session.delete(member)
        await self.session.flush()
