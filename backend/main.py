feature/FT8-35-api-spec
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr

app = FastAPI(title="FamilyConnect API")

# Cấu trúc dữ liệu đầu vào
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# API Đăng nhập
@app.post("/api/v1/auth/login")
async def login(payload: LoginRequest):
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Kiểm tra tài khoản mẫu
    if payload.email == "user@example.com" and payload.password == "Password123!":
        return {
            "success": True,
            "data": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "refresh_token": "d9b2d63d-a233-4123-bf3e-123456789abc",
                "token_type": "Bearer",
                "expires_in": 1800
            },
            "message": "Operation successful",
            "timestamp": current_time
        }
    
    # Trả về lỗi nếu sai tài khoản
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={
            "success": False,
            "error": {
                "code": "AUTHENTICATION_FAILED",
                "message": "Thông tin đăng nhập không chính xác"
            },
            "timestamp": current_time
        }
    )
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
 develop
