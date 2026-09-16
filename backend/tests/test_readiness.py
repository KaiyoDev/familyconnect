"""Regression tests: frontend-readiness endpoints (backend ↔ frontend contract).

Covers the P0/P1/P2 gap fixes: family branches/members/relationships CRUD,
join & transfer-ownership, event remind/gallery/export, user password/avatar,
AI messages, notifications, analytics & reports, admin surface.
"""
import io
import uuid

import pytest


def _make_family(client, headers):
    resp = client.post("/families", json={"name": f"Readiness {uuid.uuid4().hex[:6]}"}, headers=headers)
    assert resp.status_code == 201, resp.text
    return resp.json()["data"]["id"]


def _make_member(client, headers, family_id, name="M", gender="MALE"):
    resp = client.post(f"/families/{family_id}/members",
                       json={"full_name": name, "gender": gender, "date_of_birth": "1980-01-01"},
                       headers=headers)
    assert resp.status_code == 201, resp.text
    return resp.json()["data"]["id"]


@pytest.fixture
def auth(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    family_id = _make_family(client, headers)
    return client, headers, family_id


# ── Family branches ──────────────────────────────────────────────

def test_branches_list(auth):
    client, headers, family_id = auth
    r = client.get(f"/families/{family_id}/branches", headers=headers)
    assert r.status_code == 200
    assert isinstance(r.json()["data"], list)


def test_branch_update_delete(auth):
    client, headers, family_id = auth
    branches = client.get(f"/families/{family_id}/branches", headers=headers).json()["data"]
    bid = branches[0]["id"]
    r = client.put(f"/families/{family_id}/branches/{bid}", json={"name": "Renamed"}, headers=headers)
    assert r.status_code == 200
    assert client.delete(f"/families/{family_id}/branches/{bid}", headers=headers).status_code == 204


# ── Members ────────────────────────────────────────────────────────

def test_member_update(auth):
    client, headers, family_id = auth
    mid = _make_member(client, headers, family_id, "MemberA")
    r = client.put(f"/families/{family_id}/members/{mid}", json={"status": "ACTIVE"}, headers=headers)
    assert r.status_code == 200
    assert r.json()["data"]["status"] == "ACTIVE"


def test_member_delete(auth):
    client, headers, family_id = auth
    mid = _make_member(client, headers, family_id, "MemberD")
    assert client.delete(f"/families/{family_id}/members/{mid}", headers=headers).status_code == 204


# ── Relationships ──────────────────────────────────────────────────

def test_relationship_full_cycle(auth):
    client, headers, family_id = auth
    m1 = _make_member(client, headers, family_id, "R1")
    m2 = _make_member(client, headers, family_id, "R2")
    r = client.post(f"/families/{family_id}/relationships",
                    json={"member_a_id": m1, "member_b_id": m2, "relationship_type": "MARRIAGE"},
                    headers=headers)
    assert r.status_code == 201, r.text
    rid = r.json()["data"]["id"]
    assert client.put(f"/families/{family_id}/relationships/{rid}",
                      json={"relationship_type": "PARENT_CHILD"}, headers=headers).status_code == 200
    lookup = client.post(f"/families/{family_id}/relationships/lookup",
                         json={"member_a_id": m1, "member_b_id": m2}, headers=headers)
    assert lookup.status_code == 200
    explain = client.post(f"/families/{family_id}/relationships/explain",
                          json={"member_a_id": m1, "member_b_id": m2, "relationship_type": "MARRIAGE"},
                          headers=headers)
    assert explain.status_code == 200
    assert explain.json()["data"]["explanation"]
    assert client.delete(f"/families/{family_id}/relationships/{rid}", headers=headers).status_code == 204


# ── Join / transfer-ownership (tolerant, no model yet) ────────────

def test_family_join_tolerant(auth):
    client, headers, _ = auth
    r = client.post("/families/join", json={"join_code": "CODE-123"}, headers=headers)
    assert r.status_code == 200


def test_transfer_ownership_tolerant(auth):
    client, headers, family_id = auth
    m1 = _make_member(client, headers, family_id, "Owner")
    r = client.post(f"/families/{family_id}/transfer-ownership", json={"new_owner_id": m1}, headers=headers)
    assert r.status_code == 200


# ── Events: remind / gallery / export ─────────────────────────────

def _make_event(client, headers, family_id):
    r = client.post(f"/families/{family_id}/events",
                    json={"title": "Evt", "start_time": "2030-01-01T10:00:00"}, headers=headers)
    assert r.status_code == 201, r.text
    return r.json()["data"]["event_id"]


def test_event_remind(auth):
    client, headers, family_id = auth
    eid = _make_event(client, headers, family_id)
    r = client.post(f"/events/{eid}/remind", headers=headers)
    assert r.status_code == 200
    assert "message" in r.json()["data"]


def test_event_gallery(auth):
    client, headers, family_id = auth
    eid = _make_event(client, headers, family_id)
    assert client.get(f"/events/{eid}/gallery", headers=headers).status_code == 200
    files = {"file": ("p.jpg", io.BytesIO(b"x"), "image/jpeg")}
    r = client.post(f"/events/{eid}/gallery", files=files, headers=headers)
    assert r.status_code == 201
    assert r.json()["data"]["url"]
    assert len(client.get(f"/events/{eid}/gallery", headers=headers).json()["data"]) == 1


def test_event_export(auth):
    client, headers, family_id = auth
    eid = _make_event(client, headers, family_id)
    r = client.get(f"/events/{eid}/export", headers=headers)
    assert r.status_code == 200
    assert "attachment" in r.headers.get("content-disposition", "")


# ── User: password / avatar ──────────────────────────────────────

def test_user_change_password(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    r = client.put("/users/me/password",
                   json={"current_password": "password123", "new_password": "newpassword456"},
                   headers=headers)
    assert r.status_code == 200, r.text
    # wrong current password is rejected
    bad = client.put("/users/me/password",
                     json={"current_password": "WRONG", "new_password": "whatever123"},
                     headers=headers)
    assert bad.status_code == 400
    # restore the shared test user's password so later fixtures can log in
    client.put("/users/me/password",
               json={"current_password": "newpassword456", "new_password": "password123"},
               headers=headers)


def test_user_avatar_tolerant(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    files = {"file": ("a.png", io.BytesIO(b"x"), "image/png")}
    r = client.post("/users/me/avatar", files=files, headers=headers)
    assert r.status_code == 200


# ── AI messages ───────────────────────────────────────────────────

def test_ai_conversation_messages(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    c = client.post("/ai/conversations", json={"title": "t"}, headers=headers)
    assert c.status_code == 201, c.text
    cid = c.json()["data"]["id"]
    r = client.get(f"/ai/conversations/{cid}/messages", headers=headers)
    assert r.status_code == 200
    assert isinstance(r.json()["data"], list)


# ── Notifications ─────────────────────────────────────────────────

def test_notifications_endpoints(client, test_user):
    headers = {"Authorization": f"Bearer {test_user['token']}"}
    assert client.get("/notifications", headers=headers).status_code == 200
    assert isinstance(client.get("/notifications", headers=headers).json()["data"], list)
    r = client.put("/notifications/read-all", headers=headers)
    assert r.status_code == 200
    assert "message" in r.json()["data"]
    assert client.get("/notifications/settings", headers=headers).status_code == 200
    assert client.put("/notifications/settings", json={"email_notifications": False},
                      headers=headers).status_code == 200


# ── Analytics / reports ───────────────────────────────────────────

def test_family_analytics(auth):
    client, headers, family_id = auth
    r = client.get(f"/families/{family_id}/analytics", headers=headers)
    assert r.status_code == 200
    assert "total_members" in r.json()["data"]


def test_family_demographics(auth):
    client, headers, family_id = auth
    _make_member(client, headers, family_id, "Demo", "MALE")
    r = client.get(f"/families/{family_id}/analytics/demographics", headers=headers)
    assert r.status_code == 200
    assert "age" in r.json()["data"]


def test_family_analytics_events(auth):
    client, headers, family_id = auth
    _make_event(client, headers, family_id)
    r = client.get(f"/families/{family_id}/analytics/events", headers=headers)
    assert r.status_code == 200
    assert "terms" in r.json()["data"]


def test_reports_flow(auth):
    client, headers, family_id = auth
    r = client.post(f"/families/{family_id}/reports", headers=headers)
    assert r.status_code == 201, r.text
    rid = r.json()["data"]["id"]
    assert client.get(f"/families/{family_id}/reports/{rid}", headers=headers).status_code == 200
    assert client.get(f"/families/{family_id}/reports/{rid}/export", headers=headers).status_code == 200


def test_analytics_unknown_family_404(auth):
    client, headers, _ = auth
    r = client.get("/families/00000000-0000-4000-8000-000000000001/analytics", headers=headers)
    assert r.status_code == 404


# ── Admin surface (protected — expect 403 for normal user) ───────

def test_admin_protected(auth):
    client, headers, _ = auth
    for path in ("/admin/users", "/admin/moderation", "/admin/backups", "/admin/audit-log"):
        assert client.get(path, headers=headers).status_code == 403, path
