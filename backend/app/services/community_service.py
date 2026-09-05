from uuid import UUID
from typing import List, Optional
from sqlalchemy.orm import Session
from backend.app.infrastructure.models.community import Post, Comment, PostReaction
from backend.app.infrastructure.repositories.post_repository import PostRepository
from backend.app.infrastructure.repositories.comment_repository import CommentRepository
from backend.app.infrastructure.repositories.reaction_repository import ReactionRepository


class CommunityService:
    def __init__(self, db: Session):
        self.db = db
        self.post_repo = PostRepository(db)
        self.comment_repo = CommentRepository(db)
        self.reaction_repo = ReactionRepository(db)

    def create_post(self, family_id: UUID, author_id: UUID, content: str, media_urls: list | None) -> Post:
        post = Post(
            family_id=family_id,
            author_id=author_id,
            content=content,
            media_urls=media_urls,
        )
        return self.post_repo.create(post)

    def get_feed(self, family_id: UUID, skip: int, limit: int) -> List[Post]:
        return self.post_repo.get_feed_by_family(family_id, skip, limit)

    def get_post(self, post_id: UUID) -> Optional[Post]:
        return self.post_repo.get_by_id(post_id)

    def get_comments(self, post_id: UUID) -> List[Comment]:
        return self.comment_repo.get_by_post_id(post_id)

    def update_post(self, post_id: UUID, user_id: UUID, content: str, media_urls: list | None) -> Post:
        post = self.post_repo.get_by_id(post_id)
        if not post:
            raise ValueError("Post not found")
        if post.author_id != user_id:
            raise ValueError("Not authorized to update this post")
        post.content = content
        post.media_urls = media_urls
        return self.post_repo.update(post)

    def delete_post(self, post_id: UUID, user_id: UUID) -> None:
        post = self.post_repo.get_by_id(post_id)
        if not post:
            raise ValueError("Post not found")
        if post.author_id != user_id:
            raise ValueError("Not authorized to delete this post")
        self.post_repo.delete(post)

    def add_comment(self, post_id: UUID, user_id: UUID, content: str) -> Comment:
        comment = Comment(
            post_id=post_id,
            author_id=user_id,
            content=content,
        )
        return self.comment_repo.create(comment)

    def add_reaction(self, post_id: UUID, user_id: UUID, reaction_type: str) -> PostReaction:
        reaction = PostReaction(
            post_id=post_id,
            user_id=user_id,
            reaction_type=reaction_type,
        )
        return self.reaction_repo.add_or_update_reaction(reaction)

    def remove_reaction(self, post_id: UUID, user_id: UUID, reaction_type: str) -> bool:
        return self.reaction_repo.remove_reaction(post_id, user_id, reaction_type)

    def create_announcement(self, family_id: UUID, author_id: UUID, title: str, body: str) -> dict:
        return {
            "family_id": family_id,
            "author_id": author_id,
            "title": title,
            "body": body,
        }
