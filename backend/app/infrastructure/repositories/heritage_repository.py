"""SQLAlchemy repository adapter for HeritageItem and MediaAsset."""
from uuid import UUID
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.interfaces.repository import IRepository
from app.infrastructure.models.heritage import HeritageItem, MediaAsset


class HeritageRepository(IRepository[HeritageItem]):
    """Repository for heritage item CRUD and search."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: UUID) -> HeritageItem | None:
        return await self.session.get(HeritageItem, item_id)

    async def get_by_family(self, family_id: UUID, skip: int = 0, limit: int = 100) -> list[HeritageItem]:
        result = await self.session.execute(
            select(HeritageItem)
            .where(HeritageItem.family_id == family_id)
            .offset(skip)
            .limit(limit)
            .order_by(HeritageItem.created_at.desc())
        )
        return list(result.scalars().all())

    async def create(self, item: HeritageItem) -> HeritageItem:
        self.session.add(item)
        await self.session.flush()
        return item

    async def update(self, item: HeritageItem) -> HeritageItem:
        await self.session.flush()
        return item

    async def delete(self, item: HeritageItem) -> None:
        await self.session.delete(item)
        await self.session.flush()

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
        """Search heritage items within a family with optional filters."""
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
        """Count heritage items in a family, optionally filtered by type."""
        stmt = select(HeritageItem).where(HeritageItem.family_id == family_id)
        if type_filter:
            stmt = stmt.where(HeritageItem.type == type_filter)
        result = await self.session.execute(stmt)
        return len(result.scalars().all())


class MediaRepository(IRepository[MediaAsset]):
    """Repository for media asset CRUD."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, asset_id: UUID) -> MediaAsset | None:
        return await self.session.get(MediaAsset, asset_id)

    async def get_by_family(self, family_id: UUID, skip: int = 0, limit: int = 100) -> list[MediaAsset]:
        result = await self.session.execute(
            select(MediaAsset)
            .where(MediaAsset.family_id == family_id)
            .offset(skip)
            .limit(limit)
            .order_by(MediaAsset.created_at.desc())
        )
        return list(result.scalars().all())

    async def get_by_event(self, event_id: UUID) -> list[MediaAsset]:
        result = await self.session.execute(
            select(MediaAsset).where(MediaAsset.event_id == event_id)
        )
        return list(result.scalars().all())

    async def create(self, asset: MediaAsset) -> MediaAsset:
        self.session.add(asset)
        await self.session.flush()
        return asset

    async def update(self, asset: MediaAsset) -> MediaAsset:
        await self.session.flush()
        return asset

    async def delete(self, asset: MediaAsset) -> None:
        await self.session.delete(asset)
        await self.session.flush()