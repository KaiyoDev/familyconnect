from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from backend.app.domain.interfaces.repository_base import BaseRepository
from backend.app.domain.models.dtos import FamilyDTO, MemberDTO

class IFamilyRepository(BaseRepository[FamilyDTO], ABC):
    @abstractmethod
    async def get_by_creator(self, user_id: UUID) -> List[FamilyDTO]:
        pass

    @abstractmethod
    async def get_members(self, family_id: UUID) -> List[MemberDTO]:
        pass