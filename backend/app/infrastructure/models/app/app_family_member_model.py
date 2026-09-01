from sqlalchemy import Column, String, Boolean, Date, DateTime
from app.infrastructure.databases.base import Base


class AppFamilyMember(Base):
    __tablename__ = 'family_members'

    id = Column(String(36), primary_key=True)
    family_id = Column(String(36), nullable=False)
    branch_id = Column(String(36), nullable=True)
    user_id = Column(String(36), unique=True, nullable=True)
    full_name = Column(String(100), nullable=False)
    gender = Column(String(20), nullable=False, default='UNKNOWN')
    date_of_birth = Column(Date, nullable=True)
    is_alive = Column(Boolean, nullable=False, default=True)
    date_of_death = Column(Date, nullable=True)
    status = Column(String(20), nullable=False, default='PENDING')
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
