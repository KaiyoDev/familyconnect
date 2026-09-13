"""Application service for member directory profiles (FR-DIR-01 .. FR-DIR-04)."""
from datetime import date
from uuid import UUID, uuid4
from collections import defaultdict
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.models.directory import EmploymentProfile, EducationProfile
from app.infrastructure.repositories.directory_repository import (
    MemberRepository,
    EmploymentRepository,
    EducationRepository,
)


class DirectoryService:
    """Coordinates directory / member profile operations (FR-DIR-01..04)."""

    def __init__(
        self,
        session: AsyncSession,
        member_repo: MemberRepository | None = None,
        employment_repo: EmploymentRepository | None = None,
        education_repo: EducationRepository | None = None,
    ):
        self.session = session
        self.members = member_repo or MemberRepository(session)
        self.employment = employment_repo or EmploymentRepository(session)
        self.education = education_repo or EducationRepository(session)

    # ── Directory listing (FR-DIR-01) ───────────────────────────────────

    async def get_directory(
        self,
        family_id: UUID,
        branch_id: UUID | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> dict:
        """List all members in a family directory.

        NOTE: generation filter is reserved for future use — requires genealogy
        relationship data not yet wired in this module.
        """
        members = await self.members.get_by_family(family_id)

        if branch_id:
            members = [m for m in members if m.branch_id == branch_id]

        total = len(members)
        page = members[skip: skip + limit]

        # Batch load profiles (avoids N+1 for paginated results)
        emp_map, edu_map = await self._batch_profiles([m.id for m in page])

        return {
            "members": [
                {
                    "id": str(m.id),
                    "full_name": m.full_name,
                    "gender": m.gender,
                    "date_of_birth": str(m.date_of_birth) if m.date_of_birth else None,
                    "is_alive": m.is_alive,
                    "branch_id": str(m.branch_id) if m.branch_id else None,
                    "status": m.status,
                    "employment": self._serialize_employment(emp_map.get(m.id, [])),
                    "education": self._serialize_education(edu_map.get(m.id, [])),
                }
                for m in page
            ],
            "total": total,
            "skip": skip,
            "limit": limit,
        }

    # ── Member search (FR-DIR-04) ───────────────────────────────────────

    async def search_members(
        self,
        family_id: UUID,
        query: str | None = None,
        profession: str | None = None,
        location: str | None = None,
        branch_id: UUID | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> dict:
        """Search members by name, profession, location (FR-DIR-04).

        Profession matches company_name OR position in employment profiles.
        Location matches school_name in education profiles (address field TBD).
        """
        members = await self.members.get_by_family(family_id)

        # In-memory filters
        if query:
            ql = query.lower()
            members = [m for m in members if ql in m.full_name.lower()]

        if branch_id:
            members = [m for m in members if m.branch_id == branch_id]

        matched_ids = {m.id for m in members}

        # Profession filter (company OR position)
        if profession and matched_ids:
            company_matches = await self.employment.search_by_company(profession, list(matched_ids))
            position_matches = await self.employment.search_by_position(profession, list(matched_ids))
            prof_matched = {e.member_id for e in company_matches} | {e.member_id for e in position_matches}
            matched_ids &= prof_matched

        # Location filter (school name)
        if location and matched_ids:
            school_matches = await self.education.search_by_school(location, list(matched_ids))
            loc_matched = {e.member_id for e in school_matches}
            matched_ids &= loc_matched if loc_matched else set()

        # Enrich results
        result_members = [m for m in members if m.id in matched_ids]
        total = len(result_members)
        page = result_members[skip: skip + limit]
        emp_map, edu_map = await self._batch_profiles([m.id for m in page])

        return {
            "members": [
                {
                    "id": str(m.id),
                    "full_name": m.full_name,
                    "gender": m.gender,
                    "date_of_birth": str(m.date_of_birth) if m.date_of_birth else None,
                    "is_alive": m.is_alive,
                    "branch_id": str(m.branch_id) if m.branch_id else None,
                    "status": m.status,
                    "employment": self._serialize_employment(emp_map.get(m.id, [])),
                    "education": self._serialize_education(edu_map.get(m.id, [])),
                }
                for m in page
            ],
            "total": total,
            "skip": skip,
            "limit": limit,
        }

    # ── Member profile (FR-DIR-02, FR-DIR-03) ───────────────────────────

    async def get_member_profile(self, family_id: UUID, member_id: UUID) -> dict:
        member = await self.members.get_by_id(member_id)
        if not member or member.family_id != family_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Member not found")

        emp_map, edu_map = await self._batch_profiles([member_id])
        return {
            "id": str(member.id),
            "full_name": member.full_name,
            "gender": member.gender,
            "date_of_birth": str(member.date_of_birth) if member.date_of_birth else None,
            "date_of_death": str(member.date_of_death) if member.date_of_death else None,
            "is_alive": member.is_alive,
            "branch_id": str(member.branch_id) if member.branch_id else None,
            "status": member.status,
            "employment": self._serialize_employment_full(emp_map.get(member_id, [])),
            "education": self._serialize_education_full(edu_map.get(member_id, [])),
        }

    # ── Employment CRUD (FR-DIR-02) ─────────────────────────────────────

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
        member = await self.members.get_by_id(member_id)
        if not member or member.family_id != family_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Member not found")

        if profile_id:
            profile = await self.employment.get_by_id(profile_id)
            if not profile or profile.member_id != member_id:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employment profile not found")
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
            return await self.employment.update(profile)
        else:
            if not company_name:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    detail="company_name is required to create a new employment profile")
            return await self.employment.create(EmploymentProfile(
                id=uuid4(),
                member_id=member_id,
                company_name=company_name,
                position=position,
                start_date=start_date,
                end_date=end_date,
                is_current=is_current or False,
                description=description,
            ))

    async def delete_employment(self, family_id: UUID, member_id: UUID, profile_id: UUID) -> None:
        member = await self.members.get_by_id(member_id)
        if not member or member.family_id != family_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Member not found")
        await self.employment.delete(profile_id)

    # ── Education CRUD (FR-DIR-03) ──────────────────────────────────────

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
        member = await self.members.get_by_id(member_id)
        if not member or member.family_id != family_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Member not found")

        if profile_id:
            profile = await self.education.get_by_id(profile_id)
            if not profile or profile.member_id != member_id:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Education profile not found")
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
            return await self.education.update(profile)
        else:
            if not school_name:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    detail="school_name is required to create a new education profile")
            return await self.education.create(EducationProfile(
                id=uuid4(),
                member_id=member_id,
                school_name=school_name,
                degree=degree,
                field_of_study=field_of_study,
                start_year=start_year,
                end_year=end_year,
                gpa=gpa,
            ))

    async def delete_education(self, family_id: UUID, member_id: UUID, profile_id: UUID) -> None:
        member = await self.members.get_by_id(member_id)
        if not member or member.family_id != family_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Member not found")
        await self.education.delete(profile_id)

    # ── Helpers ─────────────────────────────────────────────────────────

    async def _batch_profiles(self, member_ids: list[UUID]) -> tuple[dict, dict]:
        emp_map: dict = defaultdict(list)
        edu_map: dict = defaultdict(list)
        for mid in member_ids:
            for e in await self.employment.get_by_member(mid):
                emp_map[mid].append(e)
            for e in await self.education.get_by_member(mid):
                edu_map[mid].append(e)
        return emp_map, edu_map

    @staticmethod
    def _serialize_employment(items: list) -> list:
        return [{"id": str(e.id), "company_name": e.company_name, "position": e.position, "is_current": e.is_current} for e in items]

    @staticmethod
    def _serialize_education(items: list) -> list:
        return [{"id": str(e.id), "school_name": e.school_name, "degree": e.degree, "field_of_study": e.field_of_study} for e in items]

    @staticmethod
    def _serialize_employment_full(items: list) -> list:
        return [{"id": str(e.id), "company_name": e.company_name, "position": e.position,
                 "start_date": str(e.start_date) if e.start_date else None,
                 "end_date": str(e.end_date) if e.end_date else None,
                 "is_current": e.is_current, "description": e.description} for e in items]

    @staticmethod
    def _serialize_education_full(items: list) -> list:
        return [{"id": str(e.id), "school_name": e.school_name, "degree": e.degree,
                 "field_of_study": e.field_of_study, "start_year": e.start_year,
                 "end_year": e.end_year, "gpa": float(e.gpa) if e.gpa else None} for e in items]