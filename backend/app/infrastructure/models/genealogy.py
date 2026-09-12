"""Family and genealogy models."""
from datetime import date
from uuid import UUID
from sqlalchemy import Boolean, CheckConstraint, String, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.databases.base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class Family(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Family (dòng họ) entity."""

    __tablename__ = "families"

    family_name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_by: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"), nullable=False
    )
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="ACTIVE")

    # Relationships
    creator = relationship("User", back_populates="families_created", foreign_keys=[created_by])
    branches = relationship("FamilyBranch", back_populates="family", cascade="all, delete-orphan")
    members = relationship("FamilyMember", back_populates="family", cascade="all, delete-orphan")
    events = relationship("Event", back_populates="family", cascade="all, delete-orphan")
    posts = relationship("Post", back_populates="family", cascade="all, delete-orphan")
    heritage_items = relationship("HeritageItem", back_populates="family", cascade="all, delete-orphan")
    media_assets = relationship("MediaAsset", back_populates="family_owner")

    def __repr__(self) -> str:
        return f"<Family(id={self.id}, name={self.family_name})>"


class FamilyBranch(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Family branch (chi/nhánh) entity."""

    __tablename__ = "family_branches"

    family_id: Mapped[UUID] = mapped_column(
        ForeignKey("families.id", ondelete="CASCADE"), nullable=False, index=True
    )
    branch_name: Mapped[str] = mapped_column(String(150), nullable=False)
    founder_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("family_members.id", ondelete="SET NULL"), nullable=True
    )
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Relationships
    family = relationship("Family", back_populates="branches")
    founder = relationship("FamilyMember", back_populates="founded_branches", foreign_keys=[founder_id])
    members = relationship(
        "FamilyMember",
        back_populates="branch",
        foreign_keys="[FamilyMember.branch_id]",
    )
    heritage_items = relationship("HeritageItem", back_populates="branch")

    def __repr__(self) -> str:
        return f"<FamilyBranch(id={self.id}, name={self.branch_name})>"


class FamilyMember(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Family member (thành viên phả hệ) entity."""

    __tablename__ = "family_members"

    family_id: Mapped[UUID] = mapped_column(
        ForeignKey("families.id", ondelete="CASCADE"), nullable=False, index=True
    )
    branch_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("family_branches.id", ondelete="SET NULL"), nullable=True
    )
    user_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True, unique=True
    )
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    gender: Mapped[str] = mapped_column(String(20), nullable=False, default="UNKNOWN")
    date_of_birth: Mapped[date | None] = mapped_column(nullable=True)
    is_alive: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    date_of_death: Mapped[date | None] = mapped_column(nullable=True)
    address: Mapped[str | None] = mapped_column(String(300), nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="PENDING")

    # Relationships — use string annotations to avoid circular imports
    family = relationship("Family", back_populates="members")
    branch = relationship(
        "FamilyBranch",
        back_populates="members",
        foreign_keys="[FamilyMember.branch_id]",
    )
    user = relationship("User", back_populates="members_linked")
    founded_branches = relationship(
        "FamilyBranch", back_populates="founder", foreign_keys="[FamilyBranch.founder_id]"
    )
    employment_profiles = relationship(
        "EmploymentProfile", back_populates="member", cascade="all, delete-orphan"
    )
    education_profiles = relationship(
        "EducationProfile", back_populates="member", cascade="all, delete-orphan"
    )
    relationships_as_from = relationship(
        "Relationship",
        back_populates="from_member",
        foreign_keys="[Relationship.from_member_id]",
    )
    relationships_as_to = relationship(
        "Relationship",
        back_populates="to_member",
        foreign_keys="[Relationship.to_member_id]",
    )
    event_rsvps = relationship("EventRSVP", back_populates="member")

    def __repr__(self) -> str:
        return f"<FamilyMember(id={self.id}, name={self.full_name})>"


class Relationship(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Relationship between two family members (PARENT_CHILD or MARRIAGE)."""

    __tablename__ = "relationships"

    from_member_id: Mapped[UUID] = mapped_column(
        ForeignKey("family_members.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    to_member_id: Mapped[UUID] = mapped_column(
        ForeignKey("family_members.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    type: Mapped[str] = mapped_column(String(30), nullable=False)
    notes: Mapped[str | None] = mapped_column(String(255), nullable=True)

    __table_args__ = (
        CheckConstraint(
            "from_member_id <> to_member_id",
            name="chk_relationship_different",
        ),
        UniqueConstraint(
            "from_member_id",
            "to_member_id",
            "type",
            name="uq_relationship_unique",
        ),
    )

    # Relationships
    from_member = relationship(
        "FamilyMember", back_populates="relationships_as_from", foreign_keys=[from_member_id]
    )
    to_member = relationship(
        "FamilyMember", back_populates="relationships_as_to", foreign_keys=[to_member_id]
    )

    def __repr__(self) -> str:
        return f"<Relationship(id={self.id}, type={self.type})>"
