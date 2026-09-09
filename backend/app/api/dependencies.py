fix/FT8-40-auth-service
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.jwt_algorithm])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return {"user_id": user_id, "email": payload.get("email")}
"""FastAPI dependencies for dependency injection."""
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.databases.database import get_db


# ---------------------------------------------------------------------------
# Database session dependency (re-exported for convenience)
# ---------------------------------------------------------------------------

__all__ = ["get_db", "get_current_user"]


# ---------------------------------------------------------------------------
# Current user stub — to be replaced by real JWT auth (FR-US-02)
#
# While auth is not yet implemented, this stub accepts an optional
# Authorization header and returns a deterministic demo user.
# Real implementation will verify JWT and extract user_id / role.
# ---------------------------------------------------------------------------

async def get_current_user(
    authorization: str | None = None,
    db: AsyncSession = Depends(get_db),
) -> dict:
    """Return a mock current user for development.

    TODO: FT8-40 — Replace with real JWT verification once auth service is ready.
    """
    # TODO: Implement JWT decode + DB lookup here (FR-US-02)
    return {
        "id": "00000000-0000-0000-0000-000000000001",
        "email": "demo@familyconnect.vn",
        "full_name": "Demo User",
        "role": "USER",
    }
develop
