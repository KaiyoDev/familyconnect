from sqlalchemy import Column, String, Text, DateTime
from app.infrastructure.databases.base import Base


class AppFamily(Base):
    __tablename__ = 'families'

    id = Column(String(36), primary_key=True)
    family_name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    created_by = Column(String(36), nullable=False)
    status = Column(String(20), nullable=False, default='ACTIVE')
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
