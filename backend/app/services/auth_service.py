from fastapi import HTTPException, status
from uuid import UUID
from app.infrastructure.repositories.user_repository import UserRepository
from app.domain.utils.password import hash_password, verify_password
from app.domain.utils.jwt import create_access_token, create_refresh_token, decode_token
from app.schemas.auth import RegisterRequest, LoginRequest, ProfileUpdateRequest

class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def register(self, dto: RegisterRequest):
        if await self.user_repo.exists_by_email(dto.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        
        user_data = {
            "full_name": dto.full_name,
            "email": dto.email,
            "password": hash_password(dto.password),
            "phone": dto.phone,
            "role": "USER",
            "status": "PENDING"
        }
        return await self.user_repo.create(user_data)

    async def login(self, dto: LoginRequest):
        user = await self.user_repo.get_by_email(dto.email)
        if not user or not verify_password(dto.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        access_token = create_access_token(str(user.id), user.role)
        refresh_token = create_refresh_token(str(user.id))
        return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

    async def refresh_token(self, refresh_token: str):
        payload = decode_token(refresh_token)
        if not payload or payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid refresh token")
        
        user_id = payload.get("sub")
        user = await self.user_repo.get_by_id(UUID(user_id))
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        access_token = create_access_token(str(user.id), user.role)
        new_refresh_token = create_refresh_token(str(user.id))
        return {"access_token": access_token, "refresh_token": new_refresh_token, "token_type": "bearer"}

    async def get_profile(self, user_id: UUID):
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def update_profile(self, user_id: UUID, dto: ProfileUpdateRequest):
        update_data = {k: v for k, v in dto.model_dump().items() if v is not None}
        return await self.user_repo.update(user_id, update_data)

    async def logout(self, user_id: UUID):
        return {"message": "Successfully logged out"}

    async def forgot_password(self, email: str):
        user = await self.user_repo.get_by_email(email)
        if not user:
            return {"message": "If email exists, reset link has been sent"}
        return {"message": "If email exists, reset link has been sent"}

    async def reset_password(self, reset_token: str, new_password: str):
        payload = decode_token(reset_token)
        if not payload:
            raise HTTPException(status_code=400, detail="Invalid token")
        user_id = payload.get("sub")
        await self.user_repo.update(UUID(user_id), {"password": hash_password(new_password)})
        return {"message": "Password updated successfully"}