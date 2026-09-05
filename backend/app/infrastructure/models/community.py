from datetime import datetime
from sqlalchemy import ForeignKey, JSON, Text, String, UUID, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column
import uuid

from app.infrastructure.databases.base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class Post(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "posts"

    family_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    author_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    media_urls: Mapped[dict | None] = mapped_column(JSON, nullable=True)


class Comment(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "comments"

    post_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("posts.id"), nullable=False)
    author_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    parent_comment_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("comments.id"), nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)


class PostReaction(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "post_reactions"

    post_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("posts.id"), nullable=False)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    reaction_type: Mapped[str] = mapped_column(String(20), nullable=False)

    __table_args__ = (
        UniqueConstraint("post_id", "user_id", "reaction_type", name="uq_post_user_reaction"),
    )
