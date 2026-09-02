from typing import Optional
from pydantic import BaseModel, EmailStr
from fastapi import APIRouter, Depends
from app.api.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["Auth Services"])


class RegisterSchema(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    phone: Optional[str] = None


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class ProfileUpdateSchema(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None


class ForgotPasswordSchema(BaseModel):
    email: EmailStr


class ResetPasswordSchema(BaseModel):
    email: EmailStr
    reset_token: str
    new_password: str


class RefreshTokenSchema(BaseModel):
    refresh_token: str


@router.post("/register", status_code=201)
async def register(payload: RegisterSchema):
    return {"message": "User registered successfully", "status": "PENDING"}


@router.post("/login")
async def login(payload: LoginSchema):
    return {
        "access_token": "token_example",
        "refresh_token": "refresh_example",
        "token_type": "bearer",
    }


@router.post("/logout")
async def logout(current_user: dict = Depends(get_current_user)):
    return {"message": "Logged out successfully"}


@router.get("/profile")
async def get_profile(current_user: dict = Depends(get_current_user)):
    return {"user_id": str(current_user["id"]), "role": current_user["role"]}


@router.put("/profile")
async def update_profile(
    payload: ProfileUpdateSchema, current_user: dict = Depends(get_current_user)
):
    return {"message": "Profile updated"}


@router.post("/refresh")
async def refresh_token(payload: RefreshTokenSchema):
    return {"access_token": "new_access_token", "token_type": "bearer"}


@router.post("/forgot-password")
async def forgot_password(payload: ForgotPasswordSchema):
    return {"message": "Reset link sent"}


@router.post("/reset-password")
async def reset_password(payload: ResetPasswordSchema):
    return {"message": "Password reset successful"}