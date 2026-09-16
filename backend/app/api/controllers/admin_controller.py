"""Administrator-only API endpoints."""
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field

from app.api.dependencies import get_db, require_admin
from app.infrastructure.repositories.admin_repository import AdminRepository
from app.services.admin_service import AdminNotFoundError, AdminService, AdminServiceError

router = APIRouter(prefix="/admin", tags=["Admin"], dependencies=[Depends(require_admin)])


def get_admin_service(db=Depends(get_db)) -> AdminService:
    return AdminService(AdminRepository(db))


class UserStatusRequest(BaseModel):
    status: str | None = Field(default=None, min_length=1, max_length=20)
    role: str | None = Field(default=None, min_length=1, max_length=20)
    join_code: str | None = None
    # tolerate unknown fields from frontend adminApi.updateUser(data: any)
    model_config = {"extra": "allow"}


class ModerateContentRequest(BaseModel):
    content_type: str
    content_id: UUID
    status: str


class SystemConfigRequest(BaseModel):
    values: dict


def _handle_error(exc: AdminServiceError) -> HTTPException:
    code = 404 if isinstance(exc, AdminNotFoundError) else 400
    return HTTPException(status_code=code, detail=str(exc))


@router.get("/users")
async def list_users(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    role: str | None = None, user_status: str | None = Query(None, alias="status"),
    service: AdminService = Depends(get_admin_service),
):
    try:
        return await service.list_users(page, page_size, role, user_status)
    except AdminServiceError as exc:
        raise _handle_error(exc) from exc


@router.put("/users/{user_id}/status")
async def update_user_status(user_id: UUID, payload: UserStatusRequest, service: AdminService = Depends(get_admin_service)):
    try:
        return await service.activate_user(user_id, payload.status)
    except AdminServiceError as exc:
        raise _handle_error(exc) from exc


@router.get("/users/{user_id}")
async def get_user(user_id: UUID, service: AdminService = Depends(get_admin_service)):
    try:
        return await service.get_user(user_id)
    except AdminServiceError as exc:
        raise _handle_error(exc) from exc


@router.put("/users/{user_id}")
async def update_user(user_id: UUID, payload: UserStatusRequest, service: AdminService = Depends(get_admin_service)):
    """Frontend adminApi.updateUser — applies `status` when present (role update not persisted yet)."""
    if not payload.status:
        return {"message": "No updatable fields provided", "user_id": str(user_id)}
    try:
        return await service.activate_user(user_id, payload.status)
    except AdminServiceError as exc:
        raise _handle_error(exc) from exc


@router.post("/users/{user_id}/suspend")
async def suspend_user(user_id: UUID, service: AdminService = Depends(get_admin_service)):
    """Frontend adminApi.suspendUser — alias of status=SUSPENDED."""
    try:
        return await service.suspend_user(user_id)
    except AdminServiceError as exc:
        raise _handle_error(exc) from exc


@router.post("/users/{user_id}/activate")
async def activate_user(user_id: UUID, service: AdminService = Depends(get_admin_service)):
    """Frontend adminApi.activateUser — alias of status=ACTIVE."""
    try:
        return await service.activate_user(user_id, "ACTIVE")
    except AdminServiceError as exc:
        raise _handle_error(exc) from exc


@router.get("/audit-log")
async def get_audit_log(
    page: int = Query(1, ge=1), page_size: int = Query(50, ge=1, le=100),
    service: AdminService = Depends(get_admin_service),
):
    try:
        return await service.get_audit_log(page, page_size)
    except AdminServiceError as exc:
        raise _handle_error(exc) from exc


@router.post("/moderate")
async def moderate_content(payload: ModerateContentRequest, service: AdminService = Depends(get_admin_service)):
    try:
        return await service.moderate_content(payload.content_type, payload.content_id, payload.status)
    except AdminServiceError as exc:
        raise _handle_error(exc) from exc


@router.get("/moderation")
async def list_moderation(limit: int = Query(100, ge=1, le=500),
                          service: AdminService = Depends(get_admin_service)):
    """Frontend adminApi.listModeration — bare array of ModerationItem dicts."""
    return await service.list_moderation(limit)


@router.post("/moderation/{item_id}/approve")
async def approve_moderation(item_id: UUID, service: AdminService = Depends(get_admin_service)):
    """Frontend adminApi.approveContent — restores content to PUBLISHED."""
    try:
        return await service.moderate_any(item_id, "PUBLISHED")
    except AdminServiceError as exc:
        raise _handle_error(exc) from exc


@router.post("/moderation/{item_id}/remove")
async def remove_moderation(item_id: UUID, service: AdminService = Depends(get_admin_service)):
    """Frontend adminApi.removeContent — marks content REMOVED."""
    try:
        return await service.moderate_any(item_id, "REMOVED")
    except AdminServiceError as exc:
        raise _handle_error(exc) from exc


# ── Backup endpoints (frontend adminApi createBackup/listBackups/restoreBackup) ──
# No backup infrastructure (storage/pipeline) is wired yet; acknowledge so ADM-05 does not 404.

@router.post("/backup")
async def create_backup():
    return {"message": "Backup not configured yet", "backup_id": None}


@router.get("/backups")
async def list_backups():
    return []


@router.post("/restore")
async def restore_backup(payload: dict | None = None):
    return {"message": "Backup restore not configured yet", "backup_id": (payload or {}).get("backup_id")}


@router.get("/config")
async def get_system_config(service: AdminService = Depends(get_admin_service)):
    return await service.get_system_config()


@router.put("/config", status_code=status.HTTP_200_OK)
async def update_system_config(payload: SystemConfigRequest, service: AdminService = Depends(get_admin_service)):
    try:
        return await service.update_system_config(payload.values)
    except AdminServiceError as exc:
        raise _handle_error(exc) from exc