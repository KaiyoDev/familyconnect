from sqlalchemy import Column, String, DateTime
from app.infrastructure.databases.base import Base


class AppEventRSVP(Base):
    __tablename__ = 'event_rsvps'

    id = Column(String(36), primary_key=True)
    event_id = Column(String(36), nullable=False)
    member_id = Column(String(36), nullable=True)
    guest_email = Column(String(150), nullable=True)
    response = Column(String(20), nullable=False)
    responded_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
