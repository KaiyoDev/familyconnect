from abc import ABC, abstractmethod
from uuid import UUID


class IAuthService(ABC):
    @abstractmethod
    async def register(self, request):
        raise NotImplementedError

    @abstractmethod
    async def login(self, request):
        raise NotImplementedError

    @abstractmethod
    async def logout(self, user_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    async def refresh(self, refresh_token: str):
        raise NotImplementedError

    @abstractmethod
    async def profile(self, user_id: UUID):
        raise NotImplementedError