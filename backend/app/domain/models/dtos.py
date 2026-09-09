from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DomainDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class RegisterRequest(BaseModel):
    full_name: str = Field(..., min_length=1, max_length=100)
    email: str = Field(..., min_length=3, max_length=150)
    password: str = Field(..., min_length=8, max_length=255)
    phone: str | None = Field(default=None, max_length=20)


class LoginRequest(BaseModel):
    email: str = Field(..., min_length=3, max_length=150)
    password: str = Field(..., min_length=1, max_length=255)


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int | None = Field(default=None, ge=0)


class UserDTO(DomainDTO):
    id: UUID
    full_name: str
    email: str
    phone: str | None = None
    role: str
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None


class CreateFamilyRequest(BaseModel):
    family_name: str = Field(..., min_length=1, max_length=150)
    description: str | None = Field(default=None, max_length=2000)


class FamilyDTO(DomainDTO):
    id: UUID
    family_name: str
    description: str | None = None
    created_by: UUID
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None


class MemberDTO(DomainDTO):
    id: UUID
    family_id: UUID
    branch_id: UUID | None = None
    user_id: UUID | None = None
    full_name: str
    gender: str
    date_of_birth: date | None = None
    is_alive: bool
    date_of_death: date | None = None
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None


class CreatePostRequest(BaseModel):
    family_id: UUID
    content: str = Field(..., min_length=1, max_length=2000)
    visibility_scope: str = "FAMILY"
    branch_id: UUID | None = None
    media_urls: list[str] | None = None


class PostDTO(DomainDTO):
    id: UUID
    family_id: UUID
    author_id: UUID
    content: str
    visibility_scope: str
    branch_id: UUID | None = None
    status: str
    media_urls: list[str] | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


class CommentDTO(DomainDTO):
    id: UUID
    post_id: UUID
    author_id: UUID
    content: str
    created_at: datetime | None = None
    updated_at: datetime | None = None


class CreateEventRequest(BaseModel):
    family_id: UUID
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=5000)
    location: str | None = Field(default=None, max_length=255)
    start_time: datetime
    end_time: datetime | None = None
    type: str = Field(..., min_length=1, max_length=30)


class EventDTO(DomainDTO):
    id: UUID
    family_id: UUID
    title: str
    description: str | None = None
    location: str | None = None
    start_time: datetime
    end_time: datetime | None = None
    type: str
    status: str
    created_by: UUID
    created_at: datetime | None = None
    updated_at: datetime | None = None


class RSVPDTO(DomainDTO):
    id: UUID
    event_id: UUID
    member_id: UUID | None = None
    guest_email: str | None = None
    response: str
    responded_at: datetime | None = None