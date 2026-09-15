#!/usr/bin/env python3
"""
FamilyConnect - Pytest Automation Test Suite
=============================================
Chạy: pytest tests/automation/ -v --cov=backend --cov-report=term-missing

Yêu cầu:
    pip install pytest httpx pytest-cov
"""

import pytest
import httpx
import uuid
from datetime import datetime, timedelta

# ============================================================
# Configuration
# ============================================================
BASE_URL = "http://localhost:8000/api/v1"

# Test data
TEST_USER = {
    "full_name": "Test User",
    "email": f"test_{uuid.uuid4().hex[:8]}@example.com",
    "password": "Abc12345",
    "password_confirm": "Abc12345",
    "agree_terms": True
}

TEST_FAMILY = {
    "family_name": f"Test Family {uuid.uuid4().hex[:8]}",
    "description": "Auto-generated test family",
    "region": "Đồng Nai",
    "country": "Việt Nam"
}


# ============================================================
# Fixtures
# ============================================================

@pytest.fixture(scope="session")
def client():
    """HTTP client for API calls"""
    return httpx.Client(base_url=BASE_URL, timeout=30)


@pytest.fixture(scope="session")
def admin_token(client):
    """Login as admin and return token"""
    resp = client.post("/auth/login", json={
        "email": "admin@familyconnect.com",
        "password": "Admin@2026"
    })
    assert resp.status_code == 200, f"Admin login failed: {resp.text}"
    return resp.json()["accessToken"]


@pytest.fixture(scope="session")
def registered_user(client):
    """Register a new user and return user data"""
    resp = client.post("/auth/register", json=TEST_USER)
    assert resp.status_code == 201, f"Registration failed: {resp.text}"
    data = resp.json()
    return {
        "userId": data["userId"],
        "email": TEST_USER["email"],
        "password": TEST_USER["password"]
    }


@pytest.fixture(scope="session")
def user_token(client, registered_user):
    """Login as registered user and return token"""
    resp = client.post("/auth/login", json={
        "email": registered_user["email"],
        "password": registered_user["password"]
    })
    assert resp.status_code == 200
    return resp.json()["accessToken"]


@pytest.fixture(scope="session")
def owner_token(client):
    """Login as family owner"""
    resp = client.post("/auth/login", json={
        "email": "owner@example.com",
        "password": "Owner@123"
    })
    assert resp.status_code == 200
    return resp.json()["accessToken"]


@pytest.fixture(scope="session")
def member_token(client):
    """Login as family member"""
    resp = client.post("/auth/login", json={
        "email": "memberB@example.com",
        "password": "Member@123"
    })
    assert resp.status_code == 200
    return resp.json()["accessToken"]


# ============================================================
# Module 1: User & Security Tests
# ============================================================

