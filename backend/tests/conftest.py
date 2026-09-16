import sys
import os

# --- THÊM 4 DÒNG NÀY ĐỂ FIX LỖI IMPORT ---
# Lấy đường dẫn tuyệt đối của thư mục gốc 'familyconnect' và thư mục 'backend'
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
BACKEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, BACKEND_DIR)
# ----------------------------------------

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import code của bạn
try:
    from backend.main import app 
    from backend.database import Base, get_db
except ModuleNotFoundError:
    # Nếu code của bạn không dùng tiền tố 'backend.', thử import trực tiếp
    from main import app
    from database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c

@pytest.fixture
def test_user(client):
    user_data = {"email": "test@example.com", "password": "password123"}
    client.post("/api/auth/register", json=user_data)
    response = client.post("/api/auth/login", data={"username": "test@example.com", "password": "password123"})
    token = None
    if response.status_code == 200:
        token = response.json().get("access_token")
    return {"email": "test@example.com", "token": token}
