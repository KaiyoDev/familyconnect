"""Central route registration (mirror of teacher's src/api/routes.py).

Responsibility: register all API blueprints/routers with the application.
Teacher used `register_routes(app)` with Flask Blueprints.
FastAPI adaptation: register all APIRouter instances via `app.include_router`.
"""
from fastapi import FastAPI


def register_routes(app: FastAPI) -> None:
    """Register the existing application routes and administrator routes."""
    from app.api.controllers.health_controller import router as health_router
    from app.api.controllers.auth_controller import router as auth_router
    from app.api.controllers.event_controller import router as event_router
    from app.api.controllers.community_controller import router as community_router
    from app.api.controllers.ai_controller import router as ai_router
    from app.api.controllers.admin_controller import router as admin_router

    app.include_router(health_router, tags=["Health"])
    app.include_router(auth_router, prefix="/api/v1", tags=["Auth"])
    app.include_router(event_router, prefix="/api/v1", tags=["Events"])
    app.include_router(community_router, prefix="/api/v1", tags=["Community"])
    app.include_router(ai_router, prefix="/api/v1", tags=["AI"])
    app.include_router(admin_router)
