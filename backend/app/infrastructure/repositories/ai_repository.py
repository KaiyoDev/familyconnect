"""AI conversation & message repository — uses raw SQL to avoid circular mapper config."""
from uuid import UUID
from datetime import datetime

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


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
    ) -> dict:
        """Insert and return conversation as dict (avoids ORM mapper config)."""
        now = datetime.utcnow()
        conv_id = UUID(int=__import__("uuid").uuid4().int)
        await self.db.execute(
            text(
                "INSERT INTO ai_conversations (id, user_id, title, created_at, updated_at)"
                " VALUES (:id, :user_id, :title, :now, :now)"
            ),
            {"id": conv_id, "user_id": user_id, "title": title, "now": now},
        )
        await self.db.commit()
        return {
            "id": str(conv_id),
            "user_id": str(user_id),
            "title": title,
            "created_at": now.isoformat(),
            "updated_at": now.isoformat(),
        }

    async def get_by_id(self, conversation_id: UUID) -> dict | None:
        result = await self.db.execute(
            text("SELECT id, user_id, title, created_at, updated_at FROM ai_conversations WHERE id = :id"),
            {"id": conversation_id},
        )
        row = result.fetchone()
        if not row:
            return None
        return {
            "id": str(row[0]),
            "user_id": str(row[1]),
            "title": row[2],
            "created_at": row[3].isoformat() if row[3] else None,
            "updated_at": row[4].isoformat() if row[4] else None,
        }

    async def list_by_user(self, user_id: UUID, limit: int = 20, offset: int = 0) -> list[dict]:
        result = await self.db.execute(
            text(
                "SELECT id, user_id, title, created_at, updated_at"
                " FROM ai_conversations WHERE user_id = :user_id"
                " ORDER BY created_at DESC LIMIT :limit OFFSET :offset"
            ),
            {"user_id": user_id, "limit": limit, "offset": offset},
        )
        rows = result.fetchall()
        return [
            {
                "id": str(r[0]),
                "user_id": str(r[1]),
                "title": r[2],
                "created_at": r[3].isoformat() if r[3] else None,
                "updated_at": r[4].isoformat() if r[4] else None,
            }
            for r in rows
        ]

    async def delete_conversation(self, conversation_id: UUID) -> bool:
        result = await self.db.execute(
            text("DELETE FROM ai_conversations WHERE id = :id"),
            {"id": conversation_id},
        )
        await self.db.commit()
        return result.rowcount > 0

    # ---------------------------------------------------------------
    # MESSAGES
    # ---------------------------------------------------------------

    async def add_message(
        self,
        conversation_id: UUID,
        role: str,
        content: str,
    ) -> dict:
        """Insert and return message as dict."""
        now = datetime.utcnow()
        msg_id = UUID(int=__import__("uuid").uuid4().int)
        await self.db.execute(
            text(
                "INSERT INTO ai_messages (id, conversation_id, role, content, created_at, updated_at)"
                " VALUES (:id, :conv_id, :role, :content, :now, :now)"
            ),
            {
                "id": msg_id,
                "conv_id": conversation_id,
                "role": role,
                "content": content,
                "now": now,
            },
        )
        await self.db.commit()
        return {
            "id": str(msg_id),
            "conversation_id": str(conversation_id),
            "role": role,
            "content": content,
            "created_at": now.isoformat(),
        }

    async def get_messages(self, conversation_id: UUID) -> list[dict]:
        result = await self.db.execute(
            text(
                "SELECT id, conversation_id, role, content, created_at"
                " FROM ai_messages WHERE conversation_id = :conv_id"
                " ORDER BY created_at ASC"
            ),
            {"conv_id": conversation_id},
        )
        rows = result.fetchall()
        return [
            {
                "id": str(r[0]),
                "conversation_id": str(r[1]),
                "role": r[2],
                "content": r[3],
                "created_at": r[4].isoformat() if r[4] else None,
            }
            for r in rows
        ]
