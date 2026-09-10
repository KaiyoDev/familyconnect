from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt, JWTError
from config import settings

def create_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.jwt_algorithm)

def create_access_token(subject: str, role: str) -> str:
    return create_token(
        {"sub": subject, "role": role, "type": "access"},
        timedelta(minutes=settings.access_token_expire_minutes)
    )

def create_refresh_token(subject: str) -> str:
    return create_token(
        {"sub": subject, "type": "refresh"},
        timedelta(days=settings.refresh_token_expire_days)
    )

def decode_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.jwt_algorithm])
        return payload
    except JWTError:
        return None
