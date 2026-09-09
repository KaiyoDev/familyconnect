from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.models.community import PostReaction


class ReactionRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get(
        self,
        post_id: UUID,
        user_id: UUID,
        reaction_type: str,
    ) -> PostReaction | None:

        result = await self.db.execute(
            select(PostReaction).where(
                PostReaction.post_id == post_id,
                PostReaction.user_id == user_id,
                PostReaction.reaction_type == reaction_type,
            )
        )

        return result.scalar_one_or_none()

    async def create(
        self,
        post_id: UUID,
        user_id: UUID,
        reaction_type: str,
    ) -> PostReaction:

        reaction = PostReaction(
            post_id=post_id,
            user_id=user_id,
            reaction_type=reaction_type,
        )

        self.db.add(reaction)
        await self.db.flush()
        await self.db.refresh(reaction)

        return reaction

    async def delete(
        self,
        post_id: UUID,
        user_id: UUID,
        reaction_type: str,
    ) -> bool:

        result = await self.db.execute(
            delete(PostReaction).where(
                PostReaction.post_id == post_id,
                PostReaction.user_id == user_id,
                PostReaction.reaction_type == reaction_type,
            )
        )

        await self.db.flush()

        return result.rowcount > 0