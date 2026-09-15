"""FastAPI dependencies for dependency injection and access control."""
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

from config import settings
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.databases.database import get_db
from app.infrastructure.repositories.branch_repository import BranchRepository
from app.infrastructure.repositories.family_repository import FamilyRepository
from app.infrastructure.repositories.member_repository import MemberRepository
from app.infrastructure.repositories.relationship_repository import RelationshipRepository
from app.infrastructure.repositories.sqlalchemy_unit_of_work import SQLAlchemyUnitOfWork
from app.services.family_service import FamilyService

bearer_scheme = HTTPBearer(auto_error=False)


async def get_current_user(
	request: Request,
	credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
) -> dict:
	"""Decode the access token and expose its claims to controllers."""
	if credentials is None:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")

	try:
		user = jwt.decode(credentials.credentials, settings.secret_key, algorithms=["HS256"])
		if "id" not in user and "sub" in user:
			user["id"] = user["sub"]
		if "id" not in user or "role" not in user:
			raise JWTError
	except JWTError as exc:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token") from exc

	request.state.current_user = user
	return user


async def require_admin(current_user: dict = Depends(get_current_user)) -> dict:
	"""Allow only administrators to access administration endpoints."""
	if str(current_user.get("role", "")).upper() not in {"ADMIN", "SUPER_ADMIN"}:
		raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Administrator role required")
	return current_user


async def require_family_access(family_id: str, _current_user: dict = Depends(get_current_user)) -> str:
	"""Temporary authorization seam — validates family id."""
	return family_id


def get_family_service(db: AsyncSession = Depends(get_db)) -> FamilyService:
	return FamilyService(
		db,
		family_repository=FamilyRepository(db),
		member_repository=MemberRepository(db),
		relationship_repository=RelationshipRepository(db),
		branch_repository=BranchRepository(db),
		unit_of_work=SQLAlchemyUnitOfWork(db),
	)


__all__ = ["get_db", "get_current_user", "require_admin", "require_family_access", "get_family_service"]
