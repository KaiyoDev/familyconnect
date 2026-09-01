from sqlalchemy import Column, String, DateTime
from app.infrastructure.databases.base import Base


class AppUser(Base):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)
    role = Column(String(20), nullable=False, default='USER')
    status = Column(String(20), nullable=False, default='PENDING')
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)
