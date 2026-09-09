from fastapi import APIRouter
from app.api.controllers.auth_controller import router as auth_router

fix/FT8-40-auth-service
api_router = APIRouter(prefix="/api")
api_router.include_router(auth_router)
Responsibility: register all API blueprints/routers with the application.
Teacher used `register_routes(app)` with Flask Blueprints.
FastAPI adaptation: register all APIRouter instances via `app.include_router`.
"""
from fastapi import FastAPI


def register_routes(app: FastAPI) -> None:
    """Register all API routers with the FastAPI application."""

    # Health check
    from app.api.controllers.health_controller import router as health_router
    app.include_router(health_router, tags=["Health"])

    # Community (posts, comments, reactions)
    from app.api.controllers.community_controller import router as community_router
    app.include_router(community_router, prefix="/api/v1", tags=["Community"])

    # AI Assistant (stub)
    from app.api.controllers.ai_controller import router as ai_router
    app.include_router(ai_router, prefix="/api/v1", tags=["AI"])
develop
