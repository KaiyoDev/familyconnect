from sqlalchemy import Column, String, Text, DateTime
from app.infrastructure.databases.base import Base


class AppEvent(Base):
    __tablename__ = 'events'

    id = Column(String(36), primary_key=True)
    family_id = Column(String(36), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    location = Column(String(255), nullable=True)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=True)
    type = Column(String(30), nullable=False)
    status = Column(String(20), nullable=False, default='OPEN')
    created_by = Column(String(36), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
