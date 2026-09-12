"""Heritage and archive API endpoints (FR-HER-01 .. FR-HER-05)."""
from uuid import UUID
from fastapi import APIRouter, Depends, Query, status
from pydantic import BaseModel, Field
from app.api.dependencies import get_heritage_service, require_family_access
from app.services.heritage_service import HeritageService

router = APIRouter()


class HeritageItemCreate(BaseModel):
    item_type: str = Field(..., description="Heritage type: DOCUMENT|STORY|PHOTO|VIDEO|AUDIO|OTHER")
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


class MediaAssetCreate(BaseModel):
    url: str = Field(min_length=1, max_length=500)
    media_type: str = Field(..., description="IMAGE|VIDEO|AUDIO|DOCUMENT")
    caption: str | None = None
    uploaded_by: UUID


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_heritage_item(
    payload: HeritageItemCreate,
    family_id: UUID = Depends(require_family_access),
    svc: HeritageService = Depends(get_heritage_service),
):
    return await svc.create_heritage_item(
        actor_id=payload.branch_id or family_id,
        family_id=family_id,
        item_type=payload.item_type,
        title=payload.title,
        content=payload.content,
        branch_id=payload.branch_id,
        period=payload.period,
        category=payload.category,
        status=payload.status,
        media_url=payload.media_url,
    )


@router.get("")
async def list_heritage_items(
    family_id: UUID = Depends(require_family_access),
    item_type: str | None = Query(default=None, alias="type"),
    status: str | None = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    svc: HeritageService = Depends(get_heritage_service),
):
    return await svc.get_items(family_id, type_filter=item_type, status=status, skip=skip, limit=limit)


@router.get("/search")
async def search_heritage_items(
    family_id: UUID = Depends(require_family_access),
    q: str | None = Query(default=None, alias="q"),
    item_type: str | None = Query(default=None, alias="type"),
    category: str | None = None,
    period: str | None = None,
    status: str | None = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    svc: HeritageService = Depends(get_heritage_service),
):
    return await svc.search_items(
        family_id,
        query=q,
        type_filter=item_type,
        category=category,
        period=period,
        status=status,
        skip=skip,
        limit=limit,
    )


@router.get("/featured-members")
async def featured_members(
    family_id: UUID = Depends(require_family_access),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    svc: HeritageService = Depends(get_heritage_service),
):
    return await svc.list_featured_members(family_id, skip=skip, limit=limit)


@router.get("/stats")
async def heritage_stats(
    family_id: UUID = Depends(require_family_access),
    svc: HeritageService = Depends(get_heritage_service),
):
    return await svc.archive_stats(family_id)


@router.get("/{item_id}")
async def get_heritage_item(
    item_id: UUID,
    family_id: UUID = Depends(require_family_access),
    svc: HeritageService = Depends(get_heritage_service),
):
    return await svc.get_item(family_id, item_id)


@router.put("/{item_id}")
async def update_heritage_item(
    payload: HeritageItemUpdate,
    item_id: UUID,
    family_id: UUID = Depends(require_family_access),
    svc: HeritageService = Depends(get_heritage_service),
):
    return await svc.update_item(family_id, item_id, **payload.model_dump(exclude_none=True))


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_heritage_item(
    item_id: UUID,
    family_id: UUID = Depends(require_family_access),
    svc: HeritageService = Depends(get_heritage_service),
):
    await svc.delete_item(family_id, item_id)


# Media endpoints (FR-HER-04 photos, FR-HER-05 storage)
@router.post("/media", status_code=status.HTTP_201_CREATED)
async def add_media(
    payload: MediaAssetCreate,
    family_id: UUID = Depends(require_family_access),
    svc: HeritageService = Depends(get_heritage_service),
):
    return await svc.add_media(
        actor_id=payload.uploaded_by,
        family_id=family_id,
        **payload.model_dump(exclude={"uploaded_by"}, exclude_none=True),
    )


@router.get("/media")
async def list_media(
    family_id: UUID = Depends(require_family_access),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    svc: HeritageService = Depends(get_heritage_service),
):
    return await svc.list_media(family_id, skip=skip, limit=limit)