import pytest

# Backend auth routes: /auth/register, /auth/login, /auth/profile, /auth/refresh
# Family routes: /families, /families/{id}, /families/{id}/members, /families/{id}/tree
# User profile: PUT /auth/me or PUT /users/me


def test_register_success(client):
    response = client.post("/auth/register", json={
        "email": "newuser@example.com",
        "password": "strongpassword123",
        "full_name": "New User",
        "phone": None,
    })
    assert response.status_code in [200, 201]


def test_register_duplicate_email(client, test_user):
    response = client.post("/auth/register", json={
        "email": test_user["email"],
        "password": "anotherpassword123",
        "full_name": "Another User",
        "phone": None,
    })
    assert response.status_code == 400


def test_register_invalid_payload(client):
    response = client.post("/auth/register", json={
        "email": "bad-email",
        "password": "123",
        "full_name": "",
    })
    assert response.status_code == 422


def test_login_success(client, test_user):
    response = client.post("/auth/login", json={
        "email": test_user["email"],
        "password": "password123",
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client, test_user):
    response = client.post("/auth/login", json={
        "email": test_user["email"],
        "password": "wrongpassword!",
    })
    assert response.status_code == 401


def test_profile_get_with_token(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    response = client.get("/auth/profile", headers=headers)
    assert response.status_code == 200
    assert response.json()["email"] == test_user["email"]


def test_profile_get_without_token(client):
    response = client.get("/auth/profile")
    assert response.status_code == 401


def test_token_refresh(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    response = client.post("/auth/refresh", json={"refresh_token": test_user["refresh_token"]})
    if response.status_code != 404:
        assert response.status_code == 200
        assert "access_token" in response.json()


def test_logout(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    response = client.post("/auth/logout", headers=headers)
    assert response.status_code == 200
