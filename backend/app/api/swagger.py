"""Swagger/OpenAPI configuration (mirror of teacher's src/api/swagger.py).

Responsibility: configure and initialize the OpenAPI/Swagger documentation.
Teacher used APISpec with FlaskPlugin + MarshmallowPlugin for Swagger 2.0.
FastAPI has built-in OpenAPI support via `app.openapi()`. This module
provides additional configuration and schema registration if needed.

NOTE: FastAPI auto-generates OpenAPI docs at /docs (Swagger UI) and /redoc.
This module is reserved for custom OpenAPI configuration.
"""
from fastapi import FastAPI
from config import settings


def setup_swagger(app: FastAPI) -> None:
    """Configure Swagger/OpenAPI documentation for the application.

    FastAPI provides built-in OpenAPI support. This function customizes
    the documentation configuration.
    """
    # Update OpenAPI metadata
    app.openapi_info.title = settings.app_name
    app.openapi_info.description = "Backend API for FamilyConnect platform"
    app.openapi_info.version = "0.1.0"

    # Custom OpenAPI schema can be extended here
    # Example: add custom security schemes, response models, etc.
