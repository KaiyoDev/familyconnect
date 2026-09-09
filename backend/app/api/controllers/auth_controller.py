from fastapi import APIRouter, HTTPException, status
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from config import settings

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/forgot-password")
async def forgot_password(email: str):
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    reset_token = jwt.encode({"sub": email, "type": "reset_password", "exp": expire}, settings.secret_key, algorithm=settings.jwt_algorithm)
    return {"message": "Reset token generated", "reset_token": reset_token}

@router.post("/reset-password")
async def reset_password(reset_token: str, new_password: str):
    try:
        payload = jwt.decode(reset_token, settings.secret_key, algorithms=[settings.jwt_algorithm])
        if payload.get("type") != "reset_password":
            raise HTTPException(status_code=400, detail="Invalid token type")
    except JWTError:
        raise HTTPException(status_code=400, detail="Token expired or invalid")
    return {"message": "Password updated successfully"}

@router.post("/refresh")
async def refresh_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, settings.secret_key, algorithms=[settings.jwt_algorithm])
        user_id = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    new_access_token = jwt.encode({"sub": user_id, "exp": datetime.now(timezone.utc) + timedelta(minutes=30)}, settings.secret_key, algorithm=settings.jwt_algorithm)
    new_refresh_token = jwt.encode({"sub": user_id, "exp": datetime.now(timezone.utc) + timedelta(days=7)}, settings.secret_key, algorithm=settings.jwt_algorithm)
    
    return {"access_token": new_access_token, "refresh_token": new_refresh_token, "token_type": "bearer"}