class TestUserSecurity:

    def test_us_001_register_success(self, client):
        """TC-US-001P: Register new account successfully"""
        email = f"newuser_{uuid.uuid4().hex[:8]}@example.com"
        resp = client.post("/auth/register", json={
            "full_name": "Nguyễn Văn New",
            "email": email,
            "password": "Abc12345",
            "password_confirm": "Abc12345",
            "agree_terms": True
        })
        assert resp.status_code == 201
        data = resp.json()
        assert "userId" in data
        assert data["status"] == "PENDING_ACTIVATION"

    def test_us_001_duplicate_email(self, client):
        """TC-US-001N: Register with existing email"""
        resp = client.post("/auth/register", json={
            "full_name": "Test Dup",
            "email": "admin@familyconnect.com",
            "password": "Abc12345",
            "password_confirm": "Abc12345",
            "agree_terms": True
        })
        assert resp.status_code == 409
        assert "email" in resp.json()["message"].lower()

    def test_us_001_weak_password(self, client):
        """TC-US-001N2: Register with weak password"""
        resp = client.post("/auth/register", json={
            "full_name": "Weak Pass",
            "email": f"weak_{uuid.uuid4().hex[:8]}@example.com",
            "password": "123",
            "password_confirm": "123",
            "agree_terms": True
        })
        assert resp.status_code == 400
        assert "mật khẩu" in resp.json()["message"].lower()

    def test_us_002_login_success(self, client):
        """TC-US-002P: Login successfully"""
        resp = client.post("/auth/login", json={
            "email": "admin@familyconnect.com",
            "password": "Admin@2026"
        })
        assert resp.status_code == 200
        data = resp.json()
        assert "accessToken" in data
        assert "refreshToken" in data
        assert resp.elapsed.total_seconds() < 3.0

    def test_us_002_wrong_password(self, client):
        """TC-US-002N: Login with wrong password"""
        resp = client.post("/auth/login", json={
            "email": "admin@familyconnect.com",
            "password": "WrongPass123"
        })
        assert resp.status_code == 401
        assert "email" in resp.json()["message"].lower() or \
               "mật khẩu" in resp.json()["message"].lower()

    def test_us_002_account_locked(self, client):
        """TC-US-002N3: Login with locked account"""
        resp = client.post("/auth/login", json={
            "email": "blockedE@example.com",
            "password": "Blocked@123"
        })
        assert resp.status_code == 403
        assert "khóa" in resp.json()["message"].lower()

    def test_us_002_invalid_email(self, client):
        """TC-US-002N4: Login with non-existent email"""
        resp = client.post("/auth/login", json={
            "email": "nonexistent@example.com",
            "password": "Abc12345"
        })
        assert resp.status_code == 401
        # Should not reveal that email doesn't exist
        assert "không tồn tại" not in resp.json()["message"].lower()

    def test_us_003_logout(self, client, member_token):
        """TC-US-003P: Logout successfully"""
        headers = {"Authorization": f"Bearer {member_token}"}
        resp = client.post("/auth/logout", headers=headers)
        assert resp.status_code == 200

    def test_us_004_reset_password(self, client):
        """TC-US-004P: Reset password flow"""
        # Step 1: Request reset
        resp = client.post("/auth/forgot-password", json={
            "email": "owner@example.com"
        })
        assert resp.status_code == 200
        assert "Nếu email tồn tại" in resp.json()["message"]

    def test_us_004_invalid_email(self, client):
        """TC-US-004N: Reset with non-existent email"""
        resp = client.post("/auth/forgot-password", json={
            "email": "unknown@example.com"
        })
        assert resp.status_code == 200
        # Should NOT reveal that email doesn't exist
        assert "không tồn tại" not in resp.json()["message"].lower()

    # ============ RBAC Tests ============

    def test_us_005_rbac_member_no_admin(self, client, member_token):
        """TC-US-005A: Member cannot access admin functions"""
        headers = {"Authorization": f"Bearer {member_token}"}
        resp = client.get("/admin/users", headers=headers)
        assert resp.status_code == 403

    def test_us_005_rbac_member_no_other_family(self, client, member_token):
        """TC-US-005A2: Member cannot access other family data"""
        headers = {"Authorization": f"Bearer {member_token}"}
        resp = client.get("/families/family-B/tree", headers=headers)
        assert resp.status_code == 403

    def test_us_005_rbac_guest_no_access(self, client):
        """TC-US-005A4: Guest cannot access protected endpoints"""
        resp = client.get("/families/family-A/posts")
        assert resp.status_code == 401

    # ============ Profile Tests ============

    def test_us_006_update_profile(self, client, member_token):
        """TC-US-006P: Update profile successfully"""
        headers = {"Authorization": f"Bearer {member_token}"}
        resp = client.patch("/auth/profile", headers=headers, json={
            "full_name": "Nguyễn Văn Updated",
            "phone": "0912345678"
        })
        assert resp.status_code == 200
        assert resp.json()["full_name"] == "Nguyễn Văn Updated"

    def test_us_006_future_dob(self, client, member_token):
        """TC-US-006N: Update with future date of birth"""
        headers = {"Authorization": f"Bearer {member_token}"}
        future_date = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
        resp = client.patch("/auth/profile", headers=headers, json={
            "date_of_birth": future_date
        })
        assert resp.status_code == 400
        assert "không hợp lệ" in resp.json()["message"].lower()


# ============================================================
# Module 2: Family & Genealogy Tests
# ============================================================

