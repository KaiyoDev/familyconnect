from sqlalchemy import Column, String, DateTime
from app.infrastructure.databases.base import Base


class AppComment(Base):
    __tablename__ = 'comments'

    id = Column(String(36), primary_key=True)
    post_id = Column(String(36), nullable=False)
    author_id = Column(String(36), nullable=False)
    content = Column(String(1000), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
