from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from app.infrastructure.databases.base import Base


class AppPost(Base):
    __tablename__ = 'posts'

    id = Column(String(36), primary_key=True)
    family_id = Column(String(36), nullable=False)
    author_id = Column(String(36), nullable=False)
    branch_id = Column(String(36), nullable=True)
    content = Column(Text, nullable=False)
    visibility_scope = Column(String(20), nullable=False, default='FAMILY')
    status = Column(String(20), nullable=False, default='PUBLISHED')
    media_urls = Column(JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
