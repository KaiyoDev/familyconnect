"""AI conversation & message repository."""
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.models.app_ai_model import AIConversation, AIMessage


class AIRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    # ---------------------------------------------------------------
    # CONVERSATIONS
    # ---------------------------------------------------------------

    async def create_conversation(
        self,
        user_id: UUID,
        title: str | None = None,
    ) -> AIConversation:
        conversation = AIConversation(user_id=user_id, title=title)
        self.db.add(conversation)
        await self.db.flush()
        await self.db.refresh(conversation)
        return conversation

    async def get_by_id(self, conversation_id: UUID) -> AIConversation | None:
        result = await self.db.execute(
            select(AIConversation).where(AIConversation.id == conversation_id)
        )
        return result.scalar_one_or_none()

    async def list_by_user(self, user_id: UUID, limit: int = 20, offset: int = 0) -> list[AIConversation]:
        result = await self.db.execute(
            select(AIConversation)
            .where(AIConversation.user_id == user_id)
            .order_by(AIConversation.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        return list(result.scalars().all())

    async def delete_conversation(self, conversation: AIConversation) -> None:
        await self.db.delete(conversation)
        await self.db.flush()

    # ---------------------------------------------------------------
    # MESSAGES
    # ---------------------------------------------------------------

    async def add_message(
        self,
        conversation_id: UUID,
        role: str,
        content: str,
    ) -> AIMessage:
        message = AIMessage(conversation_id=conversation_id, role=role, content=content)
        self.db.add(message)
        await self.db.flush()
        await self.db.refresh(message)
        return message

    async def get_messages(self, conversation_id: UUID) -> list[AIMessage]:
        result = await self.db.execute(
            select(AIMessage)
            .where(AIMessage.conversation_id == conversation_id)
            .order_by(AIMessage.created_at.asc())
        )
        return list(result.scalars().all())
