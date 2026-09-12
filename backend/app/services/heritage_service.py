"""Application service for heritage and archival use cases (FR-HER-01 .. FR-HER-05)."""
from uuid import UUID, uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.exceptions import NotFoundException, ValidationException
from app.domain.interfaces.branch_repository import IBranchRepository
from app.domain.interfaces.family_repository import IFamilyRepository
from app.domain.interfaces.repository import IRepository
from app.domain.interfaces.unit_of_work import IUnitOfWork
from app.infrastructure.models.heritage import HeritageItem, MediaAsset


# Allowed heritage item types and statuses (FR-HER-01 archives, FR-HER-04 photos).
HERITAGE_TYPES = {"DOCUMENT", "STORY", "PHOTO", "VIDEO", "AUDIO", "OTHER"}
HERITAGE_STATUSES = {"DRAFT", "PUBLISHED", "ARCHIVED", "HIDDEN"}
STORAGE_TYPE = "ARCHIVE"


class HeritageService:
    """Coordinates heritage archival operations within a family."""

    def __init__(
        self,
        session: AsyncSession,
        family_repository: IFamilyRepository | None = None,
        branch_repository: IBranchRepository | None = None,
        heritage_repository: IRepository[HeritageItem] | None = None,
        media_repository: IRepository[MediaAsset] | None = None,
        unit_of_work: IUnitOfWork | None = None,
    ):
        self.session = session
        if not all((family_repository, heritage_repository, unit_of_work)):
            raise ValueError("Repositories and unit_of_work must be injected")
        self.families = family_repository
        self.branches = branch_repository
        self.heritage = heritage_repository
        self.media = media_repository
        self.unit_of_work = unit_of_work

    async def _commit(self) -> None:
        await self.unit_of_work.commit()

    async def _rollback(self) -> None:
        await self.unit_of_work.rollback()

    async def _write(self, operation):
        try:
            result = await operation()
            await self._commit()
            return result
        except Exception:
            await self._rollback()
            raise

    async def _ensure_family(self, family_id: UUID):
        family = await self.families.get_by_id(family_id)
        if not family:
            raise NotFoundException("Family not found")
        return family

    async def create_heritage_item(
        self,
        actor_id: UUID,
        family_id: UUID,
        item_type: str,
        title: str,
        content: str | None = None,
        branch_id: UUID | None = None,
        period: str | None = None,
        category: str | None = None,
        status: str = "DRAFT",
        media_url: str | None = None,
    ) -> HeritageItem:
        """Archive a new heritage artifact (FR-HER-01, FR-HER-04)."""
        await self._ensure_family(family_id)
        if item_type not in HERITAGE_TYPES:
            raise ValidationException(f"Unsupported heritage type: {item_type}")
        if status not in HERITAGE_STATUSES:
            raise ValidationException(f"Unsupported status: {status}")
        if branch_id and self.branches:
            branch = await self.branches.get_by_id(branch_id)
            if not branch or branch.family_id != family_id:
                raise ValidationException("Branch does not belong to the family")

        kwargs = {
            "type": item_type,
        }
        item = HeritageItem(
            id=uuid4(),
            family_id=family_id,
            branch_id=branch_id,
            title=title,
            content=content,
            period=period,
            category=category or "GENERAL",
            status=status,
            media_url=media_url,
            **kwargs,
        )
        await self.heritage.create(item)
        await self._commit()
        return item

    async def get_items(
        self,
        family_id: UUID,
        type_filter: str | None = None,
        status: str | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> list[HeritageItem]:
        """List heritage items in a family (FR-HER-05 archive browsing)."""
        await self._ensure_family(family_id)
        if type_filter:
            items = await self.heritage.search(
                family_id, type_filter=type_filter, status=status, skip=skip, limit=limit
            )
        else:
            items = await self.heritage.search(
                family_id, status=status, skip=skip, limit=limit
            )
        return items

    async def get_item(self, family_id: UUID, item_id: UUID) -> HeritageItem:
        """Fetch a single heritage item within a family (FR-HER-01)."""
        item = await self.heritage.get_by_id(item_id)
        if not item or item.family_id != family_id:
            raise NotFoundException("Heritage item not found")
        return item

    async def update_item(
        self, family_id: UUID, item_id: UUID, **data
    ) -> HeritageItem:
        """Update a heritage item (FR-HER-01)."""
        item = await self.get_item(family_id, item_id)
        for key in ("title", "content", "period", "status", "media_url", "branch_id", "type"):
            if key in data and data[key] is not None:
                setattr(item, key, data[key])
        await self.heritage.update(item)
        await self._commit()
        return item

    async def delete_item(self, family_id: UUID, item_id: UUID) -> None:
        """Delete a heritage item (FR-HER-01)."""
        item = await self.get_item(family_id, item_id)
        await self.heritage.delete(item)
        await self._commit()

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
        """Full-text / filter search across the heritage archive (FR-HER-02 stories, FR-HER-05)."""
        await self._ensure_family(family_id)
        return await self.heritage.search(
            family_id,
            query=query,
            type_filter=type_filter,
            category=category,
            period=period,
            status=status,
            skip=skip,
            limit=limit,
        )

    async def list_featured_members(
        self, family_id: UUID, skip: int = 0, limit: int = 20
    ) -> list[HeritageItem]:
        """List featured/outstanding members as story-type heritage items (FR-HER-03)."""
        await self._ensure_family(family_id)
        return await self.heritage.search(
            family_id,
            type_filter="STORY",
            skip=skip,
            limit=limit,
        )

    async def add_media(
        self,
        actor_id: UUID,
        family_id: UUID,
        uploaded_by: UUID,
        url: str,
        media_type: str,
        caption: str | None = None,
    ) -> MediaAsset:
        """Attach a media asset to a family archive (FR-HER-04 photos)."""
        await self._ensure_family(family_id)
        if media_type not in {"IMAGE", "VIDEO", "AUDIO", "DOCUMENT"}:
            raise ValidationException(f"Unsupported media type: {media_type}")
        asset = MediaAsset(
            id=uuid4(),
            family_id=family_id,
            uploaded_by=uploaded_by,
            url=url,
            media_type=media_type,
            caption=caption,
        )
        if self.media:
            await self.media.create(asset)
        else:
            self.session.add(asset)
        await self._commit()
        return asset

    async def list_media(
        self, family_id: UUID, skip: int = 0, limit: int = 100
    ) -> list[MediaAsset]:
        """List media in a family's archive (FR-HER-04, FR-HER-05)."""
        if not self.media:
            return []
        await self._ensure_family(family_id)
        return await self.media.get_by_family(family_id, skip=skip, limit=limit)

    async def archive_stats(self, family_id: UUID) -> dict:
        """Return archive counts per type (FR-HER-05 storage overview)."""
        await self._ensure_family(family_id)
        stats = {t: 0 for t in HERITAGE_TYPES}
        for t in HERITAGE_TYPES:
            stats[t] = await self.heritage.count_by_family(family_id, type_filter=t)
        return {
            "family_id": str(family_id),
            "total": sum(stats.values()),
            "by_type": stats,
            "storage_type": STORAGE_TYPE,
        }