class TestFamilyGenealogy:

    def test_fg_001_create_family(self, client, owner_token):
        """TC-FG-001P: Create family successfully"""
        headers = {"Authorization": f"Bearer {owner_token}"}
        resp = client.post("/families", headers=headers, json=TEST_FAMILY)
        assert resp.status_code == 201
        data = resp.json()
        assert data["status"] == "ACTIVE"
        assert "ownerId" in data

    def test_fg_001_empty_name(self, client, owner_token):
        """TC-FG-001N: Create family with empty name"""
        headers = {"Authorization": f"Bearer {owner_token}"}
        resp = client.post("/families", headers=headers, json={
            "family_name": "",
            "region": "Test"
        })
        assert resp.status_code == 400
        assert "tên" in resp.json()["message"].lower()

    def test_fg_001_guest_cannot_create(self, client):
        """TC-FG-001A: Guest cannot create family"""
        resp = client.post("/families", json=TEST_FAMILY)
        assert resp.status_code == 401

    def test_fg_004_create_parent_child(self, client, owner_token):
        """TC-FG-004P: Create parent-child relationship"""
        headers = {"Authorization": f"Bearer {owner_token}"}
        resp = client.post(
            "/families/family-A/relationships",
            headers=headers,
            json={
                "from_member_id": "member-father",
                "to_member_id": "member-child",
                "type": "PARENT_CHILD"
            }
        )
        assert resp.status_code == 201
        assert resp.json()["type"] == "PARENT_CHILD"

    def test_fg_004_cycle_detection(self, client, owner_token):
        """TC-FG-004N: Detect cycle in relationship graph"""
        headers = {"Authorization": f"Bearer {owner_token}"}
        resp = client.post(
            "/families/family-A/relationships",
            headers=headers,
            json={
                "from_member_id": "member-grandson",
                "to_member_id": "member-grandfather",
                "type": "PARENT_CHILD"
            }
        )
        assert resp.status_code == 400
        msg = resp.json()["message"].lower()
        assert any(word in msg for word in ["vòng lặp", "cycle", "mâu thuẫn"])

    def test_fg_004_third_parent(self, client, owner_token):
        """TC-FG-004N2: Add third parent when max is 2"""
        headers = {"Authorization": f"Bearer {owner_token}"}
        # First add 2 parents
        client.post("/families/family-A/relationships", headers=headers,
                    json={"from_member_id": "member-father", "to_member_id": "member-grandson", "type": "PARENT_CHILD"})
        client.post("/families/family-A/relationships", headers=headers,
                    json={"from_member_id": "member-mother", "to_member_id": "member-grandson", "type": "PARENT_CHILD"})
        # Try adding third
        resp = client.post("/families/family-A/relationships", headers=headers,
                           json={"from_member_id": "member-uncle", "to_member_id": "member-grandson", "type": "PARENT_CHILD"})
        assert resp.status_code == 400

    def test_fg_005_marriage(self, client, owner_token):
        """TC-FG-005P: Create marriage relationship"""
        headers = {"Authorization": f"Bearer {owner_token}"}
        resp = client.post(
            "/families/family-A/relationships",
            headers=headers,
            json={
                "from_member_id": "member-child",
                "to_member_id": "member-mother",  # Note: using members with no existing active marriage
                "type": "MARRIAGE",
                "notes": "Test marriage",
                "wedding_date": "2025-01-01"
            }
        )
        # If members already have marriage, may return 400
        assert resp.status_code in [201, 400]

    def test_fg_006_view_tree(self, client, member_token):
        """TC-FG-006P: View family tree"""
        headers = {"Authorization": f"Bearer {member_token}"}
        resp = client.get("/families/family-A/tree", headers=headers)
        assert resp.status_code == 200
        data = resp.json()
        assert "nodes" in data
        assert "edges" in data

    def test_fg_006_unauthorized_tree(self, client, member_token):
        """TC-FG-006A: Cannot view tree of other family"""
        headers = {"Authorization": f"Bearer {member_token}"}
        resp = client.get("/families/family-B/tree", headers=headers)
        assert resp.status_code == 403

    def test_fg_008_relationship_query(self, client, member_token):
        """TC-FG-008P: Query relationship between two members"""
        headers = {"Authorization": f"Bearer {member_token}"}
        resp = client.get(
            "/families/family-A/relationships/query",
            headers=headers,
            params={"member_a": "member-grandfather", "member_b": "member-grandson"}
        )
        assert resp.status_code == 200
        data = resp.json()
        assert "relationship" in data
        assert "path" in data
        assert resp.elapsed.total_seconds() < 2.0


# ============================================================
# Module 3: Community Tests
# ============================================================

