"""
FamilyConnect - Unit tests for auth_service, admin_service, community_service
"""
import pytest
from uuid import uuid4
from unittest.mock import AsyncMock, MagicMock, patch

from app.infrastructure.models.user import User
from app.services.auth_service import AuthService, hash_password, verify_password


# ============================================================
# Auth Service Tests (FR-US-01, FR-US-02, FR-US-04)
# ============================================================

class TestAuthService:
    """Test framework"""

    @pytest.mark.asyncio
    async def test_register_success(self):
        """TC-US-001P: Register new user successfully"""
        mock_repo = AsyncMock()
        mock_repo.exists_by_email.return_value = False
        user_id = uuid4()
        mock_repo.create.return_value = User(
            id=user_id, full_name="Test User", email="new@example.com",
            status="PENDING", role="USER"
        )
        from app.schemas.auth import RegisterRequest
        from app.services.auth_service import AuthService
        service = AuthService(mock_repo)
        dto = RegisterRequest(
            full_name="Test User", email="new@example.com",
            password="Abc12345"
        )
        with patch("app.services.auth_service.hash_password", return_value="$2b$12$mockhash"):
            result = await service.register(dto)
        assert result.email == "new@example.com"
        assert result.status == "PENDING"
        mock_repo.exists_by_email.assert_called_once_with("new@example.com")
        mock_repo.create.assert_called_once()

    @pytest.mark.asyncio
    async def test_register_duplicate_email(self):
        """TC-US-001N: Register with existing email -> 400"""
        mock_repo = AsyncMock()
        mock_repo.exists_by_email.return_value = True
        from app.schemas.auth import RegisterRequest
        from app.services.auth_service import AuthService
        from fastapi import HTTPException
        service = AuthService(mock_repo)
        dto = RegisterRequest(
            full_name="Test", email="dup@example.com",
            password="Abc12345"
        )
        with pytest.raises(HTTPException) as exc:
            await service.register(dto)
        assert exc.value.status_code == 400

    @pytest.mark.asyncio
    async def test_login_success(self):
        """TC-US-002P: Login successfully returns tokens"""
        mock_repo = AsyncMock()
        uid = uuid4()
        mock_repo.get_by_email.return_value = User(
            id=uid, full_name="Test", email="t@example.com",
            password="$2b$12$mockhashcorrect", role="USER", status="ACTIVE"
        )
        from app.schemas.auth import LoginRequest
        from app.services.auth_service import AuthService
        service = AuthService(mock_repo)
        dto = LoginRequest(email="t@example.com", password="Abc12345")
        with patch("app.services.auth_service.verify_password", return_value=True):
            with patch("app.services.auth_service.create_access_token", return_value="access_token"):
                with patch("app.services.auth_service.create_refresh_token", return_value="refresh_token"):
                    result = await service.login(dto)
        assert result["access_token"] == "access_token"
        assert result["refresh_token"] == "refresh_token"
        assert result["token_type"] == "bearer"

    @pytest.mark.asyncio
    async def test_login_wrong_password(self):
        """TC-US-002N: Login with wrong password -> 401"""
        mock_repo = AsyncMock()
        mock_repo.get_by_email.return_value = User(
            id=uuid4(), full_name="Test", email="t@example.com",
            password="$2b$12$mockhashcorrect", role="USER", status="ACTIVE"
        )
        from app.schemas.auth import LoginRequest
        from app.services.auth_service import AuthService
        from fastapi import HTTPException
        service = AuthService(mock_repo)
        dto = LoginRequest(email="t@example.com", password="Wrong123")
        with patch("app.services.auth_service.verify_password", return_value=False):
            with pytest.raises(HTTPException) as exc:
                await service.login(dto)
        assert exc.value.status_code == 401

    @pytest.mark.asyncio
    async def test_login_nonexistent_email(self):
        """TC-US-002N4: Login with non-existent email -> 401 (no leak)"""
        mock_repo = AsyncMock()
        mock_repo.get_by_email.return_value = None
        from app.schemas.auth import LoginRequest
        from app.services.auth_service import AuthService
        from fastapi import HTTPException
        service = AuthService(mock_repo)
        dto = LoginRequest(email="ghost@example.com", password="Abc12345")
        with pytest.raises(HTTPException) as exc:
            await service.login(dto)
        assert exc.value.status_code == 401
        # Must not reveal that email doesn't exist
        assert "không tồn tại" not in str(exc.value.detail).lower()

    @pytest.mark.asyncio
    async def test_get_profile(self):
        """TC-US-006P: Get profile"""
        uid = uuid4()
        mock_repo = AsyncMock()
        mock_repo.get_by_id.return_value = User(id=uid, full_name="Test", email="t@example.com")
        from app.services.auth_service import AuthService
        service = AuthService(mock_repo)
        result = await service.get_profile(uid)
        assert result.id == uid

    @pytest.mark.asyncio
    async def test_get_profile_not_found(self):
        """TC-US-006N: Profile not found -> 404"""
        mock_repo = AsyncMock()
        mock_repo.get_by_id.return_value = None
        from app.services.auth_service import AuthService
        from fastapi import HTTPException
        service = AuthService(mock_repo)
        with pytest.raises(HTTPException) as exc:
            await service.get_profile(uuid4())
        assert exc.value.status_code == 404

    @pytest.mark.asyncio
    async def test_logout(self):
        """TC-US-003P: Logout"""
        mock_repo = AsyncMock()
        from app.services.auth_service import AuthService
        service = AuthService(mock_repo)
        result = await service.logout(uuid4())
        assert result["message"]

    @pytest.mark.asyncio
    async def test_refresh_token_success(self):
        """TC-US-004P: Refresh token"""
        uid = uuid4()
        mock_repo = AsyncMock()
        mock_repo.get_by_id.return_value = User(id=uid, role="USER")
        from app.services.auth_service import AuthService
        service = AuthService(mock_repo)
        with patch("app.services.auth_service.decode_token", return_value={"sub": str(uid), "type": "refresh"}):
            with patch("app.services.auth_service.create_access_token", return_value="new_access"):
                with patch("app.services.auth_service.create_refresh_token", return_value="new_refresh"):
                    result = await service.refresh_token("valid_token")
        assert result["access_token"] == "new_access"
        assert result["refresh_token"] == "new_refresh"

    @pytest.mark.asyncio
    async def test_refresh_token_invalid(self):
        """TC-US-004N: Invalid refresh token -> 401"""
        mock_repo = AsyncMock()
        from app.services.auth_service import AuthService
        from fastapi import HTTPException
        service = AuthService(mock_repo)
        with patch("app.services.auth_service.decode_token", return_value=None):
            with pytest.raises(HTTPException) as exc:
                await service.refresh_token("bad_token")
        assert exc.value.status_code == 401

    @pytest.mark.asyncio
    async def test_forgot_password(self):
        """TC-US-007P: Forgot password"""
        mock_repo = AsyncMock()
        mock_repo.get_by_email.return_value = User(id=uuid4(), email="t@example.com")
        from app.services.auth_service import AuthService
        service = AuthService(mock_repo)
        result = await service.forgot_password("t@example.com")
        assert "sent" in result["message"].lower()

    @pytest.mark.asyncio
    async def test_forgot_password_nonexistent(self):
        """TC-US-007N: Email not found (should not reveal)"""
        mock_repo = AsyncMock()
        mock_repo.get_by_email.return_value = None
        from app.services.auth_service import AuthService
        service = AuthService(mock_repo)
        result = await service.forgot_password("ghost@example.com")
        assert "sent" in result["message"].lower()

    @pytest.mark.asyncio
    async def test_reset_password_success(self):
        """TC-US-007P5: Reset password with valid token"""
        uid = uuid4()
        mock_repo = AsyncMock()
        from app.services.auth_service import AuthService
        service = AuthService(mock_repo)
        with patch("app.services.auth_service.decode_token", return_value={"sub": str(uid)}):
            with patch("app.services.auth_service.hash_password", return_value="new_hash"):
                result = await service.reset_password("valid_token", "NewPass123")
        assert "updated" in result["message"].lower()

    @pytest.mark.asyncio
    async def test_reset_password_invalid_token(self):
        """TC-US-007N: Invalid reset token -> 400"""
        mock_repo = AsyncMock()
        from app.services.auth_service import AuthService
        from fastapi import HTTPException
        service = AuthService(mock_repo)
        with patch("app.services.auth_service.decode_token", return_value=None):
            with pytest.raises(HTTPException) as exc:
                await service.reset_password("bad_token", "NewPass123")
        assert exc.value.status_code == 400

    @pytest.mark.asyncio
    async def test_update_profile(self):
        """TC-US-006P2: Update profile"""
        uid = uuid4()
        mock_repo = AsyncMock()
        mock_repo.update.return_value = User(id=uid, full_name="Updated", email="t@example.com")
        from app.services.auth_service import AuthService
        from app.schemas.auth import ProfileUpdateRequest
        service = AuthService(mock_repo)
        dto = ProfileUpdateRequest(full_name="Updated")
        result = await service.update_profile(uid, dto)
        assert result.full_name == "Updated"


