from uuid import UUID
from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, status
from app.api.dependencies import get_current_user

router = APIRouter(tags=["Event Services"])


class EventCreateSchema(BaseModel):
    title: str
    description: Optional[str] = None
    location: Optional[str] = None


class RSVPSchema(BaseModel):
    status: str


def check_family_access(user: dict, family_id: UUID):
    """Kiểm tra quyền truy cập của người dùng đối với Family (tránh lỗi IDOR)"""
    user_id = user.get("user_id") if isinstance(user, dict) else getattr(user, "id", None)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
    # TODO: Gọi service/repository kiểm tra user_id có thuộc family_id hay không
    # if not is_member(user_id, family_id):
    #     raise HTTPException(status_code=403, detail="Not authorized to access this family")


@router.post("/api/families/{family_id}/events", status_code=201)
async def create_event(
    family_id: UUID, 
    payload: EventCreateSchema, 
    current_user: dict = Depends(get_current_user)
):
    check_family_access(current_user, family_id)
    user_id = current_user.get("user_id") if isinstance(current_user, dict) else current_user.id
    return {
        "message": "Event created", 
        "family_id": str(family_id),
        "created_by": user_id
    }


@router.get("/api/families/{family_id}/events")
async def get_events(
    family_id: UUID, 
    current_user: dict = Depends(get_current_user)
):
    check_family_access(current_user, family_id)
    return []


@router.get("/api/events/{event_id}")
async def get_event(
    event_id: UUID, 
    current_user: dict = Depends(get_current_user)
):
    return {"event_id": str(event_id)}


@router.put("/api/events/{event_id}")
async def update_event(
    event_id: UUID, 
    payload: EventCreateSchema, 
    current_user: dict = Depends(get_current_user)
):
    return {"message": "Event updated"}


@router.delete("/api/events/{event_id}")
async def cancel_event(
    event_id: UUID, 
    current_user: dict = Depends(get_current_user)
):
    return {"message": "Event cancelled"}


@router.post("/api/events/{event_id}/rsvp")
async def rsvp_event(
    event_id: UUID, 
    payload: RSVPSchema, 
    current_user: dict = Depends(get_current_user)
):
    return {"message": "RSVP recorded"}


@router.get("/api/events/{event_id}/attendees")
async def get_attendees(
    event_id: UUID, 
    status: Optional[str] = None, 
    current_user: dict = Depends(get_current_user)
):
    return []
