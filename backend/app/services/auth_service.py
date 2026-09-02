from uuid import UUID
from typing import Optional
from fastapi import HTTPException, status
from app.infrastructure.repositories.user_repository import UserRepository
from app.domain.utils.password import hash_password, verify_password
from app.domain.utils.jwt import create_access_token, create_refresh_token, decode_token


class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def register(self, register_data: dict) -> dict:
        if await self.user_repo.exists_by_email(register_data["email"]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )
        register_data["password"] = hash_password(register_data["password"])
        register_data["status"] = "PENDING"
        register_data["role"] = register_data.get("role", "USER")

        user = await self.user_repo.create(register_data)
        return {"message": "User registered successfully", "user_id": str(user.id)}

    async def login(self, login_data: dict) -> dict:
        user = await self.user_repo.get_by_email(login_data["email"])
        if not user or not verify_password(login_data["password"], user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        token_data = {"sub": str(user.id), "role": user.role}
        access_token = create_access_token(token_data)
        refresh_token = create_refresh_token(token_data)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }

    async def logout(self, user_id: UUID) -> dict:
        return {"message": "Successfully logged out"}

    async def refresh_token(self, refresh_token_str: str) -> dict:
        payload = decode_token(refresh_token_str)
        if not payload or payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token",
            )
        user_id = payload.get("sub")
        role = payload.get("role")
        new_access_token = create_access_token({"sub": user_id, "role": role})
        return {"access_token": new_access_token, "token_type": "bearer"}

    async def get_profile(self, user_id: UUID) -> dict:
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
        return {
            "id": str(user.id),
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role,
            "status": user.status,
        }

    async def update_profile(self, user_id: UUID, update_data: dict) -> dict:
        update_data.pop("password", None)
        user = await self.user_repo.update(user_id, update_data)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
        return {"message": "Profile updated successfully"}

    async def forgot_password(self, email: str) -> dict:
        user = await self.user_repo.get_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Email not found"
            )
        return {"message": "Password reset token sent to email"}

    async def reset_password(self, reset_data: dict) -> dict:
        user = await self.user_repo.get_by_email(reset_data["email"])
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
        new_hashed_pwd = hash_password(reset_data["new_password"])
        await self.user_repo.update(user.id, {"password": new_hashed_pwd})
        return {"message": "Password updated successfully"}