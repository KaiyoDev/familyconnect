"""AI domain models: AIConversation, AIMessage."""
from uuid import UUID
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.databases.base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class AIConversation(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """AI conversation entity — stores a chat session between a user and the AI."""

    __tablename__ = "ai_conversations"

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    title: Mapped[str | None] = mapped_column(String(200), nullable=True)

    # Relationships
    messages = relationship(
        "AIMessage", back_populates="conversation", cascade="all, delete-orphan", order_by="AIMessage.created_at"
    )

    def __repr__(self) -> str:
        return f"<AIConversation(id={self.id}, title={self.title!r})>"


class AIMessage(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """AI message entity — one turn in an AI conversation."""

    __tablename__ = "ai_messages"

    conversation_id: Mapped[UUID] = mapped_column(
        ForeignKey("ai_conversations.id", ondelete="CASCADE"), nullable=False, index=True
    )
    role: Mapped[str] = mapped_column(String(50), nullable=False)  # "user" | "assistant"
    content: Mapped[str] = mapped_column(Text, nullable=False)

    # Relationships
    conversation = relationship("AIConversation", back_populates="messages")

    def __repr__(self) -> str:
        return f"<AIMessage(id={self.id}, role={self.role!r}, conversation={self.conversation_id})>"
