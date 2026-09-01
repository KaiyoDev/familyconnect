"""User authentication and profile model."""
from uuid import UUID
from sqlalchemy import String, Text, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.databases.base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class User(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """User account model — stores login credentials and system role."""

    __tablename__ = "users"

    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False, index=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    role: Mapped[str] = mapped_column(String(20), nullable=False, default="USER")
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="PENDING")

    # Relationships
    families_created = relationship(
        "Family", back_populates="creator", foreign_keys="[Family.created_by]"
    )
    members_linked = relationship(
        "FamilyMember", back_populates="user", uselist=False
    )
    events_created = relationship(
        "Event", back_populates="creator", foreign_keys="[Event.created_by]"
    )
    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="author")
    notifications = relationship("Notification", back_populates="user")
    audit_logs = relationship("AuditLog", back_populates="actor")
    ai_conversations = relationship("AIConversation", back_populates="user")
    media_uploads = relationship("MediaAsset", back_populates="uploader")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email})>"
