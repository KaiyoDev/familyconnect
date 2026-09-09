from abc import ABC, abstractmethod
from uuid import UUID
from app.domain.models.dtos import CreatePostRequest, PostDTO, CommentDTO

class ICommunityService(ABC):
    @abstractmethod
    async def create_post(self, author_id: UUID, request: CreatePostRequest) -> PostDTO:
        pass

    @abstractmethod
    async def comment(self, post_id: UUID, author_id: UUID, content: str) -> CommentDTO:
        pass

    @abstractmethod
    async def react(self, post_id: UUID, user_id: UUID, reaction_type: str) -> bool:
        pass