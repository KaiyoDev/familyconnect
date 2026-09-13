from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/api/auth", tags=["Auth"])

# Mô hình dữ liệu giả lập (hoặc kết nối Database/SQLAlchemy thực tế của bạn)
fake_users_db = {}

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    full_name: str | None = None

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_data: UserRegister):
    if user_data.email in fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    if len(user_data.password) < 6:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be at least 6 characters"
        )
    fake_users_db[user_data.email] = {
        "email": user_data.email,
        "password": user_data.password,
        "full_name": user_data.full_name,
        "is_active": True
    }
    return {"message": "User registered successfully", "email": user_data.email}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.get("is_active", True):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return {"access_token": "fake-jwt-token-123", "token_type": "bearer"}

@router.get("/profile")
def get_profile():
    # Thêm logic kiểm tra Header Authorization thực tế ở đây
    return {"email": "test@example.com", "full_name": "Test User"}

@router.post("/refresh")
def token_refresh():
    return {"access_token": "new-fake-jwt-token-456", "token_type": "bearer"}