from fastapi import APIRouter, Depends, status
from app.services.auth_service import AuthService
from app.api.dependencies import get_auth_service, get_current_user
from app.schemas.auth import (
    RegisterRequest, LoginRequest, RefreshTokenRequest, 
    ForgotPasswordRequest, ResetPasswordRequest, ProfileUpdateRequest,
    TokenResponse, UserResponse
)
from app.infrastructure.models.user import User

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(dto: RegisterRequest, service: AuthService = Depends(get_auth_service)):
    return await service.register(dto)

@router.post("/login", response_model=TokenResponse)
async def login(dto: LoginRequest, service: AuthService = Depends(get_auth_service)):
    return await service.login(dto)

@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(dto: RefreshTokenRequest, service: AuthService = Depends(get_auth_service)):
    return await service.refresh_token(dto.refresh_token)

@router.get("/profile", response_model=UserResponse)
async def get_profile(current_user: User = Depends(get_current_user), service: AuthService = Depends(get_auth_service)):
    return await service.get_profile(current_user.id)

@router.put("/profile", response_model=UserResponse)
async def update_profile(dto: ProfileUpdateRequest, current_user: User = Depends(get_current_user), service: AuthService = Depends(get_auth_service)):
    return await service.update_profile(current_user.id, dto)

@router.post("/logout")
async def logout(current_user: User = Depends(get_current_user), service: AuthService = Depends(get_auth_service)):
    return await service.logout(current_user.id)

@router.post("/forgot-password")
async def forgot_password(dto: ForgotPasswordRequest, service: AuthService = Depends(get_auth_service)):
    return await service.forgot_password(dto.email)

@router.post("/reset-password")
async def reset_password(dto: ResetPasswordRequest, service: AuthService = Depends(get_auth_service)):
    return await service.reset_password(dto.reset_token, dto.new_password)