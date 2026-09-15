"""
FamilyConnect - Unit tests for domain utils (password, jwt)
"""
import pytest
from datetime import timedelta
from unittest.mock import patch, MagicMock

from app.domain.utils.password import hash_password, verify_password


class TestPasswordUtils:

    def test_hash_password_success(self):
        """Hash a password should return a bcrypt hash"""
        with patch("app.domain.utils.password.pwd_context.hash", return_value="$2b$12$mockhash"):
            result = hash_password("Abc12345")
        assert result == "$2b$12$mockhash"

    def test_verify_password_success(self):
        """Verify correct password"""
        with patch("app.domain.utils.password.pwd_context.verify", return_value=True):
            result = verify_password("Abc12345", "$2b$12$mockhash")
        assert result is True

    def test_verify_password_failure(self):
        """Verify incorrect password"""
        with patch("app.domain.utils.password.pwd_context.verify", return_value=False):
            result = verify_password("Wrong", "$2b$12$mockhash")
        assert result is False

    def test_hash_password_empty_string(self):
        """Hash empty password"""
        with patch("app.domain.utils.password.pwd_context.hash", return_value="$2b$12$emptyhash"):
            result = hash_password("")
        assert result is not None


class TestJWTUtils:

    @pytest.mark.asyncio
    async def test_create_access_token(self):
        """Create access token"""
        with patch("app.domain.utils.jwt.settings") as mock_settings:
            mock_settings.secret_key = "test-secret"
            mock_settings.jwt_algorithm = "HS256"
            mock_settings.access_token_expire_minutes = 30
            with patch("app.domain.utils.jwt.jwt.encode", return_value="access_token_value"):
                from app.domain.utils.jwt import create_access_token
                result = create_access_token("user-123", "USER")
        assert result == "access_token_value"

    @pytest.mark.asyncio
    async def test_create_refresh_token(self):
        """Create refresh token"""
        with patch("app.domain.utils.jwt.settings") as mock_settings:
            mock_settings.secret_key = "test-secret"
            mock_settings.jwt_algorithm = "HS256"
            mock_settings.refresh_token_expire_days = 7
            with patch("app.domain.utils.jwt.jwt.encode", return_value="refresh_token_value"):
                from app.domain.utils.jwt import create_refresh_token
                result = create_refresh_token("user-123")
        assert result == "refresh_token_value"

    @pytest.mark.asyncio
    async def test_decode_token_success(self):
        """Decode token successfully"""
        with patch("app.domain.utils.jwt.settings") as mock_settings:
            mock_settings.secret_key = "test-secret"
            mock_settings.jwt_algorithm = "HS256"
            with patch("app.domain.utils.jwt.jwt.decode", return_value={"sub": "user-123", "role": "USER"}):
                from app.domain.utils.jwt import decode_token
                result = decode_token("valid.token.here")
        assert result is not None
        assert result["sub"] == "user-123"

    @pytest.mark.asyncio
    async def test_decode_token_invalid(self):
        """Decode invalid token"""
        with patch("app.domain.utils.jwt.settings") as mock_settings:
            mock_settings.secret_key = "test-secret"
            mock_settings.jwt_algorithm = "HS256"
            from jose import JWTError
            with patch("app.domain.utils.jwt.jwt.decode", side_effect=JWTError("Invalid token")):
                from app.domain.utils.jwt import decode_token
                result = decode_token("invalid.token")
        assert result is None