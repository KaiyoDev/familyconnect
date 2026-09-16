from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.models.community import Comment


class CommentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self,
        post_id: UUID,
        author_id: UUID,
        content: str,
    ) -> Comment:

        comment = Comment(
            post_id=post_id,
            author_id=author_id,
            content=content,
        )

        self.db.add(comment)
        await self.db.flush()
        await self.db.refresh(comment)

        return comment

    async def get_by_id(
        self,
        comment_id: UUID,
    ) -> Comment | None:

        result = await self.db.execute(
            select(Comment).where(Comment.id == comment_id)
        )

        return result.scalar_one_or_none()

    async def get_by_post(
        self,
        post_id: UUID,
        offset: int = 0,
        limit: int = 50,
    ) -> list[Comment]:

        result = await self.db.execute(
            select(Comment)
            .where(
                Comment.post_id == post_id,
                Comment.status != "REMOVED",
            )
            .order_by(Comment.created_at.asc())
            .offset(offset)
            .limit(limit)
        )

        return list(result.scalars().all())