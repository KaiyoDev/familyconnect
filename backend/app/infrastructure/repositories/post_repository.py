from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.models.community import Post


class PostRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self,
        family_id: UUID,
        author_id: UUID,
        content: str,
        visibility_scope: str = "FAMILY",
        branch_id: UUID | None = None,
        status: str = "PUBLISHED",
        media_urls: list | None = None,
    ) -> Post:
        post = Post(
            family_id=family_id,
            author_id=author_id,
            content=content,
            visibility_scope=visibility_scope,
            branch_id=branch_id,
            status=status,
            media_urls=media_urls,
        )

        self.db.add(post)
        await self.db.flush()
        await self.db.refresh(post)

        return post

    async def get_by_id(self, post_id: UUID) -> Post | None:
        result = await self.db.execute(
            select(Post).where(Post.id == post_id)
        )

        return result.scalar_one_or_none()

    async def get_feed(
        self,
        family_id: UUID,
        offset: int,
        limit: int,
    ) -> list[Post]:

        result = await self.db.execute(
            select(Post)
            .where(
                Post.family_id == family_id,
                Post.status == "PUBLISHED",
            )
            .order_by(Post.created_at.desc())
            .offset(offset)
            .limit(limit)
        )

        return list(result.scalars().all())

    async def update(
        self,
        post: Post,
        content: str | None = None,
        media_urls: list | None = None,
        visibility_scope: str | None = None,
        branch_id: UUID | None = None,
    ) -> Post:

        if content is not None:
            post.content = content

        if media_urls is not None:
            post.media_urls = media_urls

        if visibility_scope is not None:
            post.visibility_scope = visibility_scope

        if branch_id is not None:
            post.branch_id = branch_id

        await self.db.flush()
        await self.db.refresh(post)

        return post

    async def delete(self, post: Post):
        await self.db.delete(post)
        await self.db.flush()