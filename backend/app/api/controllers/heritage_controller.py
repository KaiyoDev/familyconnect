"""Heritage and archive API endpoints (FR-HER-01 .. FR-HER-05)."""
from uuid import UUID
from fastapi import APIRouter, Depends, Query, status
from pydantic import BaseModel, Field
from app.api.dependencies import get_current_user
from app.services.heritage_service import HeritageService
from app.infrastructure.databases.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.repositories.heritage_repository import HeritageRepository

router = APIRouter(tags=["Heritage"])


def get_service(db: AsyncSession = Depends(get_db)) -> HeritageService:
    return HeritageService(db, HeritageRepository(db))


class HeritageItemCreate(BaseModel):
    item_type: str = Field(..., description="DOCUMENT|STORY|PHOTO|VIDEO|AUDIO|OTHER")
    title: str = Field(min_length=1, max_length=200)
    content: str | None = None
    branch_id: UUID | None = None
    period: str | None = None
    category: str | None = "GENERAL"
    status: str = "DRAFT"
    media_url: str | None = None


class HeritageItemUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    branch_id: UUID | None = None
    period: str | None = None
    category: str | None = None
    status: str | None = None
    media_url: str | None = None


class MediaCreate(BaseModel):
    url: str = Field(min_length=1, max_length=500)
    media_type: str = Field(..., description="IMAGE|VIDEO|AUDIO|DOCUMENT")
    caption: str | None = None


@router.post("/api/families/{family_id}/heritage", status_code=status.HTTP_201_CREATED)
async def create_heritage_item(
    family_id: UUID,
    payload: HeritageItemCreate,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.create_heritage_item(
        family_id=family_id,
        **payload.model_dump(),
    )


@router.get("/api/families/{family_id}/heritage")
async def list_heritage_items(
    family_id: UUID,
    item_type: str | None = Query(default=None, alias="type"),
    status: str | None = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.get_items(family_id, type_filter=item_type, status=status, skip=skip, limit=limit)


@router.get("/api/families/{family_id}/heritage/search")
async def search_heritage_items(
    family_id: UUID,
    q: str | None = Query(default=None),
    type: str | None = Query(default=None, alias="type"),
    category: str | None = None,
    period: str | None = None,
    status: str | None = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.search_items(family_id, query=q, type_filter=type, category=category,
                                  period=period, status=status, skip=skip, limit=limit)


@router.get("/api/families/{family_id}/heritage/featured-members")
async def featured_members(
    family_id: UUID,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.list_featured_members(family_id, skip=skip, limit=limit)


@router.get("/api/families/{family_id}/heritage/stats")
async def heritage_stats(
    family_id: UUID,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.archive_stats(family_id)


@router.get("/api/families/{family_id}/heritage/{item_id}")
async def get_heritage_item(
    family_id: UUID,
    item_id: UUID,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.get_item(family_id, item_id)


@router.put("/api/families/{family_id}/heritage/{item_id}")
async def update_heritage_item(
    family_id: UUID,
    item_id: UUID,
    payload: HeritageItemUpdate,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.update_item(family_id, item_id, **payload.model_dump(exclude_none=True))


@router.delete("/api/families/{family_id}/heritage/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_heritage_item(
    family_id: UUID,
    item_id: UUID,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    await svc.delete_item(family_id, item_id)


@router.post("/api/families/{family_id}/heritage/media", status_code=status.HTTP_201_CREATED)
async def add_media(
    family_id: UUID,
    payload: MediaCreate,
    current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    user_id = UUID(current_user["id"])
    return await svc.add_media(family_id, uploaded_by=user_id, **payload.model_dump())


@router.get("/api/families/{family_id}/heritage/media")
async def list_media(
    family_id: UUID,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.list_media(family_id, skip=skip, limit=limit)