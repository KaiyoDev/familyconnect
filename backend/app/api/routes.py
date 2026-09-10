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

    from app.api.controllers.family_controller import router as family_router
    app.include_router(family_router, prefix="/api/families", tags=["Families"])

    # Future controllers will be registered here:
    # from app.api.controllers.auth_controller import router as auth_router
    # app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
    #
    # from app.api.controllers.user_controller import router as user_router
    # app.include_router(user_router, prefix="/api/users", tags=["Users"])
    #
    # from app.api.controllers.family_controller import router as family_router
    # app.include_router(family_router, prefix="/api/families", tags=["Families"])
    #
    # from app.api.controllers.family_member_controller import router as family_member_router
    # app.include_router(family_member_router, prefix="/api/family-members", tags=["Family Members"])
    #
    # from app.api.controllers.relationship_controller import router as relationship_router
    # app.include_router(relationship_router, prefix="/api/relationships", tags=["Relationships"])
    #
    # from app.api.controllers.event_controller import router as event_router
    # app.include_router(event_router, prefix="/api/events", tags=["Events"])
    #
    # from app.api.controllers.post_controller import router as post_router
    # app.include_router(post_router, prefix="/api/posts", tags=["Posts"])
    #
    # from app.api.controllers.heritage_controller import router as heritage_router
    # app.include_router(heritage_router, prefix="/api/heritage", tags=["Heritage"])
    #
    # from app.api.controllers.ai_controller import router as ai_router
    # app.include_router(ai_router, prefix="/api/ai", tags=["AI"])
