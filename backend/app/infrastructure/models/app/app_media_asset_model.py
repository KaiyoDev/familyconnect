from sqlalchemy import Column, String, DateTime
from app.infrastructure.databases.base import Base


class AppMediaAsset(Base):
    __tablename__ = 'media_assets'

    id = Column(String(36), primary_key=True)
    event_id = Column(String(36), nullable=True)
    family_id = Column(String(36), nullable=True)
    uploaded_by = Column(String(36), nullable=False)
    caption = Column(String(255), nullable=True)
    url = Column(String(500), nullable=False)
    media_type = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
