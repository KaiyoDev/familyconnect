from sqlalchemy import Column, String, Integer, Numeric, DateTime
from app.infrastructure.databases.base import Base


class AppEducationProfile(Base):
    __tablename__ = 'education_profiles'

    id = Column(String(36), primary_key=True)
    member_id = Column(String(36), nullable=False)
    school_name = Column(String(200), nullable=False)
    degree = Column(String(100), nullable=True)
    field_of_study = Column(String(100), nullable=True)
    start_year = Column(Integer, nullable=True)
    end_year = Column(Integer, nullable=True)
    gpa = Column(Numeric(3, 2), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
