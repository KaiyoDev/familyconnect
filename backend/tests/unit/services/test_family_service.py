"""Unit tests for FamilyService without a real database."""
from types import SimpleNamespace
from uuid import uuid4

import pytest

from app.domain.exceptions import NotFoundException, ValidationException
from app.services.family_service import FamilyService
from tests.fakes.family_repositories import (
    FakeBranchRepository,
    FakeFamilyRepository,
    FakeMemberRepository,
    FakeRelationshipRepository,
    FakeUnitOfWork,
)


class FakeSession:
    def __init__(self):
        self.items = []
        self.refresh_count = 0

    def add(self, item):
        self.items.append(item)

    async def commit(self):
        pass

    async def refresh(self, item):
        self.refresh_count += 1

    async def rollback(self):
        pass


@pytest.fixture
def context():
    family_repo = FakeFamilyRepository()
    branch_repo = FakeBranchRepository()
    member_repo = FakeMemberRepository()
    relationship_repo = FakeRelationshipRepository()
    unit_of_work = FakeUnitOfWork()
    service = FamilyService(
        FakeSession(),
        family_repository=family_repo,
        member_repository=member_repo,
        relationship_repository=relationship_repo,
        branch_repository=branch_repo,
        unit_of_work=unit_of_work,
    )
    return SimpleNamespace(
        service=service,
        families=family_repo,
        branches=branch_repo,
        members=member_repo,
        relationships=relationship_repo,
        uow=unit_of_work,
    )


@pytest.mark.asyncio
async def test_create_family_creates_default_branch_and_commits(context):
    creator_id = uuid4()

    family = await context.service.create_family(creator_id, "Nguyen Family")

    assert family.family_name == "Nguyen Family"
    assert family.created_by == creator_id
    branches = await context.branches.get_by_family(family.id)
    assert len(branches) == 1
    assert branches[0].branch_name == "Main Branch"
    assert context.uow.commit_count == 1


@pytest.mark.asyncio
async def test_get_family_raises_when_missing(context):
    with pytest.raises(NotFoundException):
        await context.service.get_family(uuid4())


@pytest.mark.asyncio
async def test_update_family(context):
    family = await context.service.create_family(uuid4(), "Old Name")

    updated = await context.service.update_family(
        family.id,
        family_name="New Name",
        description="Updated",
    )

    assert updated.family_name == "New Name"
    assert updated.description == "Updated"


@pytest.mark.asyncio
async def test_delete_family(context):
    family = await context.service.create_family(uuid4(), "To Delete")

    await context.service.delete_family(family.id)

    assert await context.families.get_by_id(family.id) is None


@pytest.mark.asyncio
async def test_add_member_to_valid_branch(context):
    family = await context.service.create_family(uuid4(), "Family")
    branch = (await context.branches.get_by_family(family.id))[0]

    member = await context.service.add_member(
        family.id, "Parent", branch_id=branch.id, gender="MALE"
    )

    assert member.family_id == family.id
    assert member.branch_id == branch.id
    assert len(await context.members.get_by_family(family.id)) == 1


@pytest.mark.asyncio
async def test_add_member_rejects_branch_from_another_family(context):
    first = await context.service.create_family(uuid4(), "First")
    second = await context.service.create_family(uuid4(), "Second")
    foreign_branch = (await context.branches.get_by_family(second.id))[0]

    with pytest.raises(ValidationException):
        await context.service.add_member(
            first.id, "Invalid", branch_id=foreign_branch.id
        )


@pytest.mark.asyncio
async def test_update_and_remove_member(context):
    family = await context.service.create_family(uuid4(), "Family")
    member = await context.service.add_member(family.id, "Old Name")

    updated = await context.service.update_member(member.id, full_name="New Name")
    assert updated.full_name == "New Name"

    await context.service.remove_member(member.id)
    assert await context.members.get_by_id(member.id) is None


@pytest.mark.asyncio
async def test_add_parent_child_relationship(context):
    family = await context.service.create_family(uuid4(), "Family")
    parent = await context.service.add_member(family.id, "Parent")
    child = await context.service.add_member(family.id, "Child")

    relationship = await context.service.add_relationship(
        family.id, parent.id, child.id, "PARENT_CHILD"
    )

    assert relationship.type == "PARENT_CHILD"
    assert relationship.id in context.relationships.items


@pytest.mark.asyncio
async def test_add_marriage_relationship(context):
    family = await context.service.create_family(uuid4(), "Family")
    first = await context.service.add_member(family.id, "First")
    second = await context.service.add_member(family.id, "Second")

    relationship = await context.service.add_relationship(
        family.id, first.id, second.id, "MARRIAGE"
    )

    assert relationship.type == "MARRIAGE"


@pytest.mark.asyncio
async def test_relationship_validation(context):
    family = await context.service.create_family(uuid4(), "Family")
    member = await context.service.add_member(family.id, "Only Member")

    with pytest.raises(ValidationException):
        await context.service.add_relationship(
            family.id, member.id, member.id, "PARENT_CHILD"
        )

    with pytest.raises(ValidationException):
        await context.service.add_relationship(
            family.id, member.id, uuid4(), "PARENT_CHILD"
        )

    with pytest.raises(ValidationException):
        await context.service.add_relationship(
            family.id, member.id, uuid4(), "INVALID"
        )


@pytest.mark.asyncio
async def test_genealogy_tree_contains_roots_children_and_spouses(context):
    family = await context.service.create_family(uuid4(), "Family")
    parent = await context.service.add_member(family.id, "Parent")
    child = await context.service.add_member(family.id, "Child")
    spouse = await context.service.add_member(family.id, "Spouse")

    await context.service.add_relationship(
        family.id, parent.id, child.id, "PARENT_CHILD"
    )
    await context.service.add_relationship(
        family.id, parent.id, spouse.id, "MARRIAGE"
    )

    tree = await context.service.get_genealogy_tree(family.id)
    root = next(node for node in tree if node["id"] == str(parent.id))

    assert [node["id"] for node in root["children"]] == [str(child.id)]
    assert root["spouse_ids"] == [str(spouse.id)]
    assert all(node["id"] != str(child.id) for node in tree)


@pytest.mark.asyncio
async def test_lookup_relationship_returns_direct_relationship(context):
    family = await context.service.create_family(uuid4(), "Family")
    first = await context.service.add_member(family.id, "First")
    second = await context.service.add_member(family.id, "Second")
    await context.service.add_relationship(family.id, first.id, second.id, "MARRIAGE")

    result = await context.service.lookup_relationship(family.id, first.id, second.id)

    assert len(result) == 1
    assert result[0].type == "MARRIAGE"
