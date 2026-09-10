"""Administrator-only API endpoints."""
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field

from app.api.dependencies import get_db, require_admin
from app.infrastructure.repositories.admin_repository import AdminRepository
from app.services.admin_service import AdminNotFoundError, AdminService, AdminServiceError

router = APIRouter(prefix="/api/admin", tags=["Admin"], dependencies=[Depends(require_admin)])


def get_admin_service(db=Depends(get_db)) -> AdminService:
    return AdminService(AdminRepository(db))


class UserStatusRequest(BaseModel):
    status: str = Field(..., min_length=1, max_length=20)


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


@router.get("/config")
async def get_system_config(service: AdminService = Depends(get_admin_service)):
    return await service.get_system_config()


@router.put("/config", status_code=status.HTTP_200_OK)
async def update_system_config(payload: SystemConfigRequest, service: AdminService = Depends(get_admin_service)):
    try:
        return await service.update_system_config(payload.values)
    except AdminServiceError as exc:
        raise _handle_error(exc) from exc