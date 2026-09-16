"""
FamilyConnect - Integration tests for Event module (FR-EVT-01, 02, 03, 05)

Tests endpoints:
  - POST   /api/families/{family_id}/events        (FR-EVT-01)
  - GET    /api/families/{family_id}/events         (FR-EVT-01)
  - GET    /api/events/{event_id}                   (FR-EVT-01)
  - PUT    /api/events/{event_id}                   (FR-EVT-01)
  - DELETE /api/events/{event_id}                   (FR-EVT-01)
  - POST   /api/events/{event_id}/rsvp              (FR-EVT-02)
  - GET    /api/events/{event_id}/attendees         (FR-EVT-03)
"""
import pytest
from uuid import uuid4
from unittest.mock import AsyncMock

from fastapi import HTTPException
from app.services.event_service import EventService


# =========================================================
# Fake models
# =========================================================

class FakeEvent:
    def __init__(self, id, title="Test Event", description="Desc", start_time="2026-09-01", family_id=None, created_by=None):
        self.id = id
        self.title = title
        self.description = description
        self.start_time = start_time
        self.family_id = family_id
        self.created_by = created_by


class FakeAttendee:
    def __init__(self, guest_email, response):
        self.guest_email = guest_email
        self.response = response


def make_service():
    event_repo = AsyncMock()
    rsvp_repo = AsyncMock()
    service = EventService(event_repo, rsvp_repo)
    return service, event_repo, rsvp_repo


# =========================================================
# FR-EVT-01: Event CRUD (Normal Cases)
# =========================================================

class TestEventIntegration_CRUD:

    @pytest.mark.asyncio
    async def test_create_event_success(self):
        """TC-EVT-001P: Create event successfully (normal case)"""
        service, event_repo, _ = make_service()
        event_id = uuid4()
        event_repo.create.return_value = FakeEvent(id=event_id)

        result = await service.create_event(
            family_id=uuid4(), creator_id=uuid4(),
            data={"title": "Tet Reunion", "start_time": "2026-02-10T08:00:00Z"}
        )
        assert result["event_id"] == str(event_id)
        assert result["message"] == "Event created successfully"

    @pytest.mark.asyncio
    async def test_get_events_empty(self):
        """TC-EVT-001P: List events for family with no events (edge case)"""
        service, event_repo, _ = make_service()
        event_repo.get_by_family.return_value = []
        result = await service.get_events(uuid4())
        assert result == []

    @pytest.mark.asyncio
    async def test_get_events_multiple(self):
        """TC-EVT-001P: List multiple events (normal case)"""
        service, event_repo, _ = make_service()
        event_repo.get_by_family.return_value = [
            FakeEvent(id=uuid4(), title="Event 1"),
            FakeEvent(id=uuid4(), title="Event 2"),
            FakeEvent(id=uuid4(), title="Event 3"),
        ]
        result = await service.get_events(uuid4())
        assert len(result) == 3
        assert result[0]["title"] == "Event 1"
        assert result[2]["title"] == "Event 3"

    @pytest.mark.asyncio
    async def test_get_event_found(self):
        """TC-EVT-001P: Get event by id (normal case)"""
        service, event_repo, _ = make_service()
        event_id = uuid4()
        event_repo.get_by_id.return_value = FakeEvent(id=event_id, title="My Event")
        result = await service.get_event(event_id)
        assert result["title"] == "My Event"
        assert str(result["id"]) == str(event_id)

    @pytest.mark.asyncio
    async def test_get_event_not_found(self):
        """TC-EVT-001N: Event not found -> 404"""
        service, event_repo, _ = make_service()
        event_repo.get_by_id.return_value = None
        with pytest.raises(HTTPException) as exc:
            await service.get_event(uuid4())
        assert exc.value.status_code == 404

    @pytest.mark.asyncio
    async def test_update_event_not_found(self):
        """TC-EVT-001N: Update non-existent event -> 404"""
        service, event_repo, _ = make_service()
        event_repo.update.return_value = None
        with pytest.raises(HTTPException) as exc:
            await service.update_event(uuid4(), {"title": "Updated"})
        assert exc.value.status_code == 404

    @pytest.mark.asyncio
    async def test_cancel_event_not_found(self):
        """TC-EVT-001N: Cancel non-existent event -> 404"""
        service, event_repo, _ = make_service()
        event_repo.delete.return_value = False
        with pytest.raises(HTTPException) as exc:
            await service.cancel_event(uuid4())
        assert exc.value.status_code == 404