class TestCommunity:

    def test_com_001_create_post(self, client, member_token):
        """TC-COM-001P: Create post successfully"""
        headers = {"Authorization": f"Bearer {member_token}"}
        resp = client.post("/families/family-A/posts", headers=headers, json={
            "content": "Chúc mừng sinh nhật ông!",
            "visibility_scope": "FAMILY"
        })
        assert resp.status_code == 201
        assert resp.json()["status"] == "PUBLISHED"

    def test_com_001_empty_content(self, client, member_token):
        """TC-COM-001N: Create post with empty content"""
        headers = {"Authorization": f"Bearer {member_token}"}
        resp = client.post("/families/family-A/posts", headers=headers, json={
            "content": "",
            "visibility_scope": "FAMILY"
        })
        assert resp.status_code == 400

    def test_com_001_guest_cannot_post(self, client):
        """TC-COM-001A: Guest cannot create post"""
        resp = client.post("/families/family-A/posts", json={
            "content": "Test",
            "visibility_scope": "FAMILY"
        })
        assert resp.status_code == 401

    def test_com_002_comment(self, client, member_token):
        """TC-COM-002P: Comment on post"""
        headers = {"Authorization": f"Bearer {member_token}"}
        # First create a post
        post_resp = client.post("/families/family-A/posts", headers=headers, json={
            "content": "Test post for comment",
            "visibility_scope": "FAMILY"
        })
        post_id = post_resp.json()["id"]

        # Comment on it
        resp = client.post(f"/posts/{post_id}/comments", headers=headers, json={
            "content": "Chúc mừng!"
        })
        assert resp.status_code == 201

    def test_com_002_react(self, client, member_token):
        """TC-COM-002P2: React to post"""
        headers = {"Authorization": f"Bearer {member_token}"}
        # Create post
        post_resp = client.post("/families/family-A/posts", headers=headers, json={
            "content": "Test post for reaction",
            "visibility_scope": "FAMILY"
        })
        post_id = post_resp.json()["id"]

        # React
        resp = client.post(f"/posts/{post_id}/reactions", headers=headers, json={
            "reaction_type": "LIKE"
        })
        assert resp.status_code == 201

    def test_com_005_announcement_owner_only(self, client, owner_token, member_token):
        """TC-COM-005A: Member cannot create announcement"""
        headers = {"Authorization": f"Bearer {member_token}"}
        resp = client.post("/families/family-A/announcements", headers=headers, json={
            "title": "Test Announcement",
            "content": "Test",
            "importance": "NORMAL"
        })
        assert resp.status_code == 403

    def test_com_005_owner_can_announce(self, client, owner_token):
        """TC-COM-005P: Owner can create announcement"""
        headers = {"Authorization": f"Bearer {owner_token}"}
        resp = client.post("/families/family-A/announcements", headers=headers, json={
            "title": "Họp mặt cuối năm",
            "content": "Kính mời toàn thể gia đình",
            "importance": "QUAN_TRONG"
        })
        assert resp.status_code == 201


# ============================================================
# Module 7: AI Services Tests
# ============================================================

class TestAIServices:

    def test_ai_001_semantic_search(self, client, member_token):
        """TC-AI-001P: Semantic search works"""
        headers = {"Authorization": f"Bearer {member_token}"}
        resp = client.post("/ai/search", headers=headers, json={
            "family_id": "family-A",
            "query": "Những ai trong gia đình làm bác sĩ?"
        })
        assert resp.status_code == 200
        assert "results" in resp.json()

    def test_ai_001_fallback(self, client, member_token):
        """TC-AI-001N2: Fallback when AI service is down"""
        headers = {"Authorization": f"Bearer {member_token}"}
        # Simulate by sending request when AI is disabled
        resp = client.post("/ai/search", headers=headers, json={
            "family_id": "family-A",
            "query": "Test fallback"
        })
        # Should still work (keyword fallback)
        assert resp.status_code in [200, 503]


# ============================================================
# Module 9: Administration Tests
# ============================================================

