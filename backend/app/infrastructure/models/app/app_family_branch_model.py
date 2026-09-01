from sqlalchemy import Column, String, Text, DateTime
from app.infrastructure.databases.base import Base


class AppFamilyBranch(Base):
    __tablename__ = 'family_branches'

    id = Column(String(36), primary_key=True)
    family_id = Column(String(36), nullable=False)
    branch_name = Column(String(150), nullable=False)
    founder_id = Column(String(36), nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
