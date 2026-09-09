from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from app.domain.models.dtos import CreateFamilyRequest, FamilyDTO, MemberDTO

class IFamilyService(ABC):
    @abstractmethod
    async def create(self, creator_id: UUID, request: CreateFamilyRequest) -> FamilyDTO:
        pass

    @abstractmethod
    async def update(self, family_id: UUID, request: CreateFamilyRequest) -> Optional[FamilyDTO]:
        pass

    @abstractmethod
    async def delete(self, family_id: UUID) -> bool:
        pass

    @abstractmethod
    async def get_tree(self, family_id: UUID) -> List[MemberDTO]:
        pass