"""Heritage and media models."""
from uuid import UUID
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.databases.base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class HeritageItem(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Heritage item: documents, stories, outstanding members, etc."""

    __tablename__ = "heritage_items"

    family_id: Mapped[UUID] = mapped_column(
        ForeignKey("families.id", ondelete="CASCADE"), nullable=False, index=True
    )
    branch_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("family_branches.id", ondelete="SET NULL"), nullable=True
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    type: Mapped[str] = mapped_column(String(30), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    period: Mapped[str | None] = mapped_column(String(100), nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="DRAFT")
    media_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

    # Relationships
    family = relationship("Family", back_populates="heritage_items")
    branch = relationship("FamilyBranch", back_populates="heritage_items")

    def __repr__(self) -> str:
        return f"<HeritageItem(id={self.id}, title={self.title})>"


class MediaAsset(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Media asset: photos, videos, documents stored as URL references to S3."""

    __tablename__ = "media_assets"

    event_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("events.id", ondelete="CASCADE"), nullable=True, index=True
    )
    family_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("families.id", ondelete="CASCADE"), nullable=True, index=True
    )
    uploaded_by: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    caption: Mapped[str | None] = mapped_column(String(255), nullable=True)
    url: Mapped[str] = mapped_column(String(500), nullable=False)
    media_type: Mapped[str] = mapped_column(String(20), nullable=False)

    # Relationships
    event_owner = relationship(
        "Event", back_populates="media_assets", foreign_keys=[event_id]
    )
    family_owner = relationship(
        "Family", back_populates="media_assets", foreign_keys=[family_id]
    )
    uploader = relationship("User", back_populates="media_uploads")

    __table_args__ = (
        # At least one of event_id or family_id must be non-null
        # Enforced at application level; DB CHECK would need generated column
    )

    def __repr__(self) -> str:
        return f"<MediaAsset(id={self.id}, type={self.media_type})>"
