"""SQLAlchemy repository adapter for directory entities (employment, education)."""
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.interfaces.repository import IRepository
from app.infrastructure.models.directory import EmploymentProfile, EducationProfile


class EmploymentRepository(IRepository[EmploymentProfile]):
    """Repository for employment profile CRUD."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, profile_id: UUID) -> EmploymentProfile | None:
        return await self.session.get(EmploymentProfile, profile_id)

    async def get_by_member(self, member_id: UUID) -> list[EmploymentProfile]:
        result = await self.session.execute(
            select(EmploymentProfile)
            .where(EmploymentProfile.member_id == member_id)
            .order_by(EmploymentProfile.start_date.desc().nullslast())
        )
        return list(result.scalars().all())

    async def create(self, profile: EmploymentProfile) -> EmploymentProfile:
        self.session.add(profile)
        await self.session.flush()
        return profile

    async def update(self, profile: EmploymentProfile) -> EmploymentProfile:
        await self.session.flush()
        return profile

    async def delete(self, profile: EmploymentProfile) -> None:
        await self.session.delete(profile)
        await self.session.flush()

    async def search_by_company(self, company_name: str, family_member_ids: list[UUID]) -> list[EmploymentProfile]:
        """Find employment profiles matching a company name for a set of family members."""
        result = await self.session.execute(
            select(EmploymentProfile).where(
                EmploymentProfile.member_id.in_(family_member_ids),
                EmploymentProfile.company_name.ilike(f"%{company_name}%"),
            )
        )
        return list(result.scalars().all())


class EducationRepository(IRepository[EducationProfile]):
    """Repository for education profile CRUD."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, profile_id: UUID) -> EducationProfile | None:
        return await self.session.get(EducationProfile, profile_id)

    async def get_by_member(self, member_id: UUID) -> list[EducationProfile]:
        result = await self.session.execute(
            select(EducationProfile)
            .where(EducationProfile.member_id == member_id)
            .order_by(EducationProfile.start_year.desc().nullslast())
        )
        return list(result.scalars().all())

    async def create(self, profile: EducationProfile) -> EducationProfile:
        self.session.add(profile)
        await self.session.flush()
        return profile

    async def update(self, profile: EducationProfile) -> EducationProfile:
        await self.session.flush()
        return profile

    async def delete(self, profile: EducationProfile) -> None:
        await self.session.delete(profile)
        await self.session.flush()

    async def search_by_school(self, school_name: str, family_member_ids: list[UUID]) -> list[EducationProfile]:
        """Find education profiles matching a school name for a set of family members."""
        result = await self.session.execute(
            select(EducationProfile).where(
                EducationProfile.member_id.in_(family_member_ids),
                EducationProfile.school_name.ilike(f"%{school_name}%"),
            )
        )
        return list(result.scalars().all())