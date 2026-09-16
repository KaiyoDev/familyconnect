"""Database engine and session management."""
import sys
if sys.platform == "win32":
    import selectors
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.engine import make_url
from config import settings
from app.infrastructure.databases.base import Base

database_url = make_url(settings.database_url)
use_ssl = (
    database_url.drivername == "postgresql+asyncpg"
    and database_url.host not in {"localhost", "127.0.0.1", "::1"}
)

engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
    future=True,
    connect_args={"ssl": "require"} if use_ssl else {},
)

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db() -> AsyncSession:
    """Dependency that provides a database session."""
    async with async_session() as session:
        yield session
