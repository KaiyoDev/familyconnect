"""AI Assistant service — stub/mock implementation.

Swaps to a real provider (OpenAI / Claude) once an API key is available.
All methods are synchronous stubs that return deterministic mock data.
"""
from uuid import UUID
from datetime import datetime, timezone

from app.infrastructure.repositories.ai_repository import AIRepository


class AIError(Exception):
    pass


class NotFoundError(AIError):
    pass


class ValidationError(AIError):
    pass


# ---------------------------------------------------------------------------
# Deterministic mock data
# ---------------------------------------------------------------------------

MOCK_CHAT_RESPONSES = [
    "Gia đình bạn có truyền thống họp mặt vào dịp Tết Nguyên Đán hàng năm tại quê nội.",
    "Theo hồ sơ gia phả, họ Nguyễn của bạn có nguồn gốc từ tỉnh Nam Định, di cư vào Sài Gòn những năm 1954.",
    "Bạn có 12 thành viên trong gia đình, thuộc 3 nhánh chính. Nhánh lớn nhất là nhánh ông nội.",
    "Có 3 sự kiện gia đình sắp tới trong tháng: sinh nhật bà nội (15/9), giỗ cụ ngoại (22/9) và họp mặt nhánh nam (30/9).",
    "Câu chuyện gia đình nổi bật nhất là hành trình di cư năm 1954 của cụ tổ, được lưu trữ trong kho tư liệu số.",
]

MOCK_SEARCH_RESULTS = [
    {
        "type": "member",
        "id": "mock-member-1",
        "title": "Nguyễn Văn A",
        "snippet": "Thành viên nhánh nam, sinh năm 1950, nghề nghiệp: Giáo viên",
        "relevance": 0.92,
    },
    {
        "type": "story",
        "id": "mock-story-1",
        "title": "Hành trình di cư 1954",
        "snippet": "Câu chuyện về gia đình cụ tổ di cư từ Nam Định vào Sài Gòn...",
        "relevance": 0.87,
    },
    {
        "type": "event",
        "id": "mock-event-1",
        "title": "Họp mặt Tết Giáp Thìn 2024",
        "snippet": "Sự kiện họp mặt toàn nhánh tại quê nội, có 45 thành viên tham dự...",
        "relevance": 0.75,
    },
]

MOCK_EXPLAIN_RESPONSES = {
    "PARENT_CHILD": "là con của",
    "MARRIAGE": "là vợ/chồng của",
}

MOCK_SUMMARIES = {
    "short": "Tóm tắt ngắn gọn nội dung.",
    "medium": "Tóm tắt trung bình, bao gồm các ý chính và chi tiết quan trọng.",
    "full": "Tóm tắt đầy đủ nội dung, bao gồm mọi chi tiết đáng chú ý.",
}


# ---------------------------------------------------------------------------
# Service
# ---------------------------------------------------------------------------

class AIService:
    def __init__(self, repository: AIRepository):
        self.repo = repository

    # ---------------------------------------------------------------
    # Conversation CRUD
    # ---------------------------------------------------------------

    async def create_conversation(
        self,
        user_id: UUID,
        title: str | None = None,
    ) -> dict:
        conv = await self.repo.create_conversation(user_id=user_id, title=title)
        return self._conv_to_dict(conv)

    async def get_conversation(self, conversation_id: UUID) -> dict:
        conv = await self.repo.get_by_id(conversation_id)
        if conv is None:
            raise NotFoundError(f"Conversation {conversation_id} not found")
        messages = await self.repo.get_messages(conversation_id)
        return {**self._conv_to_dict(conv), "messages": [self._msg_to_dict(m) for m in messages]}

    async def list_conversations(self, user_id: UUID, limit: int = 20, offset: int = 0) -> list[dict]:
        convs = await self.repo.list_by_user(user_id, limit=limit, offset=offset)
        return [self._conv_to_dict(c) for c in convs]

    async def delete_conversation(self, conversation_id: UUID) -> None:
        conv = await self.repo.get_by_id(conversation_id)
        if conv is None:
            raise NotFoundError(f"Conversation {conversation_id} not found")
        await self.repo.delete_conversation(conv)

    # ---------------------------------------------------------------
    # Chat (stub — mock response)
    # ---------------------------------------------------------------

    async def chat(
        self,
        conversation_id: UUID,
        user_id: UUID,
        message: str,
    ) -> dict:
        """Create a user message and return a deterministic mock AI reply."""
        await self.repo.add_message(conversation_id, role="user", content=message)

        # Deterministic mock reply based on message length (simulates different intents)
        idx = len(message) % len(MOCK_CHAT_RESPONSES)
        reply = MOCK_CHAT_RESPONSES[idx]
        await self.repo.add_message(conversation_id, role="assistant", content=reply)

        return {"reply": reply, "provider": "mock"}

    # ---------------------------------------------------------------
    # Semantic search (stub)
    # ---------------------------------------------------------------

    async def semantic_search(self, query: str, family_id: UUID | None = None) -> list[dict]:
        """Return mock search results. Real implementation will use embedding + vector store."""
        del family_id  # unused in stub
        return MOCK_SEARCH_RESULTS

    # ---------------------------------------------------------------
    # Explain relationship (stub)
    # ---------------------------------------------------------------

    async def explain_relationship(
        self,
        member_a_id: UUID,
        member_b_id: UUID,
        relationship_type: str,
    ) -> dict:
        """Return a natural-language explanation of the relationship between two members."""
        label = MOCK_EXPLAIN_RESPONSES.get(relationship_type, "có quan hệ")
        return {
            "member_a_id": str(member_a_id),
            "member_b_id": str(member_b_id),
            "relationship_type": relationship_type,
            "explanation": f"{member_a_id} {label} {member_b_id}. "
                           f"Đây là quan hệ được xác nhận qua dữ liệu gia phả.",
            "source": "family_tree_graph",
        }

    # ---------------------------------------------------------------
    # Summarize (stub)
    # ---------------------------------------------------------------

    async def summarize(self, content: str, length: str = "medium") -> dict:
        """Return a mock summary of the given content."""
        if length not in ("short", "medium", "full"):
            raise ValidationError(f"Invalid length: {length}. Must be short/medium/full.")
        return {
            "original_length": len(content),
            "summary_length": len(MOCK_SUMMARIES[length]),
            "summary": MOCK_SUMMARIES[length],
            "length_mode": length,
        }

    # ---------------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------------

    @staticmethod
    def _conv_to_dict(conv: AIConversation) -> dict:
        return {
            "id": str(conv.id),
            "user_id": str(conv.user_id),
            "title": conv.title,
            "created_at": conv.created_at.isoformat() if conv.created_at else None,
            "updated_at": conv.updated_at.isoformat() if conv.updated_at else None,
        }

    @staticmethod
    def _msg_to_dict(msg: AIMessage) -> dict:
        return {
            "id": str(msg.id),
            "conversation_id": str(msg.conversation_id),
            "role": msg.role,
            "content": msg.content,
            "created_at": msg.created_at.isoformat() if msg.created_at else None,
        }
