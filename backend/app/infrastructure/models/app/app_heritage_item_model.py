from sqlalchemy import Column, String, Text, DateTime
from app.infrastructure.databases.base import Base


class AppHeritageItem(Base):
    __tablename__ = 'heritage_items'

    id = Column(String(36), primary_key=True)
    family_id = Column(String(36), nullable=False)
    branch_id = Column(String(36), nullable=True)
    title = Column(String(200), nullable=False)
    type = Column(String(30), nullable=False)
    category = Column(String(50), nullable=False)
    period = Column(String(100), nullable=True)
    content = Column(Text, nullable=True)
    status = Column(String(20), nullable=False, default='DRAFT')
    media_url = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
