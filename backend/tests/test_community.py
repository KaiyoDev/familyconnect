"""
FamilyConnect - Integration tests for Community module (FR-COM-01, 02, 03, 05)

Tests endpoints: 
  - POST /families/{family_id}/posts   (FR-COM-01)
  - GET  /families/{family_id}/feed     (FR-COM-03)
  - GET  /posts/{post_id}               (FR-COM-01)
  - PUT  /posts/{post_id}               (FR-COM-01)
  - DELETE /posts/{post_id}             (FR-COM-01)
  - POST /posts/{post_id}/comments      (FR-COM-02)
  - POST /posts/{post_id}/reactions     (FR-COM-02)
  - DELETE /posts/{post_id}/reactions   (FR-COM-02)
"""
import pytest
from uuid import uuid4
from unittest.mock import AsyncMock, patch, MagicMock
from fastapi import HTTPException, status
from app.services.community_service import (
    CommunityService, NotFoundError, ForbiddenError,
    ValidationError, ConflictError,
)


# =========================================================
# Helper to make a mocked CommunityService
# =========================================================

def make_mock_service():
    """Return (service_instance, post_repo_mock, comment_repo_mock, reaction_repo_mock)."""
    post_repo = AsyncMock()
    comment_repo = AsyncMock()
    reaction_repo = AsyncMock()
    service = CommunityService(post_repo, comment_repo, reaction_repo)
    return service, post_repo, comment_repo, reaction_repo


# =========================================================
# FR-COM-01: Post Management
# =========================================================

class TestCommunityIntegration_Post:

    @pytest.mark.asyncio
    async def test_create_post_success(self):
        """TC-COM-001P: Create post successfully (normal case)"""
        service, post_repo, _, _ = make_mock_service()
        post_id = uuid4()
        post_repo.create.return_value = MagicMock(id=post_id)

        result = await service.create_post(
            family_id=uuid4(), author_id=uuid4(),
            content="  Hello world!  "
        )
        assert result.id == post_id
        post_repo.create.assert_called_once()

    @pytest.mark.asyncio
    async def test_create_post_empty_content(self):
        """TC-COM-001N: Create post with whitespace-only content -> ValidationError"""
        service, _, _, _ = make_mock_service()
        with pytest.raises(ValidationError):
            await service.create_post(
                family_id=uuid4(), author_id=uuid4(), content="   "
            )

    @pytest.mark.asyncio
    async def test_get_feed_empty(self):
        """TC-COM-003P: Get feed with no posts"""
        service, post_repo, _, _ = make_mock_service()
        post_repo.get_feed.return_value = []
        result = await service.get_feed(uuid4(), page=1, page_size=20)
        assert result == []

    @pytest.mark.asyncio
    async def test_get_feed_invalid_page(self):
        """TC-COM-001N: Feed with page=0 -> ValidationError"""
        service, _, _, _ = make_mock_service()
        with pytest.raises(ValidationError):
            await service.get_feed(uuid4(), page=0)

    @pytest.mark.asyncio
    async def test_get_feed_invalid_page_size(self):
        """TC-COM-001N: Feed with page_size > 100 -> ValidationError"""
        service, _, _, _ = make_mock_service()
        with pytest.raises(ValidationError):
            await service.get_feed(uuid4(), page=1, page_size=101)

    @pytest.mark.asyncio
    async def test_get_post_not_found(self):
        """TC-COM-001N: Get non-existent post -> NotFoundError"""
        service, post_repo, _, _ = make_mock_service()
        post_repo.get_by_id.return_value = None
        with pytest.raises(NotFoundError):
            await service.get_post(uuid4())

    @pytest.mark.asyncio
    async def test_update_post_author(self):
        """TC-COM-001P2: Author updates own post"""
        service, post_repo, _, _ = make_mock_service()
        author = uuid4()
        post = MagicMock(id=uuid4(), author_id=author, content="Old")
        post_repo.get_by_id.return_value = post
        post_repo.update.return_value = post
        result = await service.update_post(post.id, author, content="New")
        assert result is not None

    @pytest.mark.asyncio
    async def test_update_post_non_author(self):
        """TC-COM-001N2: Non-author cannot update post -> ForbiddenError"""
        service, post_repo, _, _ = make_mock_service()
        post = MagicMock(id=uuid4(), author_id=uuid4(), content="Old")
        post_repo.get_by_id.return_value = post
        with pytest.raises(ForbiddenError):
            await service.update_post(post.id, uuid4(), content="Hack")

    @pytest.mark.asyncio
    async def test_delete_post_author(self):
        """TC-COM-001P3: Author deletes own post"""
        service, post_repo, _, _ = make_mock_service()
        author = uuid4()
        post = MagicMock(id=uuid4(), author_id=author, content="To delete")
        post_repo.get_by_id.return_value = post
        await service.delete_post(post.id, author)
        post_repo.delete.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_post_non_author(self):
        """TC-COM-001N2: Non-author delete -> ForbiddenError"""
        service, post_repo, _, _ = make_mock_service()
        post = MagicMock(id=uuid4(), author_id=uuid4(), content="To delete")
        post_repo.get_by_id.return_value = post
        with pytest.raises(ForbiddenError):
            await service.delete_post(post.id, uuid4())


