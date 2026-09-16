"""SQLAlchemy repository adapter for directory profiles (FR-DIR-01 .. FR-DIR-04)."""
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.models.directory import EmploymentProfile, EducationProfile
from app.infrastructure.models.genealogy import FamilyMember


class MemberRepository:
    """Repository for family member read/search in directory context."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_family(self, family_id: UUID) -> list[FamilyMember]:
        result = await self.session.execute(
            select(FamilyMember).where(FamilyMember.family_id == family_id)
        )
        return list(result.scalars().all())

    async def get_by_id(self, member_id: UUID) -> FamilyMember | None:
        return await self.session.get(FamilyMember, member_id)


class EmploymentRepository:
    """Repository for employment profile CRUD (FR-DIR-02)."""

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
        await self.session.commit()
        await self.session.refresh(profile)
        return profile

    async def update(self, profile: EmploymentProfile) -> EmploymentProfile:
        await self.session.commit()
        await self.session.refresh(profile)
        return profile

    async def delete(self, profile_id: UUID) -> None:
        profile = await self.get_by_id(profile_id)
        if profile:
            await self.session.delete(profile)
            await self.session.commit()

    async def search_by_company(
        self, company_name: str, member_ids: list[UUID]
    ) -> list[EmploymentProfile]:
        result = await self.session.execute(
            select(EmploymentProfile).where(
                EmploymentProfile.member_id.in_(member_ids),
                EmploymentProfile.company_name.ilike(f"%{company_name}%"),
            )
        )
        return list(result.scalars().all())

    async def search_by_position(
        self, position: str, member_ids: list[UUID]
    ) -> list[EmploymentProfile]:
        result = await self.session.execute(
            select(EmploymentProfile).where(
                EmploymentProfile.member_id.in_(member_ids),
                EmploymentProfile.position.ilike(f"%{position}%"),
            )
        )
        return list(result.scalars().all())


class EducationRepository:
    """Repository for education profile CRUD (FR-DIR-03)."""

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
        await self.session.commit()
        await self.session.refresh(profile)
        return profile

    async def update(self, profile: EducationProfile) -> EducationProfile:
        await self.session.commit()
        await self.session.refresh(profile)
        return profile

    async def delete(self, profile_id: UUID) -> None:
        profile = await self.get_by_id(profile_id)
        if profile:
            await self.session.delete(profile)
            await self.session.commit()

    async def search_by_school(
        self, school_name: str, member_ids: list[UUID]
    ) -> list[EducationProfile]:
        result = await self.session.execute(
            select(EducationProfile).where(
                EducationProfile.member_id.in_(member_ids),
                EducationProfile.school_name.ilike(f"%{school_name}%"),
            )
        )
        return list(result.scalars().all())