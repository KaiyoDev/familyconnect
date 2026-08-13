"""SQLAlchemy base model with common fields."""
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, DateTime, func


class Base(DeclarativeBase):
    """Base class for all database models."""

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
