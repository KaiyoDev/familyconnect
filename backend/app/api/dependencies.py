"""FastAPI dependency factories."""
from uuid import UUID
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.databases.database import get_db
from app.infrastructure.repositories.branch_repository import BranchRepository
from app.infrastructure.repositories.family_repository import FamilyRepository
from app.infrastructure.repositories.member_repository import MemberRepository
from app.infrastructure.repositories.relationship_repository import RelationshipRepository
from app.infrastructure.repositories.sqlalchemy_unit_of_work import SQLAlchemyUnitOfWork
from app.services.family_service import FamilyService


async def require_family_access(family_id: UUID, db: AsyncSession = Depends(get_db)) -> UUID:
    """Temporary authorization seam until the authentication task is integrated."""
    if not family_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid family id")
    return family_id


def get_family_service(db: AsyncSession = Depends(get_db)) -> FamilyService:
    return FamilyService(
        db,
        family_repository=FamilyRepository(db),
        member_repository=MemberRepository(db),
        relationship_repository=RelationshipRepository(db),
        branch_repository=BranchRepository(db),
        unit_of_work=SQLAlchemyUnitOfWork(db),
    )


__all__ = ["get_db", "get_family_service", "require_family_access"]
