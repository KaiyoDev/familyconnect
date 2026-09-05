from uuid import UUID
from sqlalchemy.orm import Session
from typing import List, Optional
from backend.app.infrastructure.models.community import Post


class PostRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, post: Post) -> Post:
        self.session.add(post)
        self.session.commit()
        self.session.refresh(post)
        return post

    def get_by_id(self, post_id) -> Optional[Post]:
        return self.session.query(Post).filter(Post.id == post_id).first()

    def get_feed_by_family(self, family_id: UUID, skip: int, limit: int) -> List[Post]:
        return (
            self.session.query(Post)
            .filter(Post.family_id == family_id)
            .order_by(Post.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def update(self, post: Post) -> Post:
        self.session.add(post)
        self.session.commit()
        self.session.refresh(post)
        return post

    def delete(self, post: Post) -> None:
        self.session.delete(post)
        self.session.commit()
