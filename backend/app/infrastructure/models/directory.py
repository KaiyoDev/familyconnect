"""Directory-related models: EmploymentProfile, EducationProfile."""
from uuid import UUID
from datetime import date, datetime
from sqlalchemy import String, Date, Numeric, SmallInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.databases.base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class EmploymentProfile(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Employment/career profile of a family member (supports multiple entries)."""

    __tablename__ = "employment_profiles"

    member_id: Mapped[UUID] = mapped_column(
        ForeignKey("family_members.id", ondelete="CASCADE"), nullable=False, index=True
    )
    company_name: Mapped[str] = mapped_column(String(200), nullable=False)
    position: Mapped[str | None] = mapped_column(String(100), nullable=True)
    start_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    end_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    is_current: Mapped[bool] = mapped_column(nullable=False, default=False)
    description: Mapped[str | None] = mapped_column(nullable=True)

    # Relationships
    member = relationship("FamilyMember", back_populates="employment_profiles")

    def __repr__(self) -> str:
        return f"<EmploymentProfile(id={self.id}, company={self.company_name})>"


class EducationProfile(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Education profile of a family member (supports multiple entries)."""

    __tablename__ = "education_profiles"

    member_id: Mapped[UUID] = mapped_column(
        ForeignKey("family_members.id", ondelete="CASCADE"), nullable=False, index=True
    )
    school_name: Mapped[str] = mapped_column(String(200), nullable=False)
    degree: Mapped[str | None] = mapped_column(String(100), nullable=True)
    field_of_study: Mapped[str | None] = mapped_column(String(100), nullable=True)
    start_year: Mapped[int | None] = mapped_column(SmallInteger, nullable=True)
    end_year: Mapped[int | None] = mapped_column(SmallInteger, nullable=True)
    gpa: Mapped[float | None] = mapped_column(Numeric(3, 2), nullable=True)

    # Relationships
    member = relationship("FamilyMember", back_populates="education_profiles")

    def __repr__(self) -> str:
        return f"<EducationProfile(id={self.id}, school={self.school_name})>"
