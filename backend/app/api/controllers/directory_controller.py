"""Directory and member profile API endpoints (FR-DIR-01 .. FR-DIR-04)."""
from datetime import date
from uuid import UUID
from fastapi import APIRouter, Depends, Query, status
from pydantic import BaseModel, Field
from app.api.dependencies import get_current_user
from app.infrastructure.databases.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.repositories.directory_repository import (
    MemberRepository,
    EmploymentRepository,
    EducationRepository,
)
from app.services.directory_service import DirectoryService

router = APIRouter(tags=["Directory"])


def get_service(db: AsyncSession = Depends(get_db)) -> DirectoryService:
    return DirectoryService(
        db,
        MemberRepository(db),
        EmploymentRepository(db),
        EducationRepository(db),
    )


class EmploymentUpdate(BaseModel):
    profile_id: UUID | None = None
    company_name: str | None = Field(default=None, max_length=200)
    position: str | None = Field(default=None, max_length=100)
    start_date: date | None = None
    end_date: date | None = None
    is_current: bool | None = None
    description: str | None = None


class EducationUpdate(BaseModel):
    profile_id: UUID | None = None
    school_name: str | None = Field(default=None, max_length=200)
    degree: str | None = Field(default=None, max_length=100)
    field_of_study: str | None = Field(default=None, max_length=100)
    start_year: int | None = None
    end_year: int | None = None
    gpa: float | None = None


@router.get("/families/{family_id}/directory")
async def get_directory(
    family_id: UUID,
    branch_id: UUID | None = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    _current_user: dict = Depends(get_current_user),
    svc: DirectoryService = Depends(get_service),
):
    return await svc.get_directory(family_id, branch_id=branch_id, skip=skip, limit=limit)


@router.get("/families/{family_id}/directory/search")
async def search_members(
    family_id: UUID,
    q: str | None = Query(default=None),
    profession: str | None = None,
    location: str | None = None,
    branch_id: UUID | None = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    _current_user: dict = Depends(get_current_user),
    svc: DirectoryService = Depends(get_service),
):
    return await svc.search_members(family_id, query=q, profession=profession, location=location,
                                    branch_id=branch_id, skip=skip, limit=limit)


@router.get("/families/{family_id}/directory/members/{member_id}")
async def get_member_profile(
    family_id: UUID,
    member_id: UUID,
    _current_user: dict = Depends(get_current_user),
    svc: DirectoryService = Depends(get_service),
):
    return await svc.get_member_profile(family_id, member_id)


@router.post("/families/{family_id}/directory/members/{member_id}/employment", status_code=status.HTTP_201_CREATED)
async def create_employment(
    family_id: UUID,
    member_id: UUID,
    payload: EmploymentUpdate,
    _current_user: dict = Depends(get_current_user),
    svc: DirectoryService = Depends(get_service),
):
    return await svc.update_employment(
        family_id, member_id,
        profile_id=payload.profile_id, company_name=payload.company_name, position=payload.position,
        start_date=payload.start_date, end_date=payload.end_date,
        is_current=payload.is_current, description=payload.description,
    )


@router.put("/families/{family_id}/directory/members/{member_id}/employment/{profile_id}")
async def update_employment(
    family_id: UUID,
    member_id: UUID,
    profile_id: UUID,
    payload: EmploymentUpdate,
    _current_user: dict = Depends(get_current_user),
    svc: DirectoryService = Depends(get_service),
):
    return await svc.update_employment(
        family_id, member_id, profile_id=profile_id,
        company_name=payload.company_name, position=payload.position,
        start_date=payload.start_date, end_date=payload.end_date,
        is_current=payload.is_current, description=payload.description,
    )


@router.delete("/families/{family_id}/directory/members/{member_id}/employment/{profile_id}",
              status_code=status.HTTP_204_NO_CONTENT)
async def delete_employment(
    family_id: UUID,
    member_id: UUID,
    profile_id: UUID,
    _current_user: dict = Depends(get_current_user),
    svc: DirectoryService = Depends(get_service),
):
    await svc.delete_employment(family_id, member_id, profile_id)


@router.post("/families/{family_id}/directory/members/{member_id}/education", status_code=status.HTTP_201_CREATED)
async def create_education(
    family_id: UUID,
    member_id: UUID,
    payload: EducationUpdate,
    _current_user: dict = Depends(get_current_user),
    svc: DirectoryService = Depends(get_service),
):
    return await svc.update_education(
        family_id, member_id,
        profile_id=payload.profile_id, school_name=payload.school_name, degree=payload.degree,
        field_of_study=payload.field_of_study, start_year=payload.start_year,
        end_year=payload.end_year, gpa=payload.gpa,
    )


@router.put("/families/{family_id}/directory/members/{member_id}/education/{profile_id}")
async def update_education(
    family_id: UUID,
    member_id: UUID,
    profile_id: UUID,
    payload: EducationUpdate,
    _current_user: dict = Depends(get_current_user),
    svc: DirectoryService = Depends(get_service),
):
    return await svc.update_education(
        family_id, member_id, profile_id=profile_id,
        school_name=payload.school_name, degree=payload.degree,
        field_of_study=payload.field_of_study, start_year=payload.start_year,
        end_year=payload.end_year, gpa=payload.gpa,
    )


@router.delete("/families/{family_id}/directory/members/{member_id}/education/{profile_id}",
              status_code=status.HTTP_204_NO_CONTENT)
async def delete_education(
    family_id: UUID,
    member_id: UUID,
    profile_id: UUID,
    _current_user: dict = Depends(get_current_user),
    svc: DirectoryService = Depends(get_service),
):
    await svc.delete_education(family_id, member_id, profile_id)