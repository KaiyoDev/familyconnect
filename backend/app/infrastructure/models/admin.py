"""Models used by the administration features."""
from uuid import UUID

from sqlalchemy import JSON, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.databases.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class AuditLog(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Immutable record of an administrative or security-sensitive action."""

    __tablename__ = "audit_logs"

    actor_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True
    )
    action: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    resource_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    resource_id: Mapped[UUID | None] = mapped_column(nullable=True, index=True)
    details: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    actor = relationship("User", back_populates="audit_logs")


class Notification(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Notification delivered to a user after an account action."""

    __tablename__ = "notifications"

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    notification_type: Mapped[str] = mapped_column(String(50), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    is_read: Mapped[bool] = mapped_column(default=False, nullable=False)
    data: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    user = relationship("User", back_populates="notifications")


class SystemConfig(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Key/value storage for administrator-managed system settings."""

    __tablename__ = "system_configs"

    key: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    value: Mapped[dict | list | str | int | float | bool | None] = mapped_column(JSON, nullable=True)
