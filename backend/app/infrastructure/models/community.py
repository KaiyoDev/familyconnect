"""Community models: Post, Comment, PostReaction."""
from uuid import UUID
from sqlalchemy import String, Text, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.infrastructure.databases.base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class Post(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Community post entity."""

    __tablename__ = "posts"

    family_id: Mapped[UUID] = mapped_column(
        ForeignKey("families.id", ondelete="CASCADE"), nullable=False, index=True
    )
    author_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    content: Mapped[str] = mapped_column(Text, nullable=False)
    visibility_scope: Mapped[str] = mapped_column(String(20), nullable=False, default="FAMILY")
    branch_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("family_branches.id", ondelete="SET NULL"), nullable=True
    )
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="PUBLISHED")
    media_urls: Mapped[list | None] = mapped_column(JSONB, nullable=True)

    # Relationships
    family = relationship("Family", back_populates="posts")
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
    reactions = relationship("PostReaction", back_populates="post", cascade="all, delete-orphan")

    __table_args__ = (
        # Index on family_id + created_at for feed queries
        {"sqlite_autoincrement": True},
    )

    def __repr__(self) -> str:
        return f"<Post(id={self.id}, family={self.family_id})>"


class Comment(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Comment on a post."""

    __tablename__ = "comments"

    post_id: Mapped[UUID] = mapped_column(
        ForeignKey("posts.id", ondelete="CASCADE"), nullable=False, index=True
    )
    author_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    content: Mapped[str] = mapped_column(String(1000), nullable=False)

    # Relationships
    post = relationship("Post", back_populates="comments")
    author = relationship("User", back_populates="comments")

    def __repr__(self) -> str:
        return f"<Comment(id={self.id}, post={self.post_id})>"


class PostReaction(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Reaction (like, love, etc.) on a post — N-N junction table."""

    __tablename__ = "post_reactions"

    post_id: Mapped[UUID] = mapped_column(
        ForeignKey("posts.id", ondelete="CASCADE"), nullable=False, index=True
    )
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    reaction_type: Mapped[str] = mapped_column(String(20), nullable=False)

    # Relationships
    post = relationship("Post", back_populates="reactions")
    user = relationship("User", back_populates="posts")  # reuse user relationship

    __table_args__ = (
        UniqueConstraint("post_id", "user_id", "reaction_type", name="uq_post_reaction"),
    )

    def __repr__(self) -> str:
        return f"<PostReaction(id={self.id}, post={self.post_id}, type={self.reaction_type})>"
