"""Authentication and authorization dependencies."""
from uuid import UUID
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.databases.database import get_db
from app.infrastructure.models.user import User
from app.infrastructure.repositories.family_repository import FamilyRepository
from app.infrastructure.repositories.member_repository import MemberRepository

security_scheme = HTTPBearer(auto_error=False)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(security_scheme),
    db: AsyncSession = Depends(get_db),
) -> User | None:
    """Extract the current authenticated user from the token.

    NOTE: This is a temporary implementation until the full JWT auth is integrated.
    When no token is provided, returns None (unauthenticated access is allowed
    but restricted). When a token is present, it's parsed as a simple user ID.
    """
    if not credentials:
        return None

    # Temporary: token is the raw user UUID (will be replaced with JWT decode)
    try:
        user_id = UUID(credentials.credentials)
    except (ValueError, AttributeError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
        )

    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return user


async def require_active_user(
    user: User | None = Depends(get_current_user),
) -> User:
    """Require an authenticated and active user."""
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
        )
    if user.status != "ACTIVE":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is not active",
        )
    return user


async def require_family_membership(
    family_id: UUID,
    user: User = Depends(require_active_user),
    db: AsyncSession = Depends(get_db),
) -> UUID:
    """Verify the user has access to the family.

    Checks:
    1. Family exists
    2. User is the creator of the family OR is linked to a member in the family
    """
    family_repo = FamilyRepository(db)
    family = await family_repo.get_by_id(family_id)
    if not family:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Family not found")

    # User is the creator
    if family.created_by == user.id:
        return family_id

    # User is linked to a member in this family
    member_repo = MemberRepository(db)
    members = await member_repo.get_by_family(family_id)
    for member in members:
        if member.user_id == user.id:
            return family_id

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You don't have access to this family",
    )


__all__ = [
    "get_current_user",
    "require_active_user",
    "require_family_membership",
]