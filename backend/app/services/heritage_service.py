"""Application service for heritage archival (FR-HER-01 .. FR-HER-05)."""
from uuid import UUID, uuid4
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.models.heritage import HeritageItem, MediaAsset
from app.infrastructure.repositories.heritage_repository import HeritageRepository

# Allowed heritage item types and statuses
HERITAGE_TYPES = {"DOCUMENT", "STORY", "PHOTO", "VIDEO", "AUDIO", "OTHER"}
HERITAGE_STATUSES = {"DRAFT", "PUBLISHED", "ARCHIVED", "HIDDEN"}


class HeritageService:
    """Coordinates heritage archival operations within a family."""

    def __init__(self, session: AsyncSession, repository: HeritageRepository | None = None):
        self.session = session
        self.repo = repository or HeritageRepository(session)

    # ── CRUD (FR-HER-01) ────────────────────────────────────────────────

    async def create_heritage_item(
        self,
        family_id: UUID,
        item_type: str,
        title: str,
        content: str | None = None,
        branch_id: UUID | None = None,
        period: str | None = None,
        category: str | None = "GENERAL",
        status: str = "DRAFT",
        media_url: str | None = None,
    ) -> HeritageItem:
        """Archive a new heritage artifact."""
        if item_type not in HERITAGE_TYPES:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail=f"Unsupported heritage type: {item_type}")
        if status not in HERITAGE_STATUSES:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail=f"Unsupported status: {status}")
        return await self.repo.create(HeritageItem(
            id=uuid4(),
            family_id=family_id,
            branch_id=branch_id,
            type=item_type,
            title=title,
            content=content,
            period=period,
            category=category or "GENERAL",
            status=status,
            media_url=media_url,
        ))

    async def get_items(
        self,
        family_id: UUID,
        type_filter: str | None = None,
        status: str | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> list[HeritageItem]:
        """List heritage items (FR-HER-05 archive browsing)."""
        return await self.repo.get_by_family(family_id, type_filter, status, skip, limit)

    async def get_item(self, family_id: UUID, item_id: UUID) -> HeritageItem:
        item = await self.repo.get_by_id(item_id)
        if not item or item.family_id != family_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Heritage item not found")
        return item

    async def update_item(self, family_id: UUID, item_id: UUID, **data) -> HeritageItem:
        item = await self.get_item(family_id, item_id)
        for key in ("title", "content", "period", "status", "media_url", "branch_id", "type", "category"):
            if key in data and data[key] is not None:
                setattr(item, key, data[key])
        return await self.repo.update(item)

    async def delete_item(self, family_id: UUID, item_id: UUID) -> None:
        item = await self.get_item(family_id, item_id)
        await self.repo.delete(item)

    # ── Search (FR-HER-02 stories, FR-HER-05) ───────────────────────────

    async def search_items(
        self,
        family_id: UUID,
        query: str | None = None,
        type_filter: str | None = None,
        category: str | None = None,
        period: str | None = None,
        status: str | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> list[HeritageItem]:
        return await self.repo.search(family_id, query, type_filter, category, period, status, skip, limit)

    # ── Featured members (FR-HER-03) ────────────────────────────────────

    async def list_featured_members(self, family_id: UUID, skip: int = 0, limit: int = 20) -> list[HeritageItem]:
        return await self.repo.search(family_id, type_filter="STORY", skip=skip, limit=limit)

    # ── Media (FR-HER-04 photos, FR-HER-05) ─────────────────────────────

    async def add_media(
        self,
        family_id: UUID,
        uploaded_by: UUID,
        url: str,
        media_type: str,
        caption: str | None = None,
    ) -> MediaAsset:
        if media_type not in {"IMAGE", "VIDEO", "AUDIO", "DOCUMENT"}:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail=f"Unsupported media type: {media_type}")
        return await self.repo.add_media(MediaAsset(
            id=uuid4(),
            family_id=family_id,
            uploaded_by=uploaded_by,
            url=url,
            media_type=media_type,
            caption=caption,
        ))

    async def list_media(self, family_id: UUID, skip: int = 0, limit: int = 100) -> list[MediaAsset]:
        return await self.repo.get_media_by_family(family_id, skip, limit)

    # ── Stats (FR-HER-05 warehouse) ─────────────────────────────────────

    async def archive_stats(self, family_id: UUID) -> dict:
        stats = {}
        for t in HERITAGE_TYPES:
            stats[t] = await self.repo.count_by_family(family_id, type_filter=t)
        return {
            "family_id": str(family_id),
            "total": sum(stats.values()),
            "by_type": stats,
        }