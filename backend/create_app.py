"""Application factory (mirror of teacher's src/create_app.py).

Responsibility: create and configure the FastAPI application.
Teacher's pattern: create_app() → setup_logging, init_db, setup_middleware, register_routes.
"""
import sys

if sys.platform == "win32":
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi import FastAPI
from config import settings
from app_logging import setup_logging
from app.infrastructure.databases.database import engine
from app.api.middleware import register_middleware
from app.api.routes import register_routes


def create_app() -> FastAPI:
    """Create and configure the FastAPI application.

    Follows teacher's pattern:
    1. Setup logging
    2. Initialize database
    3. Setup middleware
    4. Register routes
    """
    # 1. Setup logging
    setup_logging()

    # 2. Create FastAPI app
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="Backend API for FamilyConnect platform",
    )

    # 3. Setup middleware (CORS, logging, error handlers)
    register_middleware(app)

    # 4. Register all API routes
    register_routes(app)

    # 5. Startup/shutdown events
    @app.on_event("startup")
    async def startup_event():
        """Application startup event."""
        pass

    @app.on_event("shutdown")
    async def shutdown_event():
        """Application shutdown event."""
        await engine.dispose()

    return app