# ============================================================
# Admin Service Tests (FR-ADM-01, 02, 03, 05)
# ============================================================

class TestAdminService:
    """Admin service tests"""

    @pytest.mark.asyncio
    async def test_list_users_valid(self):
        """TC-ADM-001P: List users with pagination"""
        mock_repo = AsyncMock()
        mock_repo.list_users.return_value = []
        from app.services.admin_service import AdminService
        service = AdminService(mock_repo)
        result = await service.list_users(page=1, page_size=20)
        assert result["page"] == 1
        assert result["count"] == 0

    @pytest.mark.asyncio
    async def test_list_users_invalid_page_size(self):
        """TC-ADM-005N: Invalid page_size -> ValidationError"""
        mock_repo = AsyncMock()
        from app.services.admin_service import AdminService, AdminValidationError
        service = AdminService(mock_repo)
        with pytest.raises(AdminValidationError):
            await service.list_users(page=0, page_size=20)

    @pytest.mark.asyncio
    async def test_activate_user_success(self):
        """TC-ADM-001P2: Activate/lock user"""
        uid = uuid4()
        mock_repo = AsyncMock()
        mock_repo.get_user.return_value = MagicMock(id=uid)
        mock_repo.update_user_status.return_value = "BLOCKED"
        from app.services.admin_service import AdminService
        service = AdminService(mock_repo)
        result = await service.activate_user(uid, "BLOCKED")
        assert result == "BLOCKED"

    @pytest.mark.asyncio
    async def test_activate_user_invalid_status(self):
        """TC-ADM-001N: Invalid status -> ValidationError"""
        mock_repo = AsyncMock()
        from app.services.admin_service import AdminService, AdminValidationError
        service = AdminService(mock_repo)
        with pytest.raises(AdminValidationError):
            await service.activate_user(uuid4(), "INVALID_STATUS")

    @pytest.mark.asyncio
    async def test_activate_user_not_found(self):
        """TC-ADM-001N: User not found"""
        mock_repo = AsyncMock()
        mock_repo.get_user.return_value = None
        from app.services.admin_service import AdminService, AdminNotFoundError
        service = AdminService(mock_repo)
        with pytest.raises(AdminNotFoundError):
            await service.activate_user(uuid4(), "BLOCKED")

    @pytest.mark.asyncio
    async def test_suspend_user(self):
        """TC-ADM-001P3: Suspend user"""
        uid = uuid4()
        mock_repo = AsyncMock()
        mock_repo.get_user.return_value = MagicMock(id=uid)
        mock_repo.update_user_status.return_value = "SUSPENDED"
        from app.services.admin_service import AdminService
        service = AdminService(mock_repo)
        result = await service.suspend_user(uid)
        assert result == "SUSPENDED"

    @pytest.mark.asyncio
    async def test_get_audit_log(self):
        """TC-ADM-003P: Get audit log"""
        mock_repo = AsyncMock()
        mock_repo.list_audit_logs.return_value = []
        from app.services.admin_service import AdminService
        service = AdminService(mock_repo)
        result = await service.get_audit_log()
        assert "items" in result

    @pytest.mark.asyncio
    async def test_moderate_post(self):
        """TC-ADM-002P: Moderate post -> REMOVED"""
        content_id = uuid4()
        mock_repo = AsyncMock()
        mock_repo.moderate_post.return_value = "REMOVED"
        from app.services.admin_service import AdminService
        service = AdminService(mock_repo)
        result = await service.moderate_content("post", content_id, "REMOVED")
        assert result == "REMOVED"

    @pytest.mark.asyncio
    async def test_moderate_invalid_type(self):
        """TC-ADM-002N: Invalid content type"""
        mock_repo = AsyncMock()
        from app.services.admin_service import AdminService, AdminValidationError
        service = AdminService(mock_repo)
        with pytest.raises(AdminValidationError):
            await service.moderate_content("invalid_type", uuid4(), "REMOVED")

    @pytest.mark.asyncio
    async def test_update_config(self):
        """TC-ADM-005P: Update system config"""
        mock_repo = AsyncMock()
        mock_repo.update_config.return_value = []
        from app.services.admin_service import AdminService
        service = AdminService(mock_repo)
        result = await service.update_system_config({"max_upload_size": "20MB"})
        assert isinstance(result, dict)

    @pytest.mark.asyncio
    async def test_update_config_empty(self):
        """TC-ADM-005N: Empty config -> ValidationError"""
        mock_repo = AsyncMock()
        from app.services.admin_service import AdminService, AdminValidationError
        service = AdminService(mock_repo)
        with pytest.raises(AdminValidationError):
            await service.update_system_config({})