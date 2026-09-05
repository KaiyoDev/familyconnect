from sqlalchemy.orm import Session
from typing import List, Optional
from backend.app.infrastructure.models.community import Comment


class CommentRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, comment: Comment) -> Comment:
        self.session.add(comment)
        self.session.commit()
        self.session.refresh(comment)
        return comment

    def get_by_id(self, comment_id) -> Optional[Comment]:
        return self.session.query(Comment).filter(Comment.id == comment_id).first()

    def get_by_post_id(self, post_id) -> List[Comment]:
        return (
            self.session.query(Comment)
            .filter(Comment.post_id == post_id)
            .order_by(Comment.created_at.asc())
            .all()
        )
