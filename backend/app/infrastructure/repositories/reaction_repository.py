from sqlalchemy.orm import Session
from typing import Optional
from backend.app.infrastructure.models.community import PostReaction


class ReactionRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_or_update_reaction(self, reaction: PostReaction) -> PostReaction:
        """Upsert by (post_id, user_id, reaction_type) to match unique constraint."""
        existing = (
            self.session.query(PostReaction)
            .filter(
                PostReaction.post_id == reaction.post_id,
                PostReaction.user_id == reaction.user_id,
                PostReaction.reaction_type == reaction.reaction_type,
            )
            .first()
        )
        if existing:
            self.session.commit()
            self.session.refresh(existing)
            return existing
        self.session.add(reaction)
        self.session.commit()
        self.session.refresh(reaction)
        return reaction

    def remove_reaction(self, post_id, user_id, reaction_type: str) -> bool:
        reaction = (
            self.session.query(PostReaction)
            .filter(
                PostReaction.post_id == post_id,
                PostReaction.user_id == user_id,
                PostReaction.reaction_type == reaction_type,
            )
            .first()
        )
        if not reaction:
            return False
        self.session.delete(reaction)
        self.session.commit()
        return True

    def get_by_post_id(self, post_id) -> list[PostReaction]:
        return self.session.query(PostReaction).filter(PostReaction.post_id == post_id).all()
