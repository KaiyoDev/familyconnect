"""Persistence operations for administration features."""
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.models.admin import AuditLog, Notification, SystemConfig
from app.infrastructure.models.community import Comment, Post
from app.infrastructure.models.user import User


class AdminRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_users(self, offset: int, limit: int, role: str | None = None, status: str | None = None):
        query = select(User).order_by(User.created_at.desc()).offset(offset).limit(limit)
        if role:
            query = query.where(User.role == role)
        if status:
            query = query.where(User.status == status)
        result = await self.db.execute(query)
        return list(result.scalars().all())

    async def get_user(self, user_id: UUID) -> User | None:
        return await self.db.get(User, user_id)

    async def update_user_status(self, user: User, new_status: str) -> User:
        user.status = new_status
        self.db.add(
            Notification(
                user_id=user.id,
                notification_type="ACCOUNT",
                title="Account status updated",
                message=f"Your account status is now {new_status}.",
                data={"status": new_status},
            )
        )
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def list_audit_logs(self, offset: int, limit: int):
        result = await self.db.execute(
            select(AuditLog).order_by(AuditLog.created_at.desc()).offset(offset).limit(limit)
        )
        return list(result.scalars().all())

    async def add_audit_log(self, **values) -> AuditLog:
        audit_log = AuditLog(**values)
        self.db.add(audit_log)
        await self.db.commit()
        await self.db.refresh(audit_log)
        return audit_log

    async def moderate_post(self, content_id: UUID, status: str) -> Post | None:
        content = await self.db.get(Post, content_id)
        if content is None:
            return None
        content.status = status
        await self.db.commit()
        await self.db.refresh(content)
        return content

    async def moderate_comment(self, content_id: UUID, status: str) -> Comment | None:
        content = await self.db.get(Comment, content_id)
        if content is None:
            return None
        content.status = status
        await self.db.commit()
        await self.db.refresh(content)
        return content

    async def get_config(self) -> list[SystemConfig]:
        result = await self.db.execute(select(SystemConfig).order_by(SystemConfig.key))
        return list(result.scalars().all())

    async def update_config(self, values: dict) -> list[SystemConfig]:
        existing = {item.key: item for item in await self.get_config()}
        for key, value in values.items():
            if key in existing:
                existing[key].value = value
            else:
                self.db.add(SystemConfig(key=key, value=value))
        await self.db.commit()
        return await self.get_config()