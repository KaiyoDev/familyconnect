"""Application service for directory profiles and member search (FR-DIR-01 .. FR-DIR-04)."""
from datetime import date
from uuid import UUID, uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.exceptions import NotFoundException, ValidationException
from app.domain.interfaces.branch_repository import IBranchRepository
from app.domain.interfaces.family_repository import IFamilyRepository
from app.domain.interfaces.member_repository import IMemberRepository
from app.domain.interfaces.repository import IRepository
from app.domain.interfaces.unit_of_work import IUnitOfWork
from app.infrastructure.models.directory import EmploymentProfile, EducationProfile
from app.infrastructure.models.genealogy import FamilyMember


class DirectoryService:
    """Coordinates directory / member profile operations."""

    def __init__(
        self,
        session: AsyncSession,
        family_repository: IFamilyRepository | None = None,
        member_repository: IMemberRepository | None = None,
        branch_repository: IBranchRepository | None = None,
        employment_repository: IRepository[EmploymentProfile] | None = None,
        education_repository: IRepository[EducationProfile] | None = None,
        unit_of_work: IUnitOfWork | None = None,
    ):
        self.session = session
        if not all((family_repository, member_repository, unit_of_work)):
            raise ValueError("Repositories and unit_of_work must be injected")
        self.families = family_repository
        self.members = member_repository
        self.branches = branch_repository
        self.employment = employment_repository
        self.education = education_repository
        self.unit_of_work = unit_of_work

    async def _commit(self) -> None:
        await self.unit_of_work.commit()

    async def _rollback(self) -> None:
        await self.unit_of_work.rollback()

    async def _write(self, operation):
        try:
            result = await operation()
            await self._commit()
            return result
        except Exception:
            await self._rollback()
            raise

    async def _ensure_family(self, family_id: UUID):
        family = await self.families.get_by_id(family_id)
        if not family:
            raise NotFoundException("Family not found")
        return family

    async def _get_member(self, member_id: UUID) -> FamilyMember:
        member = await self.members.get_by_id(member_id)
        if not member:
            raise NotFoundException("Member not found")
        return member

    async def get_directory(
        self,
        family_id: UUID,
        branch_id: UUID | None = None,
        generation: int | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> list[FamilyMember]:
        """List all members in a family directory (FR-DIR-01)."""
        await self._ensure_family(family_id)
        members = await self.members.get_by_family(family_id)
        # Filter by branch if provided
        if branch_id:
            members = [m for m in members if m.branch_id == branch_id]
        # NOTE: generation is a computed/derived attribute not stored on FamilyMember yet.
        # When genealogy depth tracking is implemented, filter by generation here.
        # For now, accept the param but skip filtering.
        if generation is not None:
            pass  # Reserved for future use
        return members[skip:skip + limit]

    async def search_members(
        self,
        family_id: UUID,
        query: str | None = None,
        profession: str | None = None,
        location: str | None = None,
        generation: int | None = None,
        branch_id: UUID | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> dict:
        """Search members by name, profession, location, generation (FR-DIR-04).

        Returns a dict with:
          - members: list of matching members with their current employment/education
          - total:   total count of unique matching members
        """
        await self._ensure_family(family_id)
        members = await self.members.get_by_family(family_id)

        # Filter by name query
        if query:
            ql = query.lower()
            members = [m for m in members if ql in m.full_name.lower()]

        # Filter by branch
        if branch_id:
            members = [m for m in members if m.branch_id == branch_id]

        if generation is not None:
            pass  # Reserved for future use — computed from genealogy depth

        # Profession filter: look up members whose employment profiles match
        matched_member_ids = {m.id for m in members}
        if profession and self.employment:
            employment_matches = await self.employment.search_by_company(
                profession, list(matched_member_ids)
            )
            matched_from_employment = {e.member_id for e in employment_matches}
            matched_member_ids &= matched_from_employment

        if location and self.education:
            # location is resolved via school name for now (extend via member.address later)
            education_matches = await self.education.search_by_school(
                location, list(matched_member_ids)
            )
            matched_from_education = {e.member_id for e in education_matches}
            matched_member_ids &= matched_from_education

        # Build enriched results
        result_members = [m for m in members if m.id in matched_member_ids]
        total = len(result_members)
        result_members = result_members[skip:skip + limit]

        enriched = []
        for m in result_members:
            employment = []
            education = []
            if self.employment:
                employment = await self.employment.get_by_member(m.id)
            if self.education:
                education = await self.education.get_by_member(m.id)
            enriched.append({
                "id": str(m.id),
                "full_name": m.full_name,
                "gender": m.gender,
                "date_of_birth": str(m.date_of_birth) if m.date_of_birth else None,
                "is_alive": m.is_alive,
                "branch_id": str(m.branch_id) if m.branch_id else None,
                "status": m.status,
                "employment": [
                    {
                        "id": str(e.id),
                        "company_name": e.company_name,
                        "position": e.position,
                        "is_current": e.is_current,
                    }
                    for e in employment
                ],
                "education": [
                    {
                        "id": str(e.id),
                        "school_name": e.school_name,
                        "degree": e.degree,
                        "field_of_study": e.field_of_study,
                    }
                    for e in education
                ],
            })

        return {
            "members": enriched,
            "total": total,
            "skip": skip,
            "limit": limit,
        }

    async def get_member_profile(self, family_id: UUID, member_id: UUID) -> dict:
        """Get a full member profile with employment and education history (FR-DIR-02, FR-DIR-03)."""
        await self._ensure_family(family_id)
        member = await self._get_member(member_id)
        if member.family_id != family_id:
            raise NotFoundException("Member does not belong to this family")

        employment = []
        education = []
        if self.employment:
            employment = await self.employment.get_by_member(member_id)
        if self.education:
            education = await self.education.get_by_member(member_id)

        return {
            "id": str(member.id),
            "full_name": member.full_name,
            "gender": member.gender,
            "date_of_birth": str(member.date_of_birth) if member.date_of_birth else None,
            "date_of_death": str(member.date_of_death) if member.date_of_death else None,
            "is_alive": member.is_alive,
            "branch_id": str(member.branch_id) if member.branch_id else None,
            "status": member.status,
            "employment": [
                {
                    "id": str(e.id),
                    "company_name": e.company_name,
                    "position": e.position,
                    "start_date": str(e.start_date) if e.start_date else None,
                    "end_date": str(e.end_date) if e.end_date else None,
                    "is_current": e.is_current,
                    "description": e.description,
                }
                for e in employment
            ],
            "education": [
                {
                    "id": str(e.id),
                    "school_name": e.school_name,
                    "degree": e.degree,
                    "field_of_study": e.field_of_study,
                    "start_year": e.start_year,
                    "end_year": e.end_year,
                    "gpa": float(e.gpa) if e.gpa else None,
                }
                for e in education
            ],
        }

    async def update_employment(
        self,
        family_id: UUID,
        member_id: UUID,
        profile_id: UUID | None = None,
        company_name: str | None = None,
        position: str | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
        is_current: bool | None = None,
        description: str | None = None,
    ) -> EmploymentProfile:
        """Create or update a member's employment profile (FR-DIR-02)."""
        await self._ensure_family(family_id)
        member = await self._get_member(member_id)
        if member.family_id != family_id:
            raise NotFoundException("Member does not belong to this family")
        if not self.employment:
            raise RuntimeError("EmploymentRepository not injected")

        if profile_id:
            # Update existing profile
            profile = await self.employment.get_by_id(profile_id)
            if not profile or profile.member_id != member_id:
                raise NotFoundException("Employment profile not found")
            if company_name is not None:
                profile.company_name = company_name
            if position is not None:
                profile.position = position
            if start_date is not None:
                profile.start_date = start_date
            if end_date is not None:
                profile.end_date = end_date
            if is_current is not None:
                profile.is_current = is_current
            if description is not None:
                profile.description = description
            await self.employment.update(profile)
        else:
            # Create new employment profile
            if not company_name:
                raise ValidationException("company_name is required to create a new employment profile")
            profile = EmploymentProfile(
                id=uuid4(),
                member_id=member_id,
                company_name=company_name,
                position=position,
                start_date=start_date,
                end_date=end_date,
                is_current=is_current or False,
                description=description,
            )
            await self.employment.create(profile)

        await self._commit()
        return profile

    async def update_education(
        self,
        family_id: UUID,
        member_id: UUID,
        profile_id: UUID | None = None,
        school_name: str | None = None,
        degree: str | None = None,
        field_of_study: str | None = None,
        start_year: int | None = None,
        end_year: int | None = None,
        gpa: float | None = None,
    ) -> EducationProfile:
        """Create or update a member's education profile (FR-DIR-03)."""
        await self._ensure_family(family_id)
        member = await self._get_member(member_id)
        if member.family_id != family_id:
            raise NotFoundException("Member does not belong to this family")
        if not self.education:
            raise RuntimeError("EducationRepository not injected")

        if profile_id:
            # Update existing profile
            profile = await self.education.get_by_id(profile_id)
            if not profile or profile.member_id != member_id:
                raise NotFoundException("Education profile not found")
            if school_name is not None:
                profile.school_name = school_name
            if degree is not None:
                profile.degree = degree
            if field_of_study is not None:
                profile.field_of_study = field_of_study
            if start_year is not None:
                profile.start_year = start_year
            if end_year is not None:
                profile.end_year = end_year
            if gpa is not None:
                profile.gpa = gpa
            await self.education.update(profile)
        else:
            # Create new education profile
            if not school_name:
                raise ValidationException("school_name is required to create a new education profile")
            profile = EducationProfile(
                id=uuid4(),
                member_id=member_id,
                school_name=school_name,
                degree=degree,
                field_of_study=field_of_study,
                start_year=start_year,
                end_year=end_year,
                gpa=gpa,
            )
            await self.education.create(profile)

        await self._commit()
        return profile

    async def delete_employment(self, family_id: UUID, member_id: UUID, profile_id: UUID) -> None:
        """Delete an employment profile."""
        await self._ensure_family(family_id)
        member = await self._get_member(member_id)
        profile = await self.employment.get_by_id(profile_id) if self.employment else None
        if not profile or profile.member_id != member_id:
            raise NotFoundException("Employment profile not found")
        await self.employment.delete(profile)
        await self._commit()

    async def delete_education(self, family_id: UUID, member_id: UUID, profile_id: UUID) -> None:
        """Delete an education profile."""
        await self._ensure_family(family_id)
        member = await self._get_member(member_id)
        profile = await self.education.get_by_id(profile_id) if self.education else None
        if not profile or profile.member_id != member_id:
            raise NotFoundException("Education profile not found")
        await self.education.delete(profile)
        await self._commit()