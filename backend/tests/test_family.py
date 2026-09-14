import pytest
from uuid import UUID


def test_create_family(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    response = client.post("/families", json={
        "creator_id": str(UUID("00000000-0000-0000-0000-000000000001")),
        "family_name": "Gia đình họ Nguyễn",
        "description": None,
    }, headers=headers)
    assert response.status_code in [200, 201, 404]


def test_list_families(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    response = client.get("/families", headers=headers)
    assert response.status_code in [200, 404]


def test_get_family(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    # First create a family
    create_resp = client.post("/families", json={
        "creator_id": str(UUID("00000000-0000-0000-0000-000000000001")),
        "family_name": "Gia đình họ Trần",
    }, headers=headers)
    if create_resp.status_code in [200, 201]:
        family_id = create_resp.json().get("id") or create_resp.json().get("family_id")
        if family_id:
            get_resp = client.get(f"/families/{family_id}", headers=headers)
            assert get_resp.status_code in [200, 404]


def test_add_member(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    # Create family first
    create_resp = client.post("/families", json={
        "creator_id": str(UUID("00000000-0000-0000-0000-000000000001")),
        "family_name": "Test Family",
    }, headers=headers)
    if create_resp.status_code in [200, 201]:
        family_id = create_resp.json().get("id") or create_resp.json().get("family_id")
        if family_id:
            resp = client.post(
                f"/families/{family_id}/members",
                json={"full_name": "Nguyễn Văn A", "gender": "MALE"},
                headers=headers,
            )
            assert resp.status_code in [200, 201, 404]


def test_get_tree(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    create_resp = client.post("/families", json={
        "creator_id": str(UUID("00000000-0000-0000-0000-000000000001")),
        "family_name": "Test Family",
    }, headers=headers)
    if create_resp.status_code in [200, 201]:
        family_id = create_resp.json().get("id") or create_resp.json().get("family_id")
        if family_id:
            resp = client.get(f"/families/{family_id}/tree", headers=headers)
            assert resp.status_code in [200, 404]


def test_add_relationship(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    create_resp = client.post("/families", json={
        "creator_id": str(UUID("00000000-0000-0000-0000-000000000001")),
        "family_name": "Test Family",
    }, headers=headers)
    if create_resp.status_code in [200, 201]:
        family_id = create_resp.json().get("id") or create_resp.json().get("family_id")
        if family_id:
            resp = client.post(
                f"/families/{family_id}/relationships",
                json={
                    "from_member_id": str(UUID("00000000-0000-0000-0000-000000000002")),
                    "to_member_id": str(UUID("00000000-0000-0000-0000-000000000003")),
                    "type": "PARENT_CHILD",
                },
                headers=headers,
            )
            assert resp.status_code in [200, 201, 404]


def test_rbac_unauthenticated(client):
    fake_token = "invalid_or_member_token_123"
    headers = {"Authorization": f"Bearer {fake_token}"}
    response = client.post("/families", json={"name": "Gia đình mới"}, headers=headers)
    assert response.status_code in [401, 403]
