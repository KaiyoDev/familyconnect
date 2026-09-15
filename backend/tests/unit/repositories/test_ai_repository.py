"""
FamilyConnect - Unit tests for ai_repository
"""
import pytest
from uuid import uuid4
from unittest.mock import AsyncMock, MagicMock

from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.repositories.ai_repository import AIRepository


@pytest.fixture
def db():
    db = AsyncMock(spec=AsyncSession)
    db.execute = AsyncMock()
    db.commit = AsyncMock()
    return db


class TestAIRepository:

    @pytest.mark.asyncio
    async def test_create_conversation(self, db):
        """TC-AI-002P: Create conversation via repo"""
        repo = AIRepository(db)
        result = await repo.create_conversation(uuid4(), title="Test")
        assert result["title"] == "Test"
        assert "id" in result
        db.execute.assert_called_once()
        db.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_by_id_found(self, db):
        """TC-AI-002P: Get conversation by id"""
        uid = uuid4()
        row = MagicMock()
        row.__getitem__ = lambda self, i: [uid, uuid4(), "Title", None, None][i]
        row[0] = uuid4()
        row[1] = uuid4()
        row[2] = "Title"
        row[3] = None
        row[4] = None

        result_mock = MagicMock()
        result_mock.fetchone.return_value = row
        db.execute = AsyncMock(return_value=result_mock)

        repo = AIRepository(db)
        result = await repo.get_by_id(uid)
        assert result is not None
        assert result["title"] == "Title"

    @pytest.mark.asyncio
    async def test_get_by_id_not_found(self, db):
        """TC-AI-002N: Get non-existent conversation"""
        result_mock = MagicMock()
        result_mock.fetchone.return_value = None
        db.execute = AsyncMock(return_value=result_mock)

        repo = AIRepository(db)
        result = await repo.get_by_id(uuid4())
        assert result is None

    @pytest.mark.asyncio
    async def test_list_by_user(self, db):
        """TC-AI-002P: List conversations by user"""
        uid = uuid4()
        row = MagicMock()
        row.__getitem__ = lambda self, i: [uuid4(), uid, "Title", None, None][i]
        result_mock = MagicMock()
        result_mock.fetchall.return_value = [row, row]
        db.execute = AsyncMock(return_value=result_mock)

        repo = AIRepository(db)
        result = await repo.list_by_user(uid)
        assert len(result) == 2

    @pytest.mark.asyncio
    async def test_delete_conversation(self, db):
        """TC-AI-002P: Delete conversation"""
        result_mock = MagicMock()
        result_mock.rowcount = 1
        db.execute = AsyncMock(return_value=result_mock)

        repo = AIRepository(db)
        result = await repo.delete_conversation(uuid4())
        assert result is True
        db.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_add_message(self, db):
        """TC-AI-002P: Add message"""
        repo = AIRepository(db)
        result = await repo.add_message(uuid4(), "user", "Hello")
        assert result["role"] == "user"
        db.execute.assert_called_once()
        db.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_messages(self, db):
        """TC-AI-002P: Get messages"""
        conv_id = uuid4()
        row = MagicMock()
        row.__getitem__ = lambda self, i: [uuid4(), conv_id, "user", "Hello", None][i]
        result_mock = MagicMock()
        result_mock.fetchall.return_value = [row]
        db.execute = AsyncMock(return_value=result_mock)

        repo = AIRepository(db)
        result = await repo.get_messages(conv_id)
        assert len(result) == 1
        assert result[0]["role"] == "user"