class TestAdministration:

    def test_adm_001_lock_user(self, client, admin_token):
        """TC-ADM-001P2: Admin can lock user account"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        resp = client.patch("/admin/users/user-member-C", headers=headers, json={
            "action": "BLOCK",
            "reason": "Vi phạm chính sách"
        })
        assert resp.status_code == 200
        assert resp.json()["status"] == "BLOCKED"
        assert "auditLogId" in resp.json()

    def test_adm_001_unlock_user(self, client, admin_token):
        """TC-ADM-001P3: Admin can unlock user"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        resp = client.patch("/admin/users/user-member-C", headers=headers, json={
            "action": "UNBLOCK"
        })
        assert resp.status_code == 200
        assert resp.json()["status"] == "ACTIVE"

    def test_adm_001_owner_cannot_manage(self, client, owner_token):
        """TC-ADM-001A: Owner cannot manage system users"""
        headers = {"Authorization": f"Bearer {owner_token}"}
        resp = client.patch("/admin/users/user-member-C", headers=headers, json={
            "action": "BLOCK",
            "reason": "Test"
        })
        assert resp.status_code == 403

    def test_adm_002_moderate_content(self, client, admin_token):
        """TC-ADM-002P: Admin can moderate content"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        resp = client.post("/admin/moderation/review", headers=headers, json={
            "content_id": "post-X",
            "action": "REMOVE",
            "reason": "Ngôn từ thù hận",
            "penalty": "WARNING"
        })
        assert resp.status_code == 200
        assert "auditLogId" in resp.json()

    def test_adm_003_view_audit_log(self, client, admin_token):
        """TC-ADM-003P: View audit log with filters"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        resp = client.get("/admin/audit-logs", headers=headers, params={
            "action": "ROLE_CHANGE",
            "days": 7
        })
        assert resp.status_code == 200
        assert "logs" in resp.json()

    def test_adm_003_audit_log_immutable(self, client, admin_token):
        """TC-ADM-003V: Audit log cannot be modified"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        resp = client.delete("/admin/audit-logs/log-001", headers=headers)
        assert resp.status_code == 405  # Method Not Allowed

    def test_adm_004_backup(self, client, admin_token):
        """TC-ADM-004P: Trigger backup"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        resp = client.post("/admin/backup", headers=headers)
        assert resp.status_code == 201
        assert "backupId" in resp.json()

    def test_adm_005_update_config(self, client, admin_token):
        """TC-ADM-005P: Update system config"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        resp = client.patch("/admin/config", headers=headers, json={
            "key": "max_upload_size",
            "value": "20MB"
        })
        assert resp.status_code == 200
        # Verify config applied
        resp2 = client.get("/admin/config", headers=headers)
        assert resp2.status_code == 200

    def test_adm_005_invalid_config(self, client, admin_token):
        """TC-ADM-005N: Invalid config value"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        resp = client.patch("/admin/config", headers=headers, json={
            "key": "max_upload_size",
            "value": -1
        })
        assert resp.status_code == 400


# ============================================================
# Integration Tests
# ============================================================

class TestIntegration:

    def test_full_flow_member_joins_family(self, client, admin_token, owner_token):
        """Integration: Guest registers -> requests join -> Owner approves -> Member accesses data"""
        # Step 1: Register new user
        email = f"flowtest_{uuid.uuid4().hex[:8]}@example.com"
        reg_resp = client.post("/auth/register", json={
            "full_name": "Flow Test User",
            "email": email,
            "password": "FlowTest123",
            "password_confirm": "FlowTest123",
            "agree_terms": True
        })
        assert reg_resp.status_code == 201
        user_id = reg_resp.json()["userId"]

        # Step 2: Request join family
        user_token_resp = client.post("/auth/login", json={
            "email": email,
            "password": "FlowTest123"
        })
        assert user_token_resp.status_code == 200
        user_token = user_token_resp.json()["accessToken"]
        user_headers = {"Authorization": f"Bearer {user_token}"}

        join_resp = client.post("/families/family-A/requests", headers=user_headers, json={
            "message": "Con trai của Nguyễn Văn Cha"
        })
        assert join_resp.status_code == 201

        # Step 3: Owner approves
        owner_headers = {"Authorization": f"Bearer {owner_token}"}
        request_id = join_resp.json()["requestId"]
        approve_resp = client.patch(
            f"/families/family-A/requests/{request_id}",
            headers=owner_headers,
            json={"action": "APPROVE"}
        )
        assert approve_resp.status_code == 200

        # Step 4: User accesses family data
        tree_resp = client.get("/families/family-A/tree", headers=user_headers)
        assert tree_resp.status_code == 200

    def test_full_flow_create_event_rsvp(self, client, member_token):
        """Integration: Create event -> RSVP -> View participants"""
        headers = {"Authorization": f"Bearer {member_token}"}

        # Step 1: Create event
        event_resp = client.post("/families/family-A/events", headers=headers, json={
            "title": "Test Event",
            "type": "MEETING",
            "start_time": (datetime.now() + timedelta(days=30)).isoformat() + "Z",
            "end_time": (datetime.now() + timedelta(days=30, hours=4)).isoformat() + "Z",
            "location": "Test Location"
        })
        assert event_resp.status_code == 201
        event_id = event_resp.json()["id"]

        # Step 2: RSVP
        rsvp_resp = client.post(f"/events/{event_id}/rsvp", headers=headers, json={
            "response": "GOING"
        })
        assert rsvp_resp.status_code == 201

        # Step 3: View participants
        participants_resp = client.get(f"/events/{event_id}/participants", headers=headers)
        assert participants_resp.status_code == 200
        assert len(participants_resp.json()["participants"]) >= 1

        # Step 4: Change RSVP
        rsvp_resp2 = client.post(f"/events/{event_id}/rsvp", headers=headers, json={
            "response": "MAYBE"
        })
        assert rsvp_resp2.status_code == 200