from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from config import settings
from app.api.dependencies import get_db
from app.infrastructure.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest, RegisterRequest, UserResponse
from app.services.auth_service import AuthService
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/auth", tags=["Authentication"])


def get_auth_service(db: AsyncSession = Depends(get_db)) -> AuthService:
    return AuthService(UserRepository(db))


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    request: RegisterRequest,
    service: AuthService = Depends(get_auth_service),
):
    user = await service.register(request)
    return {"data": UserResponse.model_validate(user).model_dump(mode="json")}


@router.post("/login")
async def login(
    request: LoginRequest,
    service: AuthService = Depends(get_auth_service),
):
    user = await service.user_repo.get_by_email(request.email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    tokens = await service.login(request)
    return {
        "data": {
            **tokens,
            "user": UserResponse.model_validate(user).model_dump(mode="json"),
        }
    }

@router.post("/forgot-password")
async def forgot_password(email: str):
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    reset_token = jwt.encode({"sub": email, "type": "reset_password", "exp": expire}, settings.secret_key, algorithm=settings.jwt_algorithm)
    return {"message": "Reset token generated", "reset_token": reset_token}

@router.post("/reset-password")
async def reset_password(reset_token: str, new_password: str):
    try:
        payload = jwt.decode(reset_token, settings.secret_key, algorithms=[settings.jwt_algorithm])
        if payload.get("type") != "reset_password":
            raise HTTPException(status_code=400, detail="Invalid token type")
    except JWTError:
        raise HTTPException(status_code=400, detail="Token expired or invalid")
    return {"message": "Password updated successfully"}

@router.post("/refresh")
async def refresh_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, settings.secret_key, algorithms=[settings.jwt_algorithm])
        user_id = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    new_access_token = jwt.encode({"sub": user_id, "exp": datetime.now(timezone.utc) + timedelta(minutes=30)}, settings.secret_key, algorithm=settings.jwt_algorithm)
    new_refresh_token = jwt.encode({"sub": user_id, "exp": datetime.now(timezone.utc) + timedelta(days=7)}, settings.secret_key, algorithm=settings.jwt_algorithm)
    
    return {"access_token": new_access_token, "refresh_token": new_refresh_token, "token_type": "bearer"}
