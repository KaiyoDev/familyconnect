"""FastAPI application factory and entry point."""
from fastapi import FastAPI
from config import settings
from app.api.middleware import register_middleware
from app.api.controllers.health_controller import router as health_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="Backend API for FamilyConnect platform",
    )

    # Register middleware
    register_middleware(app)

    # Include routers
    app.include_router(health_router, tags=["Health"])

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
    )
