from sqlalchemy import Column, String, DateTime
from app.infrastructure.databases.base import Base


class AppAIConversation(Base):
    __tablename__ = 'ai_conversations'

    id = Column(String(36), primary_key=True)
    user_id = Column(String(36), nullable=False)
    title = Column(String(200), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
