from abc import ABC, abstractmethod
from uuid import UUID


class IFamilyService(ABC):
    @abstractmethod
    async def create(self, request, creator_id: UUID):
        raise NotImplementedError

    @abstractmethod
    async def update(self, family_id: UUID, request):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, family_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def get_tree(self, family_id: UUID):
        raise NotImplementedError