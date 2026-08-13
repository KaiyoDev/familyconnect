"""Application configuration using pydantic-settings."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    app_name: str = "FamilyConnect API"
    debug: bool = False
    database_url: str
    secret_key: str
    cors_origins: list[str] = ["http://localhost:3000", "http://localhost:5173"]

    class Config:
        """Pydantic config."""
        env_file = ".env"
        case_sensitive = False


settings = Settings()
