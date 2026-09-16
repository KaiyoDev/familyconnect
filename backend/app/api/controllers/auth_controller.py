from fastapi import APIRouter, HTTPException, status
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from config import settings

router = APIRouter(prefix="/auth", tags=["Authentication"])


def get_auth_service(db: AsyncSession = Depends(get_db)) -> AuthService:
    return AuthService(UserRepository(db))


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(payload: RegisterRequest, svc: AuthService = Depends(get_auth_service)):
    """Register a new user account."""
    try:
        user = await svc.register(payload)
        return {"message": "User registered successfully", "user_id": str(user.id)}
    except HTTPException as exc:
        raise exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Registration failed: {exc}")


@router.post("/login", response_model=TokenResponse)
async def login(payload: LoginRequest, svc: AuthService = Depends(get_auth_service)):
    """Login with email and password, return JWT tokens."""
    try:
        result = await svc.login(payload)
        return result
    except HTTPException as exc:
        raise exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Login failed: {exc}")


@router.post("/logout")
async def logout(current_user: dict = Depends(get_current_user)):
    """Logout endpoint (stateless — client deletes tokens)."""
    return {"message": "Successfully logged out"}


@router.get("/profile", response_model=UserResponse)
async def get_profile(current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    """Get current user profile."""
    from uuid import UUID
    user_id = UUID(current_user.get("id") or current_user.get("sub"))
    user_repo = UserRepository(db)
    user = await user_repo.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/refresh", response_model=TokenResponse)
async def refresh(payload: RefreshTokenRequest, svc: AuthService = Depends(get_auth_service)):
    """Refresh access token using refresh token."""
    try:
        return await svc.refresh_token(payload.refresh_token)
    except HTTPException as exc:
        raise exc



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
async def forgot_password(email: str, svc: AuthService = Depends(get_auth_service)):
    """Generate password reset token (stub — no email sending)."""
    result = await svc.forgot_password(email)
    return result


@router.post("/reset-password")
async def reset_password(reset_token: str, new_password: str, svc: AuthService = Depends(get_auth_service)):
    """Reset password using token."""
    try:
        return await svc.reset_password(reset_token, new_password)
    except HTTPException as exc:
        raise exc


@router.post("/verify-email")
async def verify_email(payload: VerifyEmailRequest, svc: AuthService = Depends(get_auth_service)):
    """Activate the account referenced by an activation token."""
    return await svc.verify_email(payload.token)


@router.put("/me", response_model=UserResponse)
async def update_profile(
    payload: ProfileUpdateRequest,
    current_user: dict = Depends(get_current_user),
    svc: AuthService = Depends(get_auth_service),
):
    """Update current user profile."""
    from uuid import UUID
    user_id = UUID(current_user.get("id") or current_user.get("sub"))
    return await svc.update_profile(user_id, payload)


# Alias route: PUT /users/me — required by frontend
@router.put("/users/me", response_model=UserResponse)
async def update_user_profile(
    payload: ProfileUpdateRequest,
    current_user: dict = Depends(get_current_user),
    svc: AuthService = Depends(get_auth_service),
):
    """Update current user profile (alias for /auth/me)."""
    from uuid import UUID
    user_id = UUID(current_user.get("id") or current_user.get("sub"))
    return await svc.update_profile(user_id, payload)
