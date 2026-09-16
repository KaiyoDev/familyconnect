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
        # Frontend ADM-02 expects a bare array (envelope.data: AdminUser[])
        return [self._user_to_dict(u) for u in users]

    @staticmethod
    def _user_to_dict(u) -> dict:
        return {"id": str(u.id), "email": u.email, "full_name": u.full_name,
                "system_role": u.role, "role": u.role, "family_count": 0,
                "status": u.status,
                "created_at": u.created_at.isoformat() if getattr(u, "created_at", None) else None}

    async def get_user(self, user_id: UUID) -> dict:
        user = await self.repository.get_user(user_id)
        if user is None:
            raise AdminNotFoundError("User not found")
        return self._user_to_dict(user)

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
        # Frontend ADM-04 expects a bare array in AuditLogEntry shape
        import json as _json
        return [{"id": str(i.id), "action": i.action, "user": str(i.actor_id) if i.actor_id else "system",
                 "ip": None, "time": i.created_at.isoformat() if getattr(i, "created_at", None) else None,
                 "details": _json.dumps(i.details, default=str) if i.details is not None else ""}
                for i in items]

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

    async def moderate_any(self, content_id: UUID, status: str, content_type: str | None = None) -> dict:
        """Moderate content when the type is unknown — try post, then comment.
        Used by frontend /admin/moderation/{id}/approve|remove."""
        status = status.upper()
        if status not in self.ALLOWED_MODERATION_STATUSES:
            raise AdminValidationError("status must be PUBLISHED, REMOVED, or DRAFT")
        candidates = [content_type.lower()] if content_type else ["post", "comment"]
        found = None
        matched = None
        for ct in candidates:
            if ct not in self.ALLOWED_CONTENT_TYPES:
                continue
            found = await self.repository.moderate_post(content_id, status) if ct == "post" \
                else await self.repository.moderate_comment(content_id, status)
            if found is not None:
                matched = ct
                break
        if found is None:
            raise AdminNotFoundError("Content not found")
        return {"id": str(found.id), "content_type": matched, "status": status,
                "message": f"Content {matched} {status.lower()}d"}

    async def get_system_config(self):
        return {item.key: item.value for item in await self.repository.get_config()}

    async def list_moderation(self, limit: int = 100) -> list[dict]:
        """Frontend ADM-03 listModeration — bare array of ModerationItem dicts."""
        return await self.repository.list_moderation(limit)

    async def update_system_config(self, values: dict):
        if not values:
            raise AdminValidationError("At least one configuration value is required")
        return {item.key: item.value for item in await self.repository.update_config(values)}