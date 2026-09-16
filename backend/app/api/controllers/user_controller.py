"""Root-level user endpoints — align with frontend `userApi` calls (/users/me)."""
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.databases.database import get_db
from app.infrastructure.repositories.user_repository import UserRepository
from app.schemas.auth import ProfileUpdateRequest, UserResponse
from app.services.auth_service import AuthService
from app.api.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["User"])


def _current_user_id(current_user: dict) -> UUID:
    uid = current_user.get("id") or current_user.get("sub")
    if not uid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not resolve current user")
    return UUID(str(uid))


def get_auth_service(db: AsyncSession = Depends(get_db)) -> AuthService:
    return AuthService(UserRepository(db))


@router.get("/me", response_model=UserResponse)
async def get_me(
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Return the authenticated user's profile."""
    user_id = _current_user_id(current_user)
    user = await UserRepository(db).get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.put("/me", response_model=UserResponse)
async def update_me(
    payload: ProfileUpdateRequest,
    current_user: dict = Depends(get_current_user),
    svc: AuthService = Depends(get_auth_service),
):
    """Update the authenticated user's profile."""
    user_id = _current_user_id(current_user)
    updated = await svc.update_profile(user_id, payload)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return updated