# =========================================================
# FR-COM-02: Comments & Reactions
# =========================================================

class TestCommunityIntegration_Comment:

    @pytest.mark.asyncio
    async def test_add_comment_success(self):
        """TC-COM-002P: Add comment to existing post"""
        service, post_repo, comment_repo, _ = make_mock_service()
        post = MagicMock(id=uuid4(), author_id=uuid4(), content="Post")
        post_repo.get_by_id.return_value = post
        comment_repo.create.return_value = MagicMock(id=uuid4())

        result = await service.add_comment(post.id, uuid4(), "Chúc mừng năm mới!")
        assert result.id is not None

    @pytest.mark.asyncio
    async def test_add_comment_empty(self):
        """TC-COM-002N: Empty comment -> ValidationError"""
        service, post_repo, _, _ = make_mock_service()
        post = MagicMock(id=uuid4(), author_id=uuid4(), content="Post")
        post_repo.get_by_id.return_value = post
        with pytest.raises(ValidationError):
            await service.add_comment(post.id, uuid4(), "   ")

    @pytest.mark.asyncio
    async def test_add_comment_too_long(self):
        """TC-COM-002N: Comment > 1000 chars -> ValidationError"""
        service, post_repo, _, _ = make_mock_service()
        post = MagicMock(id=uuid4(), author_id=uuid4(), content="Post")
        post_repo.get_by_id.return_value = post
        with pytest.raises(ValidationError):
            await service.add_comment(post.id, uuid4(), "x" * 1001)

    @pytest.mark.asyncio
    async def test_add_reaction_success(self):
        """TC-COM-002P2: Add reaction LIKE"""
        service, post_repo, _, reaction_repo = make_mock_service()
        post = MagicMock(id=uuid4(), author_id=uuid4(), content="Post")
        post_repo.get_by_id.return_value = post
        reaction_repo.get.return_value = None
        reaction_repo.create.return_value = MagicMock(id=uuid4())

        result = await service.add_reaction(post.id, uuid4(), "LIKE")
        assert result.id is not None

    @pytest.mark.asyncio
    async def test_add_reaction_invalid_type(self):
        """TC-COM-002N: Invalid reaction type -> ValidationError"""
        service, post_repo, _, _ = make_mock_service()
        post = MagicMock(id=uuid4(), author_id=uuid4(), content="Post")
        post_repo.get_by_id.return_value = post
        with pytest.raises(ValidationError):
            await service.add_reaction(post.id, uuid4(), "INVALID")

    @pytest.mark.asyncio
    async def test_add_reaction_duplicate(self):
        """TC-COM-002V: Duplicate reaction -> ConflictError"""
        service, post_repo, _, reaction_repo = make_mock_service()
        post = MagicMock(id=uuid4(), author_id=uuid4(), content="Post")
        post_repo.get_by_id.return_value = post
        reaction_repo.get.return_value = MagicMock(id=uuid4())
        with pytest.raises(ConflictError):
            await service.add_reaction(post.id, uuid4(), "LIKE")

    @pytest.mark.asyncio
    async def test_remove_reaction_not_found(self):
        """TC-COM-002N: Remove non-existent reaction -> NotFoundError"""
        service, post_repo, _, reaction_repo = make_mock_service()
        post = MagicMock(id=uuid4(), author_id=uuid4(), content="Post")
        post_repo.get_by_id.return_value = post
        reaction_repo.delete.return_value = False
        with pytest.raises(NotFoundError):
            await service.remove_reaction(post.id, uuid4(), "LIKE")


# =========================================================
# FR-COM-05: Announcements
# =========================================================

class TestCommunityIntegration_Announcement:

    @pytest.mark.asyncio
    async def test_create_announcement_success(self):
        """TC-COM-005P: Create announcement successfully"""
        service, post_repo, _, _ = make_mock_service()
        announcement_id = uuid4()
        post_repo.create.return_value = MagicMock(
            id=announcement_id, visibility_scope="FAMILY"
        )
        result = await service.create_announcement(
            family_id=uuid4(), author_id=uuid4(), content="Family meeting next Sunday!"
        )
        assert result.id == announcement_id

    @pytest.mark.asyncio
    async def test_create_announcement_empty(self):
        """TC-COM-005N: Create announcement with empty content -> ValidationError"""
        service, _, _, _ = make_mock_service()
        with pytest.raises(ValidationError):
            await service.create_announcement(
                family_id=uuid4(), author_id=uuid4(), content=""
            )