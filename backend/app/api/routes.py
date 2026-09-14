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
    from app.api.controllers.family_controller import router as family_router
    from app.api.controllers.event_controller import family_router as event_family_router
    from app.api.controllers.event_controller import event_router as event_single_router
    from app.api.controllers.community_controller import router as community_router
    from app.api.controllers.ai_controller import router as ai_router
    from app.api.controllers.admin_controller import router as admin_router
    from app.api.controllers.heritage_controller import router as heritage_router
    from app.api.controllers.directory_controller import router as directory_router
    # Auth
    app.include_router(auth_router, tags=["Authentication"])
    # Health
    app.include_router(health_router, tags=["Health"])
    # Family & Genealogy
    app.include_router(family_router, tags=["Family"])
    # Event Services
    app.include_router(event_family_router, tags=["Event Services"])
    app.include_router(event_single_router, tags=["Event Services"])
    # Community
    app.include_router(community_router, tags=["Community"])
    # AI
    app.include_router(ai_router, tags=["AI"])
    # Admin
    app.include_router(admin_router, tags=["Admin"])
    # Heritage
    app.include_router(heritage_router, tags=["Heritage"])
    # Directory
    app.include_router(directory_router, tags=["Directory"])
