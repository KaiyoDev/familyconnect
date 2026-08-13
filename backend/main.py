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