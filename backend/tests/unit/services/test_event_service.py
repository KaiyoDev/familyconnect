"""
FamilyConnect - Unit tests for event_service
"""
import pytest
from uuid import uuid4
from unittest.mock import AsyncMock

from fastapi import HTTPException
from app.services.event_service import EventService


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


class TestEventService:

    # ============ FR-EVT-01 ============

    @pytest.mark.asyncio
    async def test_create_event_success(self):
        """TC-EVT-001P: Create event successfully"""
        service, event_repo, _ = make_service()
        event_id = uuid4()
        event_repo.create.return_value = FakeEvent(id=event_id)

        result = await service.create_event(
            family_id=uuid4(), creator_id=uuid4(),
            data={"title": "Test Event", "start_time": "2026-09-01T08:00:00Z"}
        )
        assert result["event_id"] == str(event_id)
        assert result["message"] == "Event created successfully"

    # ============ FR-EVT-01: get events ============

    @pytest.mark.asyncio
    async def test_get_events(self):
        """TC-EVT-001P: List events"""
        service, event_repo, _ = make_service()
        event_repo.get_by_family.return_value = [
            FakeEvent(id=uuid4(), title="Event 1"),
            FakeEvent(id=uuid4(), title="Event 2"),
        ]
        result = await service.get_events(uuid4())
        assert len(result) == 2
        assert result[0]["title"] == "Event 1"

    @pytest.mark.asyncio
    async def test_get_events_empty(self):
        """TC-EVT-001E: Family has no events"""
        service, event_repo, _ = make_service()
        event_repo.get_by_family.return_value = []
        result = await service.get_events(uuid4())
        assert result == []

    # ============ FR-EVT-01: get event by id ============

    @pytest.mark.asyncio
    async def test_get_event_success(self):
        """TC-EVT-001P: Get event by id"""
        service, event_repo, _ = make_service()
        event_id = uuid4()
        event_repo.get_by_id.return_value = FakeEvent(id=event_id, title="My Event")
        result = await service.get_event(event_id)
        assert result["title"] == "My Event"

    @pytest.mark.asyncio
    async def test_get_event_not_found(self):
        """TC-EVT-001N: Event not found -> 404"""
        service, event_repo, _ = make_service()
        event_repo.get_by_id.return_value = None
        with pytest.raises(HTTPException) as exc:
            await service.get_event(uuid4())
        assert exc.value.status_code == 404

    # ============ FR-EVT-01: update event ============

    @pytest.mark.asyncio
    async def test_update_event_success(self):
        """TC-EVT-001V: Update event"""
        service, event_repo, _ = make_service()
        event_repo.update.return_value = FakeEvent(id=uuid4())
        result = await service.update_event(uuid4(), {"title": "Updated"})
        assert result["message"] == "Event updated successfully"

    @pytest.mark.asyncio
    async def test_update_event_not_found(self):
        """TC-EVT-001N: Update non-existent event -> 404"""
        service, event_repo, _ = make_service()
        event_repo.update.return_value = None
        with pytest.raises(HTTPException) as exc:
            await service.update_event(uuid4(), {})
        assert exc.value.status_code == 404

    # ============ FR-EVT-01: cancel event ============

    @pytest.mark.asyncio
    async def test_cancel_event_success(self):
        """TC-EVT-001N2: Cancel event"""
        service, event_repo, _ = make_service()
        event_repo.delete.return_value = True
        result = await service.cancel_event(uuid4())
        assert result["message"] == "Event cancelled successfully"

    @pytest.mark.asyncio
    async def test_cancel_event_not_found(self):
        """TC-EVT-001N: Cancel non-existent event -> 404"""
        service, event_repo, _ = make_service()
        event_repo.delete.return_value = False
        with pytest.raises(HTTPException) as exc:
            await service.cancel_event(uuid4())
        assert exc.value.status_code == 404

    # ============ FR-EVT-02: RSVP ============

    @pytest.mark.asyncio
    async def test_rsvp_going(self):
        """TC-EVT-002P: RSVP going"""
        service, _, rsvp_repo = make_service()
        rsvp_repo.upsert_rsvp.return_value = None
        result = await service.rsvp(uuid4(), "guest@example.com", "going")
        assert result["message"] == "RSVP updated to going"

    @pytest.mark.asyncio
    async def test_rsvp_maybe(self):
        """TC-EVT-002P: RSVP maybe"""
        service, _, rsvp_repo = make_service()
        rsvp_repo.upsert_rsvp.return_value = None
        result = await service.rsvp(uuid4(), "guest@example.com", "maybe")
        assert "maybe" in result["message"]

    @pytest.mark.asyncio
    async def test_rsvp_not_going(self):
        """TC-EVT-002N: RSVP not_going (overwrites previous)"""
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

    # ============ FR-EVT-03: get attendees ============

    @pytest.mark.asyncio
    async def test_get_attendees_all(self):
        """TC-EVT-003P: Get all attendees"""
        service, _, rsvp_repo = make_service()
        rsvp_repo.get_attendees.return_value = [
            FakeAttendee(guest_email="guest@example.com", response="going"),
            FakeAttendee(guest_email="guest@example.com", response="maybe"),
        ]
        result = await service.get_attendees(uuid4())
        assert len(result) == 2

    @pytest.mark.asyncio
    async def test_get_attendees_filtered(self):
        """TC-EVT-003P: Get attendees filtered by response"""
        service, _, rsvp_repo = make_service()
        rsvp_repo.get_attendees.return_value = [
            FakeAttendee(guest_email="guest@example.com", response="going"),
        ]
        result = await service.get_attendees(uuid4(), rsvp_status="going")
        assert len(result) == 1
        assert result[0]["status"] == "going"

    @pytest.mark.asyncio
    async def test_get_attendees_empty(self):
        """TC-EVT-003E: No attendees yet"""
        service, _, rsvp_repo = make_service()
        rsvp_repo.get_attendees.return_value = []
        result = await service.get_attendees(uuid4())
        assert result == []

    # ============ FR-EVT-05: reminder ============

    @pytest.mark.asyncio
    async def test_send_reminder(self):
        """TC-EVT-005P: Send reminder"""
        service, _, _ = make_service()
        result = await service.send_reminder(uuid4())
        assert "Reminder" in result["message"]