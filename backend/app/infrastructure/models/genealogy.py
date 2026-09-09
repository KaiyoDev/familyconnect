"""Family and genealogy models."""
from uuid import UUID
from sqlalchemy import String, Text, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.databases.base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class Family(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Family (dòng họ) entity."""

    __tablename__ = "families"

    family_name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_by: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"), nullable=False
    )
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="ACTIVE")

    # Relationships — foreign_keys omitted; set up deferred after all classes defined
    creator = relationship("User", back_populates="families_created")
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

    # Relationships — foreign_keys omitted; set up deferred
    family = relationship("Family", back_populates="branches")
    founder = relationship("FamilyMember", back_populates="founded_branches")
    members = relationship("FamilyMember", back_populates="branch")
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
    date_of_birth: Mapped[str | None] = mapped_column("date_of_birth", nullable=True)
    is_alive: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    date_of_death: Mapped[str | None] = mapped_column("date_of_death", nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="PENDING")

    # Relationships — foreign_keys omitted; set up deferred
    family = relationship("Family", back_populates="members")
    branch = relationship("FamilyBranch", back_populates="members")
    user = relationship("User", back_populates="members_linked")
    founded_branches = relationship("FamilyBranch", back_populates="founder")
    employment_profiles = relationship(
        "EmploymentProfile", back_populates="member", cascade="all, delete-orphan"
    )
    education_profiles = relationship(
        "EducationProfile", back_populates="member", cascade="all, delete-orphan"
    )
    relationships_as_from = relationship(
        "Relationship", back_populates="from_member",
    )
    relationships_as_to = relationship(
        "Relationship", back_populates="to_member",
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

    # Relationships
    from_member = relationship(
        "FamilyMember", back_populates="relationships_as_from",
    )
    to_member = relationship(
        "FamilyMember", back_populates="relationships_as_to",
    )

    def __repr__(self) -> str:
        return f"<Relationship(id={self.id}, type={self.type})>"


# ---------------------------------------------------------------------------
# Deferred relationship configuration
# After all classes are defined, re-configure relationships with proper foreign_keys.
# This avoids NameError that occurs when referencing the class inside its own body.
# ---------------------------------------------------------------------------

# Family.creator → User, foreign key is Family.created_by → users.id
# SQLAlchemy auto-detects this since there's only one FK, so we can leave it as-is.

# FamilyBranch.founder → FamilyMember, foreign key is FamilyBranch.founder_id → family_members.id
# Auto-detected since only one FK.

# FamilyBranch.members → FamilyMember, foreign key is FamilyMember.branch_id → family_branches.id
# Must specify foreign_keys because FamilyBranch.founder_id also links to family_members
FamilyBranch.members = relationship(
    "FamilyMember",
    back_populates="branch",
    foreign_keys="[FamilyMember.branch_id]",
)

# FamilyMember.founded_branches → FamilyBranch, foreign key is FamilyBranch.founder_id → family_members.id
FamilyMember.founded_branches = relationship(
    "FamilyBranch",
    back_populates="founder",
    foreign_keys="[FamilyBranch.founder_id]",
)

Relationship.from_member = relationship(
    "FamilyMember",
    back_populates="relationships_as_from",
    foreign_keys="[Relationship.from_member_id]",
)

Relationship.to_member = relationship(
    "FamilyMember",
    back_populates="relationships_as_to",
    foreign_keys="[Relationship.to_member_id]",
)

# FamilyBranch.founder → FamilyMember, foreign key is FamilyBranch.founder_id → family_members.id
# Must specify foreign_keys because FamilyMember.branch_id also links to family_branches
FamilyBranch.founder = relationship(
    "FamilyMember",
    back_populates="founded_branches",
    foreign_keys="[FamilyBranch.founder_id]",
)
