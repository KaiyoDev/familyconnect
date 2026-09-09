from abc import ABC, abstractmethod
from uuid import UUID
from app.domain.models.dtos import RegisterRequest, LoginRequest, TokenResponse, UserDTO

class IAuthService(ABC):
    @abstractmethod
    async def register(self, request: RegisterRequest) -> UserDTO:
        pass

    @abstractmethod
    async def login(self, request: LoginRequest) -> TokenResponse:
        pass

    @abstractmethod
    async def logout(self, user_id: UUID) -> bool:
        pass

    @abstractmethod
    async def refresh(self, refresh_token: str) -> TokenResponse:
        pass

    @abstractmethod
    async def profile(self, user_id: UUID) -> UserDTO:
        pass