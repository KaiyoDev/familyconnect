"""SQLAlchemy repository adapter for heritage archival (FR-HER-01 .. FR-HER-05)."""
from uuid import UUID
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.models.heritage import HeritageItem, MediaAsset


class HeritageRepository:
    """Repository for heritage items and media assets within a family (FR-HER-01, FR-HER-04)."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: UUID) -> HeritageItem | None:
        return await self.session.get(HeritageItem, item_id)

    async def get_by_family(
        self,
        family_id: UUID,
        type_filter: str | None = None,
        status: str | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> list[HeritageItem]:
        stmt = select(HeritageItem).where(HeritageItem.family_id == family_id)
        if type_filter:
            stmt = stmt.where(HeritageItem.type == type_filter)
        if status:
            stmt = stmt.where(HeritageItem.status == status)
        stmt = stmt.offset(skip).limit(limit).order_by(HeritageItem.created_at.desc())
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def search(
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
        """Search heritage items with optional text + filters (FR-HER-02 stories, FR-HER-05)."""
        stmt = select(HeritageItem).where(HeritageItem.family_id == family_id)
        if query:
            like_pattern = f"%{query}%"
            stmt = stmt.where(
                or_(
                    HeritageItem.title.ilike(like_pattern),
                    HeritageItem.content.ilike(like_pattern),
                )
            )
        if type_filter:
            stmt = stmt.where(HeritageItem.type == type_filter)
        if category:
            stmt = stmt.where(HeritageItem.category == category)
        if period:
            stmt = stmt.where(HeritageItem.period == period)
        if status:
            stmt = stmt.where(HeritageItem.status == status)
        stmt = stmt.offset(skip).limit(limit).order_by(HeritageItem.created_at.desc())
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def count_by_family(self, family_id: UUID, type_filter: str | None = None) -> int:
        stmt = select(HeritageItem).where(HeritageItem.family_id == family_id)
        if type_filter:
            stmt = stmt.where(HeritageItem.type == type_filter)
        result = await self.session.execute(stmt)
        return len(result.scalars().all())

    async def create(self, item: HeritageItem) -> HeritageItem:
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def update(self, item: HeritageItem) -> HeritageItem:
        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def delete(self, item: HeritageItem) -> None:
        await self.session.delete(item)
        await self.session.commit()

    # ── Media assets (FR-HER-04 photos) ────────────────────────────────

    async def add_media(self, asset: MediaAsset) -> MediaAsset:
        self.session.add(asset)
        await self.session.commit()
        await self.session.refresh(asset)
        return asset

    async def get_media_by_family(
        self, family_id: UUID, skip: int = 0, limit: int = 100
    ) -> list[MediaAsset]:
        stmt = (
            select(MediaAsset)
            .where(MediaAsset.family_id == family_id)
            .offset(skip)
            .limit(limit)
            .order_by(MediaAsset.created_at.desc())
        )
        result = await self.session.execute(stmt)
        return list(result.scalars().all())
