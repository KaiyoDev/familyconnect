"""Heritage and archive API endpoints (FR-HER-01 .. FR-HER-05)."""
from uuid import UUID
from fastapi import APIRouter, Depends, Query, status
from pydantic import BaseModel, Field
from app.api.dependencies import get_current_user
from app.services.heritage_service import HeritageService
from app.infrastructure.databases.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.repositories.heritage_repository import HeritageRepository

# No /api prefix — frontend calls /families/{id}/heritage/... and /families/{id}/photos
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


class DocumentCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str | None = None
    period: str | None = None
    category: str | None = "GENERAL"
    media_url: str | None = None


class StoryCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str | None = None
    category: str | None = "GENERAL"
    media_url: str | None = None


class OutstandingCreate(BaseModel):
    member_id: UUID | None = None  # accepted; member linkage stored via content (no dedicated column yet)
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None


# ── Typed collections (documents / stories / outstanding / photos) ────────
# NOTE: these must be registered before the generic /heritage/{item_id} routes
# below, otherwise "documents"/"stories" would be captured as an (invalid) UUID.

@router.get("/families/{family_id}/heritage/documents")
async def list_documents(
    family_id: UUID,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.get_items(family_id, type_filter="DOCUMENT", skip=skip, limit=limit)


@router.post("/families/{family_id}/heritage/documents", status_code=status.HTTP_201_CREATED)
async def create_document(
    family_id: UUID,
    payload: DocumentCreate,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.create_heritage_item(
        family_id=family_id,
        item_type="DOCUMENT",
        title=payload.title,
        content=payload.content,
        period=payload.period,
        category=payload.category,
        media_url=payload.media_url,
    )


@router.put("/families/{family_id}/heritage/documents/{item_id}")
async def update_document(
    family_id: UUID,
    item_id: UUID,
    payload: HeritageItemUpdate,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.update_item(family_id, item_id, **payload.model_dump(exclude_none=True))


@router.delete("/families/{family_id}/heritage/documents/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_document(
    family_id: UUID,
    item_id: UUID,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    await svc.delete_item(family_id, item_id)


@router.post("/families/{family_id}/heritage/documents/{item_id}/approve")
async def approve_document(
    family_id: UUID,
    item_id: UUID,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.update_item(family_id, item_id, status="PUBLISHED")


@router.post("/families/{family_id}/heritage/documents/{item_id}/reject")
async def reject_document(
    family_id: UUID,
    item_id: UUID,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.update_item(family_id, item_id, status="DRAFT")


@router.get("/families/{family_id}/heritage/stories")
async def list_stories(
    family_id: UUID,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.get_items(family_id, type_filter="STORY", skip=skip, limit=limit)


@router.post("/families/{family_id}/heritage/stories", status_code=status.HTTP_201_CREATED)
async def create_story(
    family_id: UUID,
    payload: StoryCreate,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.create_heritage_item(
        family_id=family_id,
        item_type="STORY",
        title=payload.title,
        content=payload.content,
        category=payload.category,
        media_url=payload.media_url,
    )


@router.put("/families/{family_id}/heritage/stories/{item_id}")
async def update_story(
    family_id: UUID,
    item_id: UUID,
    payload: HeritageItemUpdate,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.update_item(family_id, item_id, **payload.model_dump(exclude_none=True))


@router.delete("/families/{family_id}/heritage/stories/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_story(
    family_id: UUID,
    item_id: UUID,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    await svc.delete_item(family_id, item_id)


@router.get("/families/{family_id}/heritage/outstanding")
async def list_outstanding(
    family_id: UUID,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.list_featured_members(family_id, skip=skip, limit=limit)


@router.post("/families/{family_id}/heritage/outstanding", status_code=status.HTTP_201_CREATED)
async def add_outstanding(
    family_id: UUID,
    payload: OutstandingCreate,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.create_heritage_item(
        family_id=family_id,
        item_type="OTHER",
        category="OUTSTANDING",
        title=payload.title,
        content=payload.description,
    )


@router.get("/families/{family_id}/photos")
async def list_photos(
    family_id: UUID,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.list_media(family_id, skip=skip, limit=limit)


# ── Generic heritage item routes (FR-HER-01 .. FR-HER-05) ────────────────

@router.post("/families/{family_id}/heritage", status_code=status.HTTP_201_CREATED)
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


@router.get("/families/{family_id}/heritage")
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


@router.get("/families/{family_id}/heritage/search")
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


@router.get("/families/{family_id}/heritage/featured-members")
async def featured_members(
    family_id: UUID,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.list_featured_members(family_id, skip=skip, limit=limit)


@router.get("/families/{family_id}/heritage/stats")
async def heritage_stats(
    family_id: UUID,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.archive_stats(family_id)


@router.get("/families/{family_id}/heritage/{item_id}")
async def get_heritage_item(
    family_id: UUID,
    item_id: UUID,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.get_item(family_id, item_id)


@router.put("/families/{family_id}/heritage/{item_id}")
async def update_heritage_item(
    family_id: UUID,
    item_id: UUID,
    payload: HeritageItemUpdate,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.update_item(family_id, item_id, **payload.model_dump(exclude_none=True))


@router.delete("/families/{family_id}/heritage/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_heritage_item(
    family_id: UUID,
    item_id: UUID,
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    await svc.delete_item(family_id, item_id)


@router.post("/families/{family_id}/heritage/media", status_code=status.HTTP_201_CREATED)
async def add_media(
    family_id: UUID,
    payload: MediaCreate,
    current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    user_id = UUID(str(current_user.get("id") or current_user.get("sub")))
    return await svc.add_media(family_id, uploaded_by=user_id, **payload.model_dump())


@router.get("/families/{family_id}/heritage/media")
async def list_media(
    family_id: UUID,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    _current_user: dict = Depends(get_current_user),
    svc: HeritageService = Depends(get_service),
):
    return await svc.list_media(family_id, skip=skip, limit=limit)
