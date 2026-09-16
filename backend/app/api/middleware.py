"""FastAPI middleware configuration."""
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.domain.exceptions import DomainException
import json
import logging
import time
from datetime import datetime, timezone

logger = logging.getLogger(__name__)


def register_middleware(app: FastAPI) -> None:
    """Register all middleware for the application."""

    # CORS middleware
    from config import settings
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Request logging middleware
    @app.middleware("http")
    async def logging_middleware(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        if request.url.path.startswith(("/admin", "/api/admin")) and response.status_code < 400:
            current_user = getattr(request.state, "current_user", None)
            if current_user and request.method != "GET":
                from app.infrastructure.databases.database import async_session
                from app.infrastructure.models.admin import AuditLog
                from uuid import UUID

                action = "MODERATE" if request.url.path.endswith("/moderate") else "UPDATE"
                try:
                    async with async_session() as audit_session:
                        audit_session.add(
                            AuditLog(
                                actor_id=UUID(str(current_user["id"])),
                                action=action,
                                resource_type="admin_endpoint",
                                details={"method": request.method, "path": request.url.path},
                            )
                        )
                        await audit_session.commit()
                except Exception:
                    logger.exception("Failed to write admin audit log")

        logger.info(
            f"{request.method} {request.url.path} "
            f"- {response.status_code} ({process_time:.3f}s)"
        )
        return response

    # Global exception handler for domain exceptions
    @app.exception_handler(DomainException)
    async def domain_exception_handler(request: Request, exc: DomainException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.message}
        )

    # Global exception handler for unexpected errors
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled exception: {exc}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error"}
        )

    # Response envelope middleware — frontend expects {success, data, timestamp}
    @app.middleware("http")
    async def envelope_middleware(request: Request, call_next):
        response = await call_next(request)

        # Errors keep FastAPI default shape ({"detail": ...}) — frontend reads error.response.data.detail
        if response.status_code >= 400 or response.status_code in (204, 304):
            return response

        content_type = response.headers.get("content-type", "")
        if "application/json" not in content_type:
            return response

        body = b""
        async for chunk in response.body_iterator:
            body += chunk
        if not body:
            return response

        try:
            payload = json.loads(body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return response

        if isinstance(payload, dict) and "success" in payload:
            return response

        headers = {k: v for k, v in response.headers.items() if k.lower() not in ("content-length", "content-type")}
        wrapped = {
            "success": True,
            "data": payload,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        from fastapi.responses import Response
        return Response(
            status_code=response.status_code,
            content=json.dumps(wrapped, default=str).encode("utf-8"),
            media_type="application/json",
            headers=headers,
        )
