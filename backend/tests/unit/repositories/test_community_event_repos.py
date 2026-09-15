"""
FamilyConnect - Unit tests for community & event repositories
"""
import pytest
from uuid import uuid4
from unittest.mock import AsyncMock, MagicMock, patch

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.post_repository import PostRepository
from app.infrastructure.repositories.comment_repository import CommentRepository
from app.infrastructure.repositories.reaction_repository import ReactionRepository
from app.infrastructure.repositories.event_repository import EventRepository
from app.infrastructure.repositories.branch_repository import BranchRepository
from app.infrastructure.repositories.member_repository import MemberRepository
from app.infrastructure.repositories.relationship_repository import RelationshipRepository


# ---------------------------------------------------------------------------
# Helper: mock async DB result
# ---------------------------------------------------------------------------
def scalar_result(first_value=None, all_values=None):
    result = MagicMock()
    scalars = MagicMock()
    scalars.first.return_value = first_value
    scalars.all.return_value = all_values if all_values is not None else []
    result.scalars.return_value = scalars
    result.scalar_one_or_none = MagicMock(return_value=first_value)
    return result


@pytest.fixture
def db():
    db = AsyncMock(spec=AsyncSession)
    db.execute = AsyncMock()
    db.flush = AsyncMock()
    db.refresh = AsyncMock()
    db.add = MagicMock()
    db.delete = MagicMock()
    return db


# ---------------------------------------------------------------------------
# PostRepository
# ---------------------------------------------------------------------------

class TestPostRepository:
    @pytest.mark.asyncio
    async def test_create(self, db):
        repo = PostRepository(db)
        result = await repo.create(
            family_id=uuid4(), author_id=uuid4(),
            content="Hello", visibility_scope="FAMILY"
        )
        db.add.assert_called_once()
        db.flush.assert_called_once()
        db.refresh.assert_called_once()
        assert result is not None

    @pytest.mark.asyncio
    async def test_get_by_id(self, db):
        db.execute.return_value = scalar_result(first_value=MagicMock())
        repo = PostRepository(db)
        result = await repo.get_by_id(uuid4())
        assert result is not None

    @pytest.mark.asyncio
    async def test_get_by_id_not_found(self, db):
        db.execute.return_value = scalar_result(first_value=None)
        repo = PostRepository(db)
        result = await repo.get_by_id(uuid4())
        assert result is None

    @pytest.mark.asyncio
    async def test_get_feed(self, db):
        db.execute.return_value = scalar_result(all_values=[])
        repo = PostRepository(db)
        result = await repo.get_feed(uuid4(), 0, 20)
        assert result == []

    @pytest.mark.asyncio
    async def test_update(self, db):
        post = MagicMock()
        repo = PostRepository(db)
        result = await repo.update(post, content="Updated")
        db.flush.assert_called_once()
        assert result is not None

    @pytest.mark.asyncio
    async def test_delete(self, db):
        # post repo delete uses db.delete + flush (async)
        post = MagicMock()
        db.delete = AsyncMock()
        repo = PostRepository(db)
        await repo.delete(post)
        db.delete.assert_called_once_with(post)
        db.flush.assert_called_once()


# ---------------------------------------------------------------------------
# CommentRepository
# ---------------------------------------------------------------------------

class TestCommentRepository:
    @pytest.mark.asyncio
    async def test_create(self, db):
        db.refresh = AsyncMock()
        from app.infrastructure.repositories.comment_repository import CommentRepository
        repo = CommentRepository(db)
        result = await repo.create(post_id=uuid4(), author_id=uuid4(), content="Comment")
        db.add.assert_called_once()
        assert result is not None

    @pytest.mark.asyncio
    async def test_get_by_post(self, db):
        db.execute.return_value = scalar_result(all_values=[])
        from app.infrastructure.repositories.comment_repository import CommentRepository
        repo = CommentRepository(db)
        result = await repo.get_by_post(uuid4())
        assert result == []


# ---------------------------------------------------------------------------
# ReactionRepository
# ---------------------------------------------------------------------------

class TestReactionRepository:
    @pytest.mark.asyncio
    async def test_get(self, db):
        db.execute.return_value = scalar_result(first_value=None)
        from app.infrastructure.repositories.reaction_repository import ReactionRepository
        repo = ReactionRepository(db)
        result = await repo.get(post_id=uuid4(), user_id=uuid4(), reaction_type="like")
        assert result is None

    @pytest.mark.asyncio
    async def test_create(self, db):
        db.refresh = AsyncMock()
        from app.infrastructure.repositories.reaction_repository import ReactionRepository
        repo = ReactionRepository(db)
        result = await repo.create(post_id=uuid4(), user_id=uuid4(), reaction_type="like")
        db.add.assert_called_once()
        assert result is not None

    @pytest.mark.asyncio
    async def test_delete(self, db):
        mock_result = MagicMock()
        mock_result.rowcount = 1
        db.execute = AsyncMock(return_value=mock_result)
        from app.infrastructure.repositories.reaction_repository import ReactionRepository
        repo = ReactionRepository(db)
        result = await repo.delete(post_id=uuid4(), user_id=uuid4(), reaction_type="like")
        assert result is True


# ---------------------------------------------------------------------------
# EventRepository
# ---------------------------------------------------------------------------

