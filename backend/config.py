"""Application configuration using pydantic-settings."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    app_name: str = "FamilyConnect API"
    debug: bool = False
    database_url: str
    secret_key: str
    cors_origins: list[str] = ["http://localhost:3000", "http://localhost:5173"]

    # AI Provider Settings (stub — wire real provider when API key available)
    ai_provider: str = "mock"  # "mock" | "openai" | "claude"
    ai_api_key: str = ""
    ai_base_url: str = ""  # custom endpoint (Ollama, vLLM, LM Studio, gateway…)
    ai_model: str = "gpt-4o-mini"  # model name used by provider
    ai_max_tokens: int = 1024
    ai_temperature: float = 0.7

    class Config:
        """Pydantic config."""
        env_file = ".env"
        case_sensitive = False


settings = Settings()
