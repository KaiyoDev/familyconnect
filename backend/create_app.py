"""Application factory (mirror of teacher's src/create_app.py).

Responsibility: create and configure the FastAPI application.
Teacher's pattern: create_app() → setup_logging, init_db, setup_middleware, register_routes.
"""
import sys
if sys.platform == "win32":
    import selectors
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi import FastAPI
from config import settings
from app_logging import setup_logging
from app.infrastructure.databases.database import engine
from app.api.middleware import register_middleware
from app.api.routes import register_routes


# ---------------------------------------------------------------------------
# Force-import all model packages so SQLAlchemy class registry is fully populated
# before any request hits the DB. Without this, creating an AIConversation instance
# triggers mapper configuration for ALL models, but genealogy.Family etc. are not
# yet registered → InvalidRequestError: 'Family' failed to locate a name.
# ---------------------------------------------------------------------------
from app.infrastructure.models import genealogy  # noqa: F401
from app.infrastructure.models import community  # noqa: F401
from app.infrastructure.models import event      # noqa: F401
from app.infrastructure.models import heritage   # noqa: F401
from app.infrastructure.models import directory  # noqa: F401
from app.infrastructure.models import user       # noqa: F401
from app.infrastructure.models import types      # noqa: F401
from app.infrastructure.models import app_ai_model  # noqa: F401


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
