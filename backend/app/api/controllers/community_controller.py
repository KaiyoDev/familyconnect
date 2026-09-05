from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.app.services.community_service import CommunityService
from backend.app.infrastructure.databases.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user():
    return {"id": UUID("00000000-0000-0000-0000-000000000000"), "family_id": UUID("00000000-0000-0000-0000-000000000000")}


router = APIRouter(prefix="/api", tags=["Community"])


class PostRequest(BaseModel):
    content: str
    media_urls: Optional[List[str]] = []


class CommentRequest(BaseModel):
    content: str


class ReactionRequest(BaseModel):
    type: str


class AnnouncementRequest(BaseModel):
    title: str
    body: str


@router.post("/families/{family_id}/posts", status_code=status.HTTP_201_CREATED)
def create_post(
    family_id: UUID,
    req: PostRequest,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    service = CommunityService(db)
    if user.get("family_id") != family_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not a member of this family")
    return service.create_post(family_id, user["id"], req.content, req.media_urls)


@router.get("/families/{family_id}/feed")
def get_feed(family_id: UUID, skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    service = CommunityService(db)
    return service.get_feed(family_id, skip, limit)


@router.get("/posts/{post_id}")
def get_post(post_id: UUID, db: Session = Depends(get_db)):
    service = CommunityService(db)
    post = service.get_post(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post


@router.get("/posts/{post_id}/comments")
def get_comments(post_id: UUID, db: Session = Depends(get_db)):
    service = CommunityService(db)
    return service.get_comments(post_id)


@router.put("/posts/{post_id}")
def update_post(
    post_id: UUID,
    req: PostRequest,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    service = CommunityService(db)
    try:
        return service.update_post(post_id, user["id"], req.content, req.media_urls)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    post_id: UUID,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    service = CommunityService(db)
    try:
        service.delete_post(post_id, user["id"])
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@router.post("/posts/{post_id}/comments", status_code=status.HTTP_201_CREATED)
def add_comment(
    post_id: UUID,
    req: CommentRequest,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    service = CommunityService(db)
    try:
        return service.add_comment(post_id, user["id"], req.content)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/posts/{post_id}/reactions", status_code=status.HTTP_201_CREATED)
def add_reaction(
    post_id: UUID,
    req: ReactionRequest,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    service = CommunityService(db)
    try:
        return service.add_reaction(post_id, user["id"], req.type)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/posts/{post_id}/reactions/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_reaction(
    post_id: UUID,
    user_id: UUID,
    reaction_type: str,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    service = CommunityService(db)
    try:
        service.remove_reaction(post_id, user_id, reaction_type)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/families/{family_id}/announcements", status_code=status.HTTP_201_CREATED)
def create_announcement(
    family_id: UUID,
    req: AnnouncementRequest,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    service = CommunityService(db)
    if user.get("family_id") != family_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not a member of this family")
    return service.create_announcement(family_id, user["id"], req.title, req.body)
