from pydantic import BaseModel, EmailStr
from typing import List, Optional
from uuid import UUID
from datetime import datetime

# --- AUTH & USER DTOs ---
class UserDTO(BaseModel):
    id: UUID
    email: EmailStr
    full_name: str
    is_active: bool
    created_at: datetime

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    full_name: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

# --- FAMILY DTOs ---
class FamilyDTO(BaseModel):
    id: UUID
    name: str
    description: Optional[str] = None
    creator_id: UUID
    created_at: datetime

class CreateFamilyRequest(BaseModel):
    name: str
    description: Optional[str] = None

class MemberDTO(BaseModel):
    user_id: UUID
    family_id: UUID
    role: str
    joined_at: datetime

# --- COMMUNITY DTOs ---
class PostDTO(BaseModel):
    id: UUID
    family_id: UUID
    author_id: UUID
    content: str
    created_at: datetime

class CreatePostRequest(BaseModel):
    family_id: UUID
    content: str

class CommentDTO(BaseModel):
    id: UUID
    post_id: UUID
    author_id: UUID
    content: str
    created_at: datetime

# --- EVENT DTOs ---
class EventDTO(BaseModel):
    id: UUID
    family_id: UUID
    creator_id: UUID
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime

class CreateEventRequest(BaseModel):
    family_id: UUID
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime

class RSVPDTO(BaseModel):
    event_id: UUID
    user_id: UUID
    status: str # e.g., 'going', 'maybe', 'declined'