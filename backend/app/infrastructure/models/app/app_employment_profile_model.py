from sqlalchemy import Column, String, Text, Date, Boolean, DateTime
from app.infrastructure.databases.base import Base


class AppEmploymentProfile(Base):
    __tablename__ = 'employment_profiles'

    id = Column(String(36), primary_key=True)
    member_id = Column(String(36), nullable=False)
    company_name = Column(String(200), nullable=False)
    position = Column(String(100), nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    is_current = Column(Boolean, nullable=False, default=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
