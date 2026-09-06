"""Central route registration (mirror of teacher's src/api/routes.py).

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

    """Central route registration."""

from fastapi import FastAPI