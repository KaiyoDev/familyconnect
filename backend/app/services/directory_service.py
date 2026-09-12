"""Application service for directory profiles and member search (FR-DIR-01 .. FR-DIR-04)."""
from datetime import date
from uuid import UUID, uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.exceptions import NotFoundException, ValidationException
from app.domain.interfaces.branch_repository import IBranchRepository
from app.domain.interfaces.family_repository import IFamilyRepository
from app.domain.interfaces.member_repository import IMemberRepository
from app.domain.interfaces.relationship_repository import IRelationshipRepository
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
        relationship_repository: IRelationshipRepository | None = None,
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
        self.relationships = relationship_repository
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

    async def _compute_generations(
        self, family_id: UUID, member_ids: list[UUID]
    ) -> dict[UUID, int]:
        """Compute generation depth for each member using PARENT_CHILD relationships.

        Generation 1 = root/oldest ancestor, 2 = their children, etc.
        Returns a dict mapping member_id -> generation number.
        """
        if not self.relationships:
            return {}
        member_id_set = {str(mid) for mid in member_ids}
        relationships = await self.relationships.get_by_family_members(member_id_set)

        # Build parent->children adjacency and find all children
        children: set[UUID] = set()
        parent_children: dict[UUID, list[UUID]] = {}
        for rel in relationships:
            if rel.type != "PARENT_CHILD":
                continue
            parent_id = rel.from_member_id
            child_id = rel.to_member_id
            children.add(child_id)
            parent_children.setdefault(parent_id, []).append(child_id)

        # Roots are members who are never a child in any PARENT_CHILD relationship
        roots = [mid for mid in member_ids if mid not in children]

        # If there are no PARENT_CHILD relationships at all, all members are roots
        if not roots:
            roots = member_ids

        # BFS from roots to assign generations
        generations: dict[UUID, int] = {}
        queue = [(rid, 1) for rid in roots]
        visited: set[UUID] = set()
        while queue:
            member_id, gen = queue.pop(0)
            if member_id in visited:
                continue
            visited.add(member_id)
            generations[member_id] = gen
            for child_id in parent_children.get(member_id, []):
                if child_id not in visited:
                    queue.append((child_id, gen + 1))

        return generations

    async def get_directory(
        self,
        family_id: UUID,
        branch_id: UUID | None = None,
        generation: int | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> dict:
        """List all members in a family directory (FR-DIR-01).

        Returns a dict with:
          - members: list of members with generation info
          - total: total count
        """
        await self._ensure_family(family_id)
        members = await self.members.get_by_family(family_id)

        if branch_id:
            members = [m for m in members if m.branch_id == branch_id]

        member_ids = [m.id for m in members]
        generations = await self._compute_generations(family_id, member_ids)

        # Filter by generation if provided
        if generation is not None:
            members = [
                m for m in members
                if generations.get(m.id) == generation
            ]

        total = len(members)
        members = members[skip: skip + limit]

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
                    "generation": generations.get(m.id),
                }
                for m in members
            ],
            "total": total,
            "skip": skip,
            "limit": limit,
        }

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
          - members: list of matching members with their current employment/education and generation
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

        member_ids = [m.id for m in members]

        # Compute generations for all members
        generations = await self._compute_generations(family_id, member_ids)

        # Filter by generation
        if generation is not None:
            members = [
                m for m in members
                if generations.get(m.id) == generation
            ]
            member_ids = [m.id for m in members]

        # Profession filter: match position OR company name
        matched_member_ids = {m.id for m in members}
        if profession and self.employment:
            # Search by both company name and position (profession could be either)
            company_matches = await self.employment.search_by_company(
                profession, list(matched_member_ids)
            )
            position_matches = await self.employment.search_by_position(
                profession, list(matched_member_ids)
            )
            matched_set = {e.member_id for e in company_matches} | {e.member_id for e in position_matches}
            matched_member_ids &= matched_set

        # Location filter: use school name as a proxy until a dedicated address field is added
        if location and self.education and matched_member_ids:
            school_matches = await self.education.search_by_school(
                location, list(matched_member_ids)
            )
            matched_from_education = {e.member_id for e in school_matches}
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
                "generation": generations.get(m.id),
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

        generations = await self._compute_generations(family_id, [member_id])

        return {
            "id": str(member.id),
            "full_name": member.full_name,
            "gender": member.gender,
            "generation": generations.get(member.id),
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