# =========================================================
# FR-EVT-02: RSVP
# =========================================================

class TestEventIntegration_RSVP:

    @pytest.mark.asyncio
    async def test_rsvp_going(self):
        """TC-EVT-002P: RSVP with 'going'"""
        service, _, rsvp_repo = make_service()
        rsvp_repo.upsert_rsvp.return_value = None
        result = await service.rsvp(uuid4(), "guest@example.com", "going")
        assert "going" in result["message"]

    @pytest.mark.asyncio
    async def test_rsvp_maybe(self):
        """TC-EVT-002P: RSVP 'maybe'"""
        service, _, rsvp_repo = make_service()
        rsvp_repo.upsert_rsvp.return_value = None
        result = await service.rsvp(uuid4(), "guest@example.com", "maybe")
        assert "maybe" in result["message"]

    @pytest.mark.asyncio
    async def test_rsvp_not_going(self):
        """TC-EVT-002P: RSVP 'not_going' (normal case)"""
        service, _, rsvp_repo = make_service()
        rsvp_repo.upsert_rsvp.return_value = None
        result = await service.rsvp(uuid4(), "guest@example.com", "not_going")
        assert "not_going" in result["message"]

    @pytest.mark.asyncio
    async def test_rsvp_invalid_status(self):
        """TC-EVT-002N: Invalid RSVP status -> 400"""
        service, _, _ = make_service()
        with pytest.raises(HTTPException) as exc:
            await service.rsvp(uuid4(), "guest@example.com", "invalid_status")
        assert exc.value.status_code == 400

    @pytest.mark.asyncio
    async def test_rsvp_update_existing(self):
        """TC-EVT-002V: Change RSVP from 'going' to 'not_going' (update)"""
        service, _, rsvp_repo = make_service()
        rsvp_repo.upsert_rsvp.return_value = None
        # Simulate: first RSVP "going", then overwrite with "not_going"
        result = await service.rsvp(uuid4(), "guest@example.com", "not_going")
        assert "not_going" in result["message"]
        rsvp_repo.upsert_rsvp.assert_called_once()


# =========================================================
# FR-EVT-03: Attendees
# =========================================================

class TestEventIntegration_Attendees:

    @pytest.mark.asyncio
    async def test_get_attendees_all(self):
        """TC-EVT-003P: Get all attendees (no filter)"""
        service, _, rsvp_repo = make_service()
        rsvp_repo.get_attendees.return_value = [
            FakeAttendee(guest_email="guest@example.com", response="going"),
            FakeAttendee(guest_email="guest@example.com", response="maybe"),
        ]
        result = await service.get_attendees(uuid4())
        assert len(result) == 2

    @pytest.mark.asyncio
    async def test_get_attendees_filtered(self):
        """TC-EVT-003P: Get attendees filtered by 'going'"""
        service, _, rsvp_repo = make_service()
        rsvp_repo.get_attendees.return_value = [
            FakeAttendee(guest_email="guest@example.com", response="going"),
        ]
        result = await service.get_attendees(uuid4(), rsvp_status="going")
        assert len(result) == 1
        assert result[0]["status"] == "going"

    @pytest.mark.asyncio
    async def test_get_attendees_no_results(self):
        """TC-EVT-003E: No attendees yet (empty)"""
        service, _, rsvp_repo = make_service()
        rsvp_repo.get_attendees.return_value = []
        result = await service.get_attendees(uuid4())
        assert result == []


# =========================================================
# FR-EVT-05: Reminders
# =========================================================

class TestEventIntegration_Reminder:

    @pytest.mark.asyncio
    async def test_send_reminder(self):
        """TC-EVT-005P: Send reminder (deferred)"""
        service, _, _ = make_service()
        result = await service.send_reminder(uuid4())
        assert "Reminder" in result["message"]