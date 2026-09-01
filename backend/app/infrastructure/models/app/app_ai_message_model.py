from sqlalchemy import Column, String, Text, DateTime
from app.infrastructure.databases.base import Base


class AppAIMessage(Base):
    __tablename__ = 'ai_messages'

    id = Column(String(36), primary_key=True)
    conversation_id = Column(String(36), nullable=False)
    role = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
