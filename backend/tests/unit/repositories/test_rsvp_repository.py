"""
FamilyConnect - Unit tests for rsvp_repository
"""
import pytest
from uuid import uuid4
from unittest.mock import AsyncMock, MagicMock

from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture
def db():
    db = AsyncMock(spec=AsyncSession)
    db.execute = AsyncMock()
    db.commit = AsyncMock()
    db.refresh = AsyncMock()
    db.add = MagicMock()
    return db


class TestRSVPRepository:

    @pytest.mark.asyncio
    async def test_upsert_rsvp_new(self, db):
        """BR-EVT-001: Create new RSVP"""
        result_mock = MagicMock()
        scalars_mock = MagicMock()
        scalars_mock.first.return_value = None
        result_mock.scalars.return_value = scalars_mock
        db.execute = AsyncMock(return_value=result_mock)

        from app.infrastructure.repositories.rsvp_repository import RSVPRepository
        repo = RSVPRepository(db)
        result = await repo.upsert_rsvp(uuid4(), uuid4(), "going")
        db.add.assert_called_once()
        db.commit.assert_called_once()
        assert result is not None

    @pytest.mark.asyncio
    async def test_upsert_rsvp_update(self, db):
        """BR-EVT-001: Update existing RSVP"""
        existing = MagicMock()
        existing.response = "maybe"
        result_mock = MagicMock()
        scalars_mock = MagicMock()
        scalars_mock.first.return_value = existing
        result_mock.scalars.return_value = scalars_mock
        db.execute = AsyncMock(return_value=result_mock)

        from app.infrastructure.repositories.rsvp_repository import RSVPRepository
        repo = RSVPRepository(db)
        result = await repo.upsert_rsvp(uuid4(), uuid4(), "going")
        assert existing.response == "going"
        db.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_attendees_all(self, db):
        """TC-EVT-003P: Get all attendees"""
        row = MagicMock()
        result_mock = MagicMock()
        scalars_mock = MagicMock()
        scalars_mock.all.return_value = [row]
        result_mock.scalars.return_value = scalars_mock
        db.execute = AsyncMock(return_value=result_mock)

        from app.infrastructure.repositories.rsvp_repository import RSVPRepository
        repo = RSVPRepository(db)
        result = await repo.get_attendees(uuid4())
        assert len(result) == 1

    @pytest.mark.asyncio
    async def test_get_attendees_filtered(self, db):
        """TC-EVT-003P: Get attendees filtered by response"""
        row = MagicMock()
        result_mock = MagicMock()
        scalars_mock = MagicMock()
        scalars_mock.all.return_value = [row]
        result_mock.scalars.return_value = scalars_mock
        db.execute = AsyncMock(return_value=result_mock)

        from app.infrastructure.repositories.rsvp_repository import RSVPRepository
        repo = RSVPRepository(db)
        result = await repo.get_attendees(uuid4(), "going")
        assert len(result) == 1