"""Application service for administrator operations."""
from uuid import UUID

from app.infrastructure.repositories.admin_repository import AdminRepository


class AdminServiceError(Exception):
    pass


class AdminNotFoundError(AdminServiceError):
    pass


class AdminValidationError(AdminServiceError):
    pass


class AdminService:
    ALLOWED_STATUSES = {"ACTIVE", "SUSPENDED", "BLOCKED", "INACTIVE"}
    ALLOWED_CONTENT_TYPES = {"post", "comment"}
    ALLOWED_MODERATION_STATUSES = {"PUBLISHED", "REMOVED", "DRAFT"}

    def __init__(self, repository: AdminRepository):
        self.repository = repository

    async def list_users(self, page: int = 1, page_size: int = 20, role: str | None = None, status: str | None = None):
        if page < 1 or page_size < 1 or page_size > 100:
            raise AdminValidationError("page must be >= 1 and page_size must be between 1 and 100")
        users = await self.repository.list_users((page - 1) * page_size, page_size, role, status)
        return {"items": users, "page": page, "page_size": page_size, "count": len(users)}

    async def activate_user(self, user_id: UUID, status: str):
        status = status.upper()
        if status not in self.ALLOWED_STATUSES:
            raise AdminValidationError("status must be ACTIVE, SUSPENDED, BLOCKED, or INACTIVE")
        user = await self.repository.get_user(user_id)
        if user is None:
            raise AdminNotFoundError("User not found")
        return await self.repository.update_user_status(user, status)

    async def suspend_user(self, user_id: UUID):
        return await self.activate_user(user_id, "SUSPENDED")

    async def get_audit_log(self, page: int = 1, page_size: int = 50):
        if page < 1 or page_size < 1 or page_size > 100:
            raise AdminValidationError("page must be >= 1 and page_size must be between 1 and 100")
        items = await self.repository.list_audit_logs((page - 1) * page_size, page_size)
        return {"items": items, "page": page, "page_size": page_size, "count": len(items)}

    async def moderate_content(self, content_type: str, content_id: UUID, status: str):
        content_type = content_type.lower()
        status = status.upper()
        if content_type not in self.ALLOWED_CONTENT_TYPES:
            raise AdminValidationError("content_type must be post or comment")
        if status not in self.ALLOWED_MODERATION_STATUSES:
            raise AdminValidationError("status must be PUBLISHED, REMOVED, or DRAFT")
        if content_type == "post":
            content = await self.repository.moderate_post(content_id, status)
        else:
            content = await self.repository.moderate_comment(content_id, status)
        if content is None:
            raise AdminNotFoundError("Content not found")
        return content

    async def get_system_config(self):
        return {item.key: item.value for item in await self.repository.get_config()}

    async def update_system_config(self, values: dict):
        if not values:
            raise AdminValidationError("At least one configuration value is required")
        return {item.key: item.value for item in await self.repository.update_config(values)}