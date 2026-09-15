import pytest

# Tùy thuộc vào code thực tế của bạn, prefix URL có thể là /api/auth hoặc /auth. 
# Bạn hãy sửa lại các đường dẫn (như "/api/auth/register") cho khớp với router trong FastAPI của bạn nhé.

def test_register_success(client):
    response = client.post("/api/auth/register", json={
        "email": "newuser@example.com",
        "password": "strongpassword123",
        "full_name": "New User" # Thêm các field bắt buộc khác nếu model của bạn yêu cầu
    })
    assert response.status_code == 201 or response.status_code == 200
    assert "email" in response.json()
    assert response.json()["email"] == "newuser@example.com"

def test_register_duplicate_email(client, test_user):
    # test_user đã được tạo sẵn email "test@example.com" ở conftest.py
    response = client.post("/api/auth/register", json={
        "email": test_user["email"],
        "password": "anotherpassword123"
    })
    assert response.status_code == 400 # Bad request do trùng email

def test_register_invalid_password(client):
    response = client.post("/api/auth/register", json={
        "email": "badpass@example.com",
        "password": "123" # Giả sử hệ thống yêu cầu pass > 6 ký tự
    })
    # Tùy logic bạn viết (có thể là 400 hoặc 422 Unprocessable Entity do Pydantic validate)
    assert response.status_code in [400, 422] 

def test_login_success(client, test_user):
    # Dùng form-data (OAuth2PasswordRequestForm) thường được dùng trong FastAPI
    response = client.post("/api/auth/login", data={
        "username": test_user["email"],
        "password": "password123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"].lower() == "bearer"

def test_login_wrong_password(client, test_user):
    response = client.post("/api/auth/login", data={
        "username": test_user["email"],
        "password": "wrongpassword!"
    })
    assert response.status_code == 401 # Unauthorized

def test_login_inactive_account(client):
    # Mock một user bị khóa/inactive nếu DB của bạn có cờ is_active
    # Ở đây viết khung sẵn, tùy thuộc logic API của bạn
    pass 

def test_profile_get_with_token(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    response = client.get("/api/auth/profile", headers=headers) # API lấy thông tin user hiện tại
    assert response.status_code == 200
    assert response.json()["email"] == test_user["email"]

def test_profile_get_without_token(client):
    response = client.get("/api/auth/profile")
    assert response.status_code == 401 # Phải báo lỗi Unauthorized

def test_token_refresh(client, test_user):
    # Nếu hệ thống bạn có API refresh token
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    response = client.post("/api/auth/refresh", headers=headers)
    
    # Bỏ qua test này nếu bạn chưa code chức năng refresh token
    if response.status_code != 404: 
        assert response.status_code == 200
        assert "access_token" in response.json()