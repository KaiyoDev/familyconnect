from sqlalchemy import Column, String, Text, DateTime
from app.infrastructure.databases.base import Base


class AppRelationship(Base):
    __tablename__ = 'relationships'

    id = Column(String(36), primary_key=True)
    from_member_id = Column(String(36), nullable=False)
    to_member_id = Column(String(36), nullable=False)
    type = Column(String(30), nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
