"""Test configuration — async database for FastAPI test client."""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from create_app import create_app
from app.infrastructure.databases.base import Base
from app.infrastructure.databases.database import get_db as prod_get_db

TEST_DATABASE_URL = "sqlite+aiosqlite:///./test.db"

test_engine = create_async_engine(
    TEST_DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False},
)
TestingAsyncSessionLocal = async_sessionmaker(
    test_engine, class_=AsyncSession, expire_on_commit=False
)


async def test_get_db() -> AsyncSession:
    """Override dependency that yields an async session bound to test engine."""
    async with TestingAsyncSessionLocal() as session:
        try:
            yield session
        finally:
            pass


@pytest.fixture(scope="session", autouse=True)
async def setup_db():
    """Create tables once before all tests."""
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await test_engine.dispose()


@pytest.fixture(scope="session")
def client():
    app = create_app()
    app.dependency_overrides[prod_get_db] = test_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture
def test_user(client):
    email = "test@example.com"
    # Try to register — ignore if already exists
    client.post("/auth/register", json={
        "email": email,
        "password": "password123",
        "full_name": "Test User",
        "phone": None,
    })
    login_resp = client.post("/auth/login", json={
        "email": email,
        "password": "password123",
    })
    token = None
    refresh_token = None
    if login_resp.status_code == 200:
        data = login_resp.json().get("data") or {}
        token = data.get("access_token")
        refresh_token = data.get("refresh_token")
    return {
        "email": email,
        "token": token,
        "refresh_token": refresh_token,
    }
