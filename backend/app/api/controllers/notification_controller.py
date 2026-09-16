"""Notification API endpoints — wired to the Notification model (admin.py).

Frontend `notificationApi`:
  GET  /notifications                 (PRF-02 list — expects a bare array)
  PUT  /notifications/{id}/read
  PUT  /notifications/read-all
  GET  /notifications/settings        (no settings model yet — defaults)
  PUT  /notifications/settings        (accepted, not persisted yet)
"""
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.infrastructure.databases.database import get_db
from app.infrastructure.models.admin import Notification

router = APIRouter(prefix="/notifications", tags=["Notifications"])


def _current_user_id(current_user: dict) -> UUID:
    uid = current_user.get("id") or current_user.get("sub")
    if not uid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not resolve current user")
    return UUID(str(uid))


def _to_dict(n: Notification) -> dict:
    return {
        "id": str(n.id),
        "notification_type": n.notification_type,
        "title": n.title,
        "message": n.message,
        "is_read": n.is_read,
        "data": n.data,
        "created_at": n.created_at.isoformat() if getattr(n, "created_at", None) else None,
    }


DEFAULT_SETTINGS = {
    "email_notifications": True,
    "event_reminders": True,
    "family_activity": True,
    "admin_alerts": False,
}


@router.get("")
async def list_notifications(current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    """Current user's notifications, newest first. Empty array until notifications are created."""
    uid = _current_user_id(current_user)
    rows = (await db.execute(
        select(Notification).where(Notification.user_id == uid).order_by(Notification.created_at.desc()).limit(100)
    )).scalars().all()
    return [_to_dict(n) for n in rows]


@router.put("/{notification_id}/read")
async def mark_read(notification_id: UUID, current_user: dict = Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    uid = _current_user_id(current_user)
    note = await db.get(Notification, notification_id)
    if note is None or note.user_id != uid:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found")
    note.is_read = True
    await db.commit()
    return _to_dict(note)


@router.put("/read-all")
async def mark_all_read(current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    uid = _current_user_id(current_user)
    result = await db.execute(
        update(Notification).where(Notification.user_id == uid, Notification.is_read.is_(False))
        .values(is_read=True)
    )
    await db.commit()
    return {"message": "All notifications marked as read", "updated": result.rowcount or 0}


@router.get("/settings")
async def get_settings(current_user: dict = Depends(get_current_user)):
    """No notification-settings table yet — return defaults so PRF-02 renders."""
    return dict(DEFAULT_SETTINGS)


@router.put("/settings")
async def update_settings(payload: dict | None = None, current_user: dict = Depends(get_current_user)):
    """Accepted but not persisted yet (no settings model); echo merged defaults."""
    merged = {**DEFAULT_SETTINGS, **(payload or {})}
    return {"message": "Notification settings accepted (persistence not wired yet)", **merged}
