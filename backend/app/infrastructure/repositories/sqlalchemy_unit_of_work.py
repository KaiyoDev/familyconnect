"""SQLAlchemy transaction adapter."""
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.interfaces.unit_of_work import IUnitOfWork


class SQLAlchemyUnitOfWork(IUnitOfWork):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
