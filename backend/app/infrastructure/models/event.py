"""Event models: Event, EventRSVP."""
from uuid import UUID
from datetime import datetime
from sqlalchemy import String, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.databases.base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class Event(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Family event entity (giỗ chạp, họp mặt, etc.)."""

    __tablename__ = "events"

    family_id: Mapped[UUID] = mapped_column(
        ForeignKey("families.id", ondelete="CASCADE"), nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)
    start_time: Mapped[datetime] = mapped_column(nullable=False, index=True)
    end_time: Mapped[datetime | None] = mapped_column(nullable=True)
    type: Mapped[str] = mapped_column(String(30), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="OPEN")
    created_by: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"), nullable=False
    )

    # Relationships
    family = relationship("Family", back_populates="events")
    creator = relationship("User", back_populates="events_created")
    rsvps = relationship("EventRSVP", back_populates="event", cascade="all, delete-orphan")
    media_assets = relationship(
        "MediaAsset",
        back_populates="event_owner",
        foreign_keys="[MediaAsset.event_id]",
    )

    __table_args__ = (
        CheckConstraint(
            "end_time IS NULL OR end_time > start_time",
            name="chk_event_end_after_start",
        ),
    )

    def __repr__(self) -> str:
        return f"<Event(id={self.id}, title={self.title})>"


class EventRSVP(UUIDPrimaryKeyMixin, Base):
    """RSVP confirmation for an event — junction between Event and FamilyMember."""

    __tablename__ = "event_rsvps"

    event_id: Mapped[UUID] = mapped_column(
        ForeignKey("events.id", ondelete="CASCADE"), nullable=False, index=True
    )
    member_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("family_members.id", ondelete="SET NULL"), nullable=True
    )
    guest_email: Mapped[str | None] = mapped_column(String(150), nullable=True)
    response: Mapped[str] = mapped_column(String(20), nullable=False)
    responded_at: Mapped[datetime | None] = mapped_column(nullable=True)

    # Relationships
    event = relationship("Event", back_populates="rsvps")
    member = relationship("FamilyMember", back_populates="event_rsvps")

    __table_args__ = (
        CheckConstraint(
            "member_id IS NOT NULL OR guest_email IS NOT NULL",
            name="chk_rsvp_has_member_or_guest",
        ),
        CheckConstraint(
            "NOT (member_id IS NOT NULL AND guest_email IS NOT NULL)",
            name="chk_rsvp_only_one_identifier",
        ),
    )

    def __repr__(self) -> str:
        return f"<EventRSVP(id={self.id}, event={self.event_id})>"
