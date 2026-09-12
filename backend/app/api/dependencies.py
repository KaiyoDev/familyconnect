"""FastAPI dependency factories."""
from uuid import UUID
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.auth import require_family_membership as require_family_membership_auth
from app.infrastructure.databases.database import get_db
from app.infrastructure.repositories.branch_repository import BranchRepository
from app.infrastructure.repositories.directory_repository import (
    EducationRepository,
    EmploymentRepository,
)
from app.infrastructure.repositories.family_repository import FamilyRepository
from app.infrastructure.repositories.heritage_repository import HeritageRepository, MediaRepository
from app.infrastructure.repositories.member_repository import MemberRepository
from app.infrastructure.repositories.relationship_repository import RelationshipRepository
from app.infrastructure.repositories.sqlalchemy_unit_of_work import SQLAlchemyUnitOfWork
from app.services.directory_service import DirectoryService
from app.services.family_service import FamilyService
from app.services.heritage_service import HeritageService


async def require_family_access(family_id: UUID, db: AsyncSession = Depends(get_db)) -> UUID:
    """Temporary authorization seam — validates family id existence.

    NOTE: Used by legacy family_controller. New controllers use require_family_membership.
    """
    if not family_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid family id")
    return family_id


# RBAC-aware variant that also verifies the user belongs to the family
require_family_membership = require_family_membership_auth


def get_family_service(db: AsyncSession = Depends(get_db)) -> FamilyService:
    return FamilyService(
        db,
        family_repository=FamilyRepository(db),
        member_repository=MemberRepository(db),
        relationship_repository=RelationshipRepository(db),
        branch_repository=BranchRepository(db),
        unit_of_work=SQLAlchemyUnitOfWork(db),
    )


def get_heritage_service(db: AsyncSession = Depends(get_db)) -> HeritageService:
    return HeritageService(
        db,
        family_repository=FamilyRepository(db),
        branch_repository=BranchRepository(db),
        heritage_repository=HeritageRepository(db),
        media_repository=MediaRepository(db),
        unit_of_work=SQLAlchemyUnitOfWork(db),
    )


def get_directory_service(db: AsyncSession = Depends(get_db)) -> DirectoryService:
    return DirectoryService(
        db,
        family_repository=FamilyRepository(db),
        member_repository=MemberRepository(db),
        branch_repository=BranchRepository(db),
        relationship_repository=RelationshipRepository(db),
        employment_repository=EmploymentRepository(db),
        education_repository=EducationRepository(db),
        unit_of_work=SQLAlchemyUnitOfWork(db),
    )


__all__ = [
    "get_db",
    "get_family_service",
    "get_heritage_service",
    "get_directory_service",
    "require_family_access",
    "require_family_membership",
]