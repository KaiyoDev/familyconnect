from sqlalchemy import Column, String, DateTime
from app.infrastructure.databases.base import Base


class AppPostReaction(Base):
    __tablename__ = 'post_reactions'

    id = Column(String(36), primary_key=True)
    post_id = Column(String(36), nullable=False)
    user_id = Column(String(36), nullable=False)
    reaction_type = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
