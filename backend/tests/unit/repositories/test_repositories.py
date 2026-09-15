"""
FamilyConnect - Unit tests for repositories
"""
import pytest
from uuid import uuid4
from unittest.mock import AsyncMock, MagicMock, patch

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.user_repository import UserRepository
from app.infrastructure.repositories.admin_repository import AdminRepository
from app.infrastructure.repositories.family_repository import FamilyRepository


# ---------------------------------------------------------------------------
# Helper: create a mock that async session.execute() returns,
# where .scalars().first() / .scalars().all() work synchronously.
# ---------------------------------------------------------------------------
def make_scalar_result(first_value=None, all_values=None):
    """Return a mock that behaves like the result of session.execute().
    
    result.scalars().first() -> first_value
    result.scalars().all() -> all_values
    """
    result = MagicMock()
    scalars_mock = MagicMock()
    scalars_mock.first.return_value = first_value
    scalars_mock.all.return_value = all_values if all_values is not None else []
    result.scalars.return_value = scalars_mock
    return result


@pytest.fixture
def mock_db():
    db = AsyncMock(spec=AsyncSession)
    # session.execute is an async call, so we set execute.return_value via
    # the returned awaitable.
    db.execute = AsyncMock()
    db.commit = AsyncMock()
    db.refresh = AsyncMock()
    db.flush = AsyncMock()
    db.add = MagicMock()
    return db


# ---------------------------------------------------------------------------
# UserRepository
# ---------------------------------------------------------------------------

class TestUserRepository:

    @pytest.mark.asyncio
    async def test_exists_by_email_true(self, mock_db):
        """BR-US-001: Email exists"""
        mock_db.execute.return_value = make_scalar_result(first_value=MagicMock())
        repo = UserRepository(mock_db)
        result = await repo.exists_by_email("test@example.com")
        assert result is True

    @pytest.mark.asyncio
    async def test_exists_by_email_false(self, mock_db):
        """BR-US-001: Email not exists"""
        mock_db.execute.return_value = make_scalar_result(first_value=None)
        repo = UserRepository(mock_db)
        result = await repo.exists_by_email("new@example.com")
        assert result is False

    @pytest.mark.asyncio
    async def test_create_user(self, mock_db):
        """TC-US-001P: Create user via repository"""
        repo = UserRepository(mock_db)
        user_id = uuid4()
        mock_db.refresh = AsyncMock(side_effect=lambda obj: setattr(obj, 'id', user_id))

        result = await repo.create({
            "full_name": "Test", "email": "t@example.com",
            "password": "hash", "role": "USER", "status": "PENDING"
        })
        mock_db.add.assert_called_once()
        mock_db.commit.assert_called_once()
        mock_db.refresh.assert_called_once()
        assert result.id == user_id

    @pytest.mark.asyncio
    async def test_get_by_email_found(self, mock_db):
        """TC-US-002P: Get user by email found"""
        mock_user = MagicMock(spec=object)
        mock_user.email = "t@example.com"
        mock_db.execute.return_value = make_scalar_result(first_value=mock_user)

        repo = UserRepository(mock_db)
        result = await repo.get_by_email("t@example.com")
        assert result is not None
        assert result.email == "t@example.com"

    @pytest.mark.asyncio
    async def test_get_by_email_not_found(self, mock_db):
        """TC-US-002N4: Get non-existent email"""
        mock_db.execute.return_value = make_scalar_result(first_value=None)

        repo = UserRepository(mock_db)
        result = await repo.get_by_email("ghost@example.com")
        assert result is None

    @pytest.mark.asyncio
    async def test_get_by_id(self, mock_db):
        """TC-US-006P: Get user by ID"""
        uid = uuid4()
        mock_user = MagicMock(spec=object)
        mock_user.id = uid
        mock_user.full_name = "Test"
        mock_db.execute.return_value = make_scalar_result(first_value=mock_user)

        repo = UserRepository(mock_db)
        result = await repo.get_by_id(uid)
        assert result is not None
        assert result.full_name == "Test"

    @pytest.mark.asyncio
    async def test_update_user(self, mock_db):
        """TC-US-006P: Update user profile"""
        uid = uuid4()
        mock_user = MagicMock(spec=object)
        mock_user.id = uid
        mock_user.full_name = "New"

        # update() calls execute() twice: once for update stmt, once for get_by_id
        mock_db.execute.return_value = make_scalar_result(first_value=mock_user)

        repo = UserRepository(mock_db)
        result = await repo.update(uid, {"full_name": "New"})
        assert result is not None
        assert result.full_name == "New"
        assert mock_db.commit.call_count >= 1

    @pytest.mark.asyncio
    async def test_get_all(self, mock_db):
        """TC-US-001P: List all users"""
        mock_db.execute.return_value = make_scalar_result(all_values=[
            MagicMock(spec=object, id=uuid4(), email="a@b.com")
        ])
        repo = UserRepository(mock_db)
        result = await repo.get_all()
        assert len(result) == 1

    @pytest.mark.asyncio
    async def test_delete_user(self, mock_db):
        """TC-US-006N: Delete user"""
        mock_result = MagicMock()
        mock_result.rowcount = 1
        mock_db.execute.return_value = mock_result

        repo = UserRepository(mock_db)
        result = await repo.delete(uuid4())
        assert result is True
        mock_db.commit.assert_called_once()


# ---------------------------------------------------------------------------
# AdminRepository
# ---------------------------------------------------------------------------

