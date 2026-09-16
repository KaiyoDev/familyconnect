"""
FamilyConnect - Unit tests for ai_service
"""
import pytest
from uuid import uuid4
from unittest.mock import AsyncMock, patch
from app.services.ai_service import AIService, ValidationError, NotFoundError


def make_repo_mock():
    repo = AsyncMock()
    return repo


class TestAIService:

    # ============ FR-AI-02: Conversation CRUD ============

    @pytest.mark.asyncio
    async def test_create_conversation(self):
        """TC-AI-002P: Create conversation"""
        repo = make_repo_mock()
        conv_id = uuid4()
        repo.create_conversation.return_value = {
            "id": conv_id, "user_id": uuid4(), "title": "Test"
        }
        service = AIService(repo)
        result = await service.create_conversation(uuid4(), "Test")
        assert result["id"] == str(conv_id)

    @pytest.mark.asyncio
    async def test_get_conversation_with_messages(self):
        """TC-AI-002P: Get conversation with messages"""
        repo = make_repo_mock()
        conv_id = uuid4()
        repo.get_by_id.return_value = {
            "id": conv_id, "user_id": uuid4(), "title": "Test"
        }
        repo.get_messages.return_value = [
            {"id": uuid4(), "conversation_id": conv_id, "role": "user", "content": "Hello"}
        ]
        service = AIService(repo)
        result = await service.get_conversation(conv_id)
        assert "messages" in result
        assert len(result["messages"]) == 1

    @pytest.mark.asyncio
    async def test_get_conversation_not_found(self):
        """TC-AI-002N: Conversation not found"""
        repo = make_repo_mock()
        repo.get_by_id.return_value = None
        service = AIService(repo)
        with pytest.raises(NotFoundError):
            await service.get_conversation(uuid4())

    @pytest.mark.asyncio
    async def test_list_conversations(self):
        """TC-AI-002P: List conversations by user"""
        repo = make_repo_mock()
        repo.list_by_user.return_value = [
            {"id": uuid4(), "user_id": uuid4(), "title": "Conv 1"},
            {"id": uuid4(), "user_id": uuid4(), "title": "Conv 2"},
        ]
        service = AIService(repo)
        result = await service.list_conversations(uuid4())
        assert len(result) == 2

    @pytest.mark.asyncio
    async def test_delete_conversation(self):
        """TC-AI-002P: Delete conversation"""
        repo = make_repo_mock()
        conv_id = uuid4()
        repo.get_by_id.return_value = {
            "id": conv_id, "user_id": uuid4(), "title": "Test"
        }
        service = AIService(repo)
        await service.delete_conversation(conv_id)
        repo.delete_conversation.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_conversation_not_found(self):
        """TC-AI-002N: Delete non-existent"""
        repo = make_repo_mock()
        repo.get_by_id.return_value = None
        service = AIService(repo)
        with pytest.raises(NotFoundError):
            await service.delete_conversation(uuid4())

    # ============ FR-AI-02: Chat ============

    @pytest.mark.asyncio
    async def test_chat_mock_provider(self):
        """TC-AI-002P: Chat with mock provider"""
        with patch("app.services.ai_service.settings") as mock_settings:
            mock_settings.ai_provider = "mock"
            mock_settings.ai_model = "mock-model"
            repo = make_repo_mock()
            repo.add_message.return_value = None
            service = AIService(repo)
            result = await service.chat(uuid4(), uuid4(), "Tết Nguyên Đán")
            assert "reply" in result
            assert result["provider"] == "mock"
            assert repo.add_message.call_count == 2  # user + assistant

    # ============ FR-AI-01: Semantic Search ============

    @pytest.mark.asyncio
    async def test_semantic_search(self):
        """TC-AI-001P: Semantic search returns results"""
        repo = make_repo_mock()
        service = AIService(repo)
        results = await service.semantic_search("bác sĩ trong gia đình")
        assert isinstance(results, list)
        assert len(results) > 0
        assert results[0]["type"] == "member"

    @pytest.mark.asyncio
    async def test_semantic_search_no_results(self):
        """TC-AI-001N: Semantic search handles edge case"""
        repo = make_repo_mock()
        service = AIService(repo)
        results = await service.semantic_search("ádfghjkl")
        assert isinstance(results, list)

    # ============ FR-AI-03: Explain Relationship ============

    @pytest.mark.asyncio
    async def test_explain_relationship_parent_child(self):
        """TC-AI-003P: Explain parent-child relationship"""
        repo = make_repo_mock()
        service = AIService(repo)
        result = await service.explain_relationship(
            uuid4(), uuid4(), "PARENT_CHILD"
        )
        assert "explanation" in result
        assert "PARENT_CHILD" in result["relationship_type"]

    @pytest.mark.asyncio
    async def test_explain_relationship_marriage(self):
        """TC-AI-003P: Explain marriage relationship"""
        repo = make_repo_mock()
        service = AIService(repo)
        result = await service.explain_relationship(
            uuid4(), uuid4(), "MARRIAGE"
        )
        assert "explanation" in result

    # ============ FR-AI-04: Summarize ============

    @pytest.mark.asyncio
    async def test_summarize_short(self):
        """TC-AI-004P: Summarize short mode"""
        repo = make_repo_mock()
        service = AIService(repo)
        result = await service.summarize("Đây là nội dung dài cần tóm tắt", "short")
        assert result["length_mode"] == "short"
        assert "summary" in result

    @pytest.mark.asyncio
    async def test_summarize_medium(self):
        """TC-AI-004P: Summarize medium mode"""
        repo = make_repo_mock()
        service = AIService(repo)
        result = await service.summarize("Nội dung dài", "medium")
        assert result["length_mode"] == "medium"

    @pytest.mark.asyncio
    async def test_summarize_full(self):
        """TC-AI-004P: Summarize full mode"""
        repo = make_repo_mock()
        service = AIService(repo)
        result = await service.summarize("Nội dung dài", "full")
        assert result["length_mode"] == "full"

    @pytest.mark.asyncio
    async def test_summarize_invalid_length(self):
        """TC-AI-004N: Invalid length -> ValidationError"""
        repo = make_repo_mock()
        service = AIService(repo)
        with pytest.raises(ValidationError):
            await service.summarize("Content", "invalid")