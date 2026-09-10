"""Family and genealogy API endpoints."""
from uuid import UUID
from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, Field
from app.api.dependencies import get_family_service, require_family_access
from app.services.family_service import FamilyService

router = APIRouter()


class FamilyCreate(BaseModel):
    creator_id: UUID
    family_name: str = Field(min_length=1, max_length=150)
    description: str | None = None


class FamilyUpdate(BaseModel):
    family_name: str | None = None
    description: str | None = None
    status: str | None = None


class MemberCreate(BaseModel):
    full_name: str = Field(min_length=1, max_length=100)
    branch_id: UUID | None = None
    gender: str = "UNKNOWN"


class RelationshipCreate(BaseModel):
    from_member_id: UUID
    to_member_id: UUID
    type: str
    notes: str | None = None


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_family(payload: FamilyCreate, svc: FamilyService = Depends(get_family_service)):
    return await svc.create_family(**payload.model_dump())


@router.get("")
async def list_families(svc: FamilyService = Depends(get_family_service)):
    return await svc.list_families()


@router.get("/{family_id}")
async def get_family(family_id: UUID, svc: FamilyService = Depends(get_family_service)):
    return await svc.get_family(family_id)


@router.put("/{family_id}")
async def update_family(payload: FamilyUpdate, family_id: UUID = Depends(require_family_access),
                        svc: FamilyService = Depends(get_family_service)):
    return await svc.update_family(family_id, **payload.model_dump(exclude_unset=True))


@router.delete("/{family_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_family(family_id: UUID = Depends(require_family_access),
                        svc: FamilyService = Depends(get_family_service)):
    await svc.delete_family(family_id)


@router.post("/{family_id}/members", status_code=status.HTTP_201_CREATED)
async def add_member(payload: MemberCreate, family_id: UUID = Depends(require_family_access),
                     svc: FamilyService = Depends(get_family_service)):
    return await svc.add_member(family_id, **payload.model_dump())


@router.get("/{family_id}/tree")
async def genealogy_tree(family_id: UUID = Depends(require_family_access),
                         svc: FamilyService = Depends(get_family_service)):
    return await svc.get_genealogy_tree(family_id)


@router.post("/{family_id}/relationships", status_code=status.HTTP_201_CREATED)
async def add_relationship(payload: RelationshipCreate, family_id: UUID = Depends(require_family_access),
                          svc: FamilyService = Depends(get_family_service)):
    return await svc.add_relationship(family_id, **payload.model_dump())