class TestAdminRepository:

    @pytest.mark.asyncio
    async def test_list_users(self, mock_db):
        """TC-ADM-001P: List users"""
        mock_db.execute.return_value = make_scalar_result(all_values=[])
        repo = AdminRepository(mock_db)
        result = await repo.list_users(0, 20)
        assert result == []

    @pytest.mark.asyncio
    async def test_get_user_found(self, mock_db):
        """TC-ADM-001P2: Get user by ID"""
        uid = uuid4()
        mock_user = MagicMock()
        mock_user.id = uid
        mock_db.get = AsyncMock(return_value=mock_user)
        repo = AdminRepository(mock_db)
        result = await repo.get_user(uid)
        assert result is not None

    @pytest.mark.asyncio
    async def test_get_user_not_found(self, mock_db):
        """TC-ADM-001N: Get non-existent user"""
        mock_db.get = AsyncMock(return_value=None)
        repo = AdminRepository(mock_db)
        result = await repo.get_user(uuid4())
        assert result is None

    @pytest.mark.asyncio
    async def test_update_user_status(self, mock_db):
        """TC-ADM-001P2: Update user status"""
        user_mock = MagicMock()
        user_mock.id = uuid4()
        user_mock.status = "ACTIVE"
        mock_db.add = MagicMock()
        repo = AdminRepository(mock_db)
        result = await repo.update_user_status(user_mock, "BLOCKED")
        assert result == user_mock
        assert user_mock.status == "BLOCKED"
        mock_db.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_list_audit_logs(self, mock_db):
        """TC-ADM-003P: List audit logs"""
        mock_db.execute.return_value = make_scalar_result(all_values=[])
        repo = AdminRepository(mock_db)
        result = await repo.list_audit_logs(0, 50)
        assert result == []

    @pytest.mark.asyncio
    async def test_moderate_post(self, mock_db):
        """TC-ADM-002P: Moderate a post"""
        post_id = uuid4()
        mock_post = MagicMock(spec=object)
        mock_post.id = post_id
        mock_post.status = "PUBLISHED"
        mock_post.moderation_status = "PUBLISHED"
        mock_db.get = AsyncMock(return_value=mock_post)

        repo = AdminRepository(mock_db)
        result = await repo.moderate_post(post_id, "REMOVED")
        assert result is not None

    @pytest.mark.asyncio
    async def test_moderate_post_not_found(self, mock_db):
        """TC-ADM-002N: Moderate non-existent post"""
        mock_db.get = AsyncMock(return_value=None)
        repo = AdminRepository(mock_db)
        result = await repo.moderate_post(uuid4(), "REMOVED")
        assert result is None

    @pytest.mark.asyncio
    async def test_moderate_comment(self, mock_db):
        """TC-ADM-002P: Moderate a comment"""
        comment_id = uuid4()
        mock_comment = MagicMock()
        mock_comment.id = comment_id
        mock_comment.status = "PUBLISHED"
        mock_db.get = AsyncMock(return_value=mock_comment)
        repo = AdminRepository(mock_db)
        result = await repo.moderate_comment(comment_id, "REMOVED")
        assert result is not None

    @pytest.mark.asyncio
    async def test_add_audit_log(self, mock_db):
        """TC-ADM-003P: Add audit log"""
        repo = AdminRepository(mock_db)
        result = await repo.add_audit_log(action="BLOCK_USER", actor_id=uuid4(), resource_type="user")
        mock_db.add.assert_called_once()
        assert result is not None

    @pytest.mark.asyncio
    async def test_get_config(self, mock_db):
        """TC-ADM-005P: Get config"""
        mock_db.execute.return_value = make_scalar_result(all_values=[])
        repo = AdminRepository(mock_db)
        result = await repo.get_config()
        assert result == []

    @pytest.mark.asyncio
    async def test_update_config_new(self, mock_db):
        """TC-ADM-005P: Update config with new key"""
        mock_db.execute.return_value = make_scalar_result(all_values=[])
        repo = AdminRepository(mock_db)
        result = await repo.update_config({"new_key": "new_value"})
        mock_db.add.assert_called_once()
        assert result is not None

    @pytest.mark.asyncio
    async def test_list_users_with_filter(self, mock_db):
        """TC-ADM-001P: List users with role filter"""
        mock_db.execute.return_value = make_scalar_result(all_values=[])
        repo = AdminRepository(mock_db)
        result = await repo.list_users(0, 20, role="USER", status="ACTIVE")
        assert result == []


# ---------------------------------------------------------------------------
# FamilyRepository
# ---------------------------------------------------------------------------

class TestFamilyRepository:

    @pytest.mark.asyncio
    async def test_create_family(self, mock_db):
        """TC-FG-001P: Create family via repository"""
        repo = FamilyRepository(mock_db)

        family = MagicMock()
        family.id = uuid4()

        result = await repo.create(family)
        mock_db.add.assert_called_once()
        mock_db.flush.assert_called_once()
        assert result.id == family.id

    @pytest.mark.asyncio
    async def test_get_by_id(self, mock_db):
        """TC-FG-001P: Get family by ID"""
        mock_db.get = AsyncMock(return_value=MagicMock())
        repo = FamilyRepository(mock_db)
        result = await repo.get_by_id(uuid4())
        assert result is not None

    @pytest.mark.asyncio
    async def test_get_by_id_not_found(self, mock_db):
        """TC-FG-001N: Get non-existent family"""
        mock_db.get = AsyncMock(return_value=None)
        repo = FamilyRepository(mock_db)
        result = await repo.get_by_id(uuid4())
        assert result is None

    @pytest.mark.asyncio
    async def test_get_all(self, mock_db):
        """TC-FG-001P: Get all families"""
        mock_db.execute.return_value = make_scalar_result(all_values=[])
        repo = FamilyRepository(mock_db)
        result = await repo.get_all()
        assert result == []