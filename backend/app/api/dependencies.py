"""FastAPI dependencies for dependency injection."""
from app.infrastructure.databases.database import get_db

# Re-export get_db for use in controllers
__all__ = ["get_db"]