class TestEventRepository:
    @pytest.mark.asyncio
    async def test_create(self, db):
        db.refresh = AsyncMock()
        repo = EventRepository(db)
        result = await repo.create({"title": "Event", "start_time": "2026-09-01", "family_id": uuid4(), "created_by": uuid4()})
        db.add.assert_called_once()
        assert result is not None

    @pytest.mark.asyncio
    async def test_get_by_family(self, db):
        mock_result = MagicMock()
        scalars_mock = MagicMock()
        scalars_mock.all.return_value = []
        mock_result.scalars.return_value = scalars_mock
        db.execute = AsyncMock(return_value=mock_result)
        repo = EventRepository(db)
        result = await repo.get_by_family(uuid4())
        assert result == []

    @pytest.mark.asyncio
    async def test_get_by_id_found(self, db):
        mock_result = MagicMock()
        scalars_mock = MagicMock()
        scalars_mock.first.return_value = MagicMock()
        mock_result.scalars.return_value = scalars_mock
        db.execute = AsyncMock(return_value=mock_result)
        repo = EventRepository(db)
        result = await repo.get_by_id(uuid4())
        assert result is not None

    @pytest.mark.asyncio
    async def test_get_by_id_not_found(self, db):
        mock_result = MagicMock()
        scalars_mock = MagicMock()
        scalars_mock.first.return_value = None
        mock_result.scalars.return_value = scalars_mock
        db.execute = AsyncMock(return_value=mock_result)
        repo = EventRepository(db)
        result = await repo.get_by_id(uuid4())
        assert result is None

    @pytest.mark.asyncio
    async def test_update(self, db):
        # update calls get_by_id which does db.execute
        mock_result = MagicMock()
        scalars_mock = MagicMock()
        scalars_mock.first.return_value = MagicMock()
        mock_result.scalars.return_value = scalars_mock
        db.execute = AsyncMock(return_value=mock_result)
        repo = EventRepository(db)
        result = await repo.update(uuid4(), {"title": "Updated"})
        assert result is not None

    @pytest.mark.asyncio
    async def test_delete_found(self, db):
        # delete calls get_by_id which does db.execute
        mock_result = MagicMock()
        scalars_mock = MagicMock()
        scalars_mock.first.return_value = MagicMock()
        mock_result.scalars.return_value = scalars_mock
        db.execute = AsyncMock(return_value=mock_result)
        db.delete = AsyncMock()
        repo = EventRepository(db)
        result = await repo.delete(uuid4())
        assert result is True

    @pytest.mark.asyncio
    async def test_delete_not_found(self, db):
        mock_result = MagicMock()
        scalars_mock = MagicMock()
        scalars_mock.first.return_value = None
        mock_result.scalars.return_value = scalars_mock
        db.execute = AsyncMock(return_value=mock_result)
        repo = EventRepository(db)
        result = await repo.delete(uuid4())
        assert result is False


# ---------------------------------------------------------------------------
# BranchRepository
# ---------------------------------------------------------------------------

class TestBranchRepository:
    @pytest.mark.asyncio
    async def test_create(self, db):
        db.refresh = AsyncMock()
        repo = BranchRepository(db)
        result = await repo.create({"name": "Nhánh 1", "family_id": uuid4()})
        db.add.assert_called_once()
        assert result is not None

    @pytest.mark.asyncio
    async def test_get_by_family(self, db):
        db.execute.return_value = scalar_result(all_values=[])
        repo = BranchRepository(db)
        result = await repo.get_by_family(uuid4())
        assert result == []

    @pytest.mark.asyncio
    async def test_get_by_id(self, db):
        db.get = AsyncMock(return_value=MagicMock())
        repo = BranchRepository(db)
        result = await repo.get_by_id(uuid4())
        assert result is not None


# ---------------------------------------------------------------------------
# MemberRepository
# ---------------------------------------------------------------------------

class TestMemberRepository:
    @pytest.mark.asyncio
    async def test_create(self, db):
        db.refresh = AsyncMock()
        repo = MemberRepository(db)
        result = await repo.create({"full_name": "Member", "family_id": uuid4()})
        db.add.assert_called_once()
        assert result is not None

    @pytest.mark.asyncio
    async def test_get_by_family(self, db):
        db.execute.return_value = scalar_result(all_values=[])
        repo = MemberRepository(db)
        result = await repo.get_by_family(uuid4())
        assert result == []


# ---------------------------------------------------------------------------
# RelationshipRepository
# ---------------------------------------------------------------------------

class TestRelationshipRepository:
    @pytest.mark.asyncio
    async def test_create(self, db):
        db.refresh = AsyncMock()
        repo = RelationshipRepository(db)
        result = await repo.create({"from_member_id": uuid4(), "to_member_id": uuid4(), "relationship_type": "PARENT_CHILD"})
        db.add.assert_called_once()
        assert result is not None

    @pytest.mark.asyncio
    async def test_get_by_member(self, db):
        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = []
        db.execute = AsyncMock(return_value=mock_result)
        from app.infrastructure.repositories.relationship_repository import RelationshipRepository
        repo = RelationshipRepository(db)
        result = await repo.get_by_family_members({"id1", "id2"})
        assert result == []