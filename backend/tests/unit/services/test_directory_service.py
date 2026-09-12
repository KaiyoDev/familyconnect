"""Unit tests for DirectoryService (generation computation, search, profile)."""
from types import SimpleNamespace
from uuid import uuid4
from datetime import date

import pytest

from app.domain.exceptions import NotFoundException, ValidationException
from app.services.directory_service import DirectoryService
from tests.fakes.family_repositories import (
    FakeFamilyRepository,
    FakeMemberRepository,
    FakeBranchRepository,
    FakeRelationshipRepository,
    FakeUnitOfWork,
)
from tests.fakes.directory_repositories import FakeEmploymentRepository, FakeEducationRepository


class FakeSession:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)


@pytest.fixture
def context():
    family_repo = FakeFamilyRepository()
    member_repo = FakeMemberRepository()
    branch_repo = FakeBranchRepository()
    relationship_repo = FakeRelationshipRepository()
    employment_repo = FakeEmploymentRepository()
    education_repo = FakeEducationRepository()
    unit_of_work = FakeUnitOfWork()
    service = DirectoryService(
        FakeSession(),
        family_repository=family_repo,
        member_repository=member_repo,
        branch_repository=branch_repo,
        relationship_repository=relationship_repo,
        employment_repository=employment_repo,
        education_repository=education_repo,
        unit_of_work=unit_of_work,
    )
    return SimpleNamespace(
        service=service,
        families=family_repo,
        members=member_repo,
        branches=branch_repo,
        relationships=relationship_repo,
        employment=employment_repo,
        education=education_repo,
        uow=unit_of_work,
    )


def _make_member(member_repo, family_id, member_id, full_name, branch_id=None, address=None):
    """Helper to create a minimal FamilyMember-like object."""
    from types import SimpleNamespace as NS
    m = NS(
        id=member_id,
        family_id=family_id,
        full_name=full_name,
        branch_id=branch_id,
        gender="MALE",
        date_of_birth=date(1990, 1, 1),
        date_of_death=None,
        address=address,
        is_alive=True,
        status="ACTIVE",
    )
    member_repo.items[member_id] = m
    return m


def _make_relationship(rel_repo, rel_id, from_id, to_id, rel_type):
    from types import SimpleNamespace as NS
    r = NS(id=rel_id, from_member_id=from_id, to_member_id=to_id, type=rel_type)
    rel_repo.items[rel_id] = r
    return r


# ── Generation computation ──────────────────────────────────────────────


@pytest.mark.asyncio
async def test_generation_no_relations_assigns_root_generation(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    m = _make_member(context.members, family_id, uuid4(), "A")

    result = await context.service._compute_generations(family_id, [m.id])

    # No relationships means the member is a root (generation 1)
    assert result[m.id] == 1


@pytest.mark.asyncio
async def test_generation_simple_parent_child(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    grandparent = _make_member(context.members, family_id, uuid4(), "Grandparent")
    parent = _make_member(context.members, family_id, uuid4(), "Parent")
    child = _make_member(context.members, family_id, uuid4(), "Child")

    _make_relationship(context.relationships, uuid4(), grandparent.id, parent.id, "PARENT_CHILD")
    _make_relationship(context.relationships, uuid4(), parent.id, child.id, "PARENT_CHILD")

    member_ids = [grandparent.id, parent.id, child.id]
    generations = await context.service._compute_generations(family_id, member_ids)

    assert generations[grandparent.id] == 1
    assert generations[parent.id] == 2
    assert generations[child.id] == 3


@pytest.mark.asyncio
async def test_generation_marriage_ignored(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    parent = _make_member(context.members, family_id, uuid4(), "Parent")
    spouse = _make_member(context.members, family_id, uuid4(), "Spouse")

    _make_relationship(context.relationships, uuid4(), parent.id, spouse.id, "MARRIAGE")

    member_ids = [parent.id, spouse.id]
    generations = await context.service._compute_generations(family_id, member_ids)

    # Neither has generation because no PARENT_CHILD edges
    assert generations.get(parent.id) is None or generations.get(parent.id) == 1
    assert generations.get(spouse.id) is None or generations.get(spouse.id) == 1


# ── Directory listing ───────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_get_directory_returns_members_with_generation(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    root = _make_member(context.members, family_id, uuid4(), "Root")
    child = _make_member(context.members, family_id, uuid4(), "Child")
    _make_relationship(context.relationships, uuid4(), root.id, child.id, "PARENT_CHILD")

    result = await context.service.get_directory(family_id)

    assert result["total"] == 2
    gen_map = {m["full_name"]: m["generation"] for m in result["members"]}
    assert gen_map["Root"] == 1
    assert gen_map["Child"] == 2


@pytest.mark.asyncio
async def test_get_directory_filters_by_generation(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    root = _make_member(context.members, family_id, uuid4(), "Root")
    course = _make_member(context.members, family_id, uuid4(), "Course")
    _make_relationship(context.relationships, uuid4(), root.id, course.id, "PARENT_CHILD")

    result = await context.service.get_directory(family_id, generation=1)

    assert len(result["members"]) == 1
    assert result["total"] == 1
    assert result["members"][0]["full_name"] == "Root"


# ── Member search ───────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_search_members_by_name_query(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    _make_member(context.members, family_id, uuid4(), "Nguyen Van A")
    _make_member(context.members, family_id, uuid4(), "Tran Thi B")
    _make_member(context.members, family_id, uuid4(), "Le Van C")

    result = await context.service.search_members(family_id, query="Van")

    assert len(result["members"]) == 2
    names = {m["full_name"] for m in result["members"]}
    assert "Nguyen Van A" in names
    assert "Le Van C" in names
    assert "Tran Thi B" not in names


@pytest.mark.asyncio
async def test_search_members_by_profession_matches_company(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    m1 = _make_member(context.members, family_id, uuid4(), "Doctor")
    m2 = _make_member(context.members, family_id, uuid4(), "Teacher")
    m3 = _make_member(context.members, family_id, uuid4(), "Engineer")

    from types import SimpleNamespace as NS
    for mid, company in [(m1.id, "Central Hospital"), (m2.id, "High School"), (m3.id, "Tech Corp")]:
        p = NS(id=uuid4(), member_id=mid, company_name=company, position="Staff",
               start_date=date(2020, 1, 1), end_date=None,
               is_current=True, description=None)
        context.employment.items[p.id] = p

    result = await context.service.search_members(family_id, profession="Hospital")

    assert len(result["members"]) == 1
    assert result["members"][0]["full_name"] == "Doctor"


@pytest.mark.asyncio
async def test_search_members_by_profession_matches_position(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    m1 = _make_member(context.members, family_id, uuid4(), "Lead Dev")
    m2 = _make_member(context.members, family_id, uuid4(), "Manager")

    from types import SimpleNamespace as NS
    p = NS(id=uuid4(), member_id=m1.id, company_name="Company", position="Engineering Lead",
           start_date=date(2020, 1, 1), end_date=None,
           is_current=True, description=None)
    context.employment.items[p.id] = p

    result = await context.service.search_members(family_id, profession="Engineering")

    assert len(result["members"]) == 1
    assert result["members"][0]["full_name"] == "Lead Dev"


@pytest.mark.asyncio
async def test_search_members_by_generation(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    root = _make_member(context.members, family_id, uuid4(), "Root")
    child = _make_member(context.members, family_id, uuid4(), "Child")
    _make_relationship(context.relationships, uuid4(), root.id, child.id, "PARENT_CHILD")

    result = await context.service.search_members(family_id, generation=1)

    assert len(result["members"]) == 1
    assert result["members"][0]["full_name"] == "Root"
    assert result["members"][0]["generation"] == 1


@pytest.mark.asyncio
async def test_search_combined_filters(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    root = _make_member(context.members, family_id, uuid4(), "Root")
    child = _make_member(context.members, family_id, uuid4(), "Child")
    _make_relationship(context.relationships, uuid4(), root.id, child.id, "PARENT_CHILD")

    from types import SimpleNamespace as NS
    p = NS(id=uuid4(), member_id=child.id, company_name="Hospital", position="Doctor",
           start_date=date(2020, 1, 1), end_date=None,
           is_current=True, description=None)
    context.employment.items[p.id] = p

    # Child is generation 2 but works at Hospital
    result_gen1 = await context.service.search_members(family_id, generation=1, profession="Hospital")
    result_gen2 = await context.service.search_members(family_id, generation=2, profession="Hospital")

    assert len(result_gen1["members"]) == 0
    assert len(result_gen2["members"]) == 1
    assert result_gen2["members"][0]["full_name"] == "Child"


# ── Member profile ──────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_get_member_profile_includes_employment_education(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    m = _make_member(context.members, family_id, uuid4(), "Alice")

    from types import SimpleNamespace as NS
    emp = NS(id=uuid4(), member_id=m.id, company_name="ACME", position="Engineer",
             start_date=date(2020, 1, 1), end_date=date(2022, 1, 1),
             is_current=False, description="Built things")
    edu = NS(id=uuid4(), member_id=m.id, school_name="MIT", degree="BS", field_of_study="CS",
             start_year=2016, end_year=2020, gpa=3.5)
    context.employment.items[emp.id] = emp
    context.education.items[edu.id] = edu

    profile = await context.service.get_member_profile(family_id, m.id)

    assert profile["full_name"] == "Alice"
    assert len(profile["employment"]) == 1
    assert profile["employment"][0]["company_name"] == "ACME"
    assert len(profile["education"]) == 1
    assert profile["education"][0]["school_name"] == "MIT"


# ── CRUD profile operations ─────────────────────────────────────────────


@pytest.mark.asyncio
async def test_create_and_update_employment(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    m = _make_member(context.members, family_id, uuid4(), "Bob")

    created = await context.service.update_employment(
        family_id, m.id, company_name="New Corp", position="Dev", is_current=True,
    )

    assert created.company_name == "New Corp"
    assert created.is_current is True

    updated = await context.service.update_employment(
        family_id, m.id, profile_id=created.id, position="Senior Dev",
    )

    assert updated.position == "Senior Dev"


@pytest.mark.asyncio
async def test_create_employment_requires_company_name(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    m = _make_member(context.members, family_id, uuid4(), "Eve")

    with pytest.raises(ValidationException):
        await context.service.update_employment(family_id, m.id)


@pytest.mark.asyncio
async def test_delete_employment(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    m = _make_member(context.members, family_id, uuid4(), "Charlie")

    created = await context.service.update_employment(
        family_id, m.id, company_name="Gone Corp", position="Gone",
    )

    await context.service.delete_employment(family_id, m.id, created.id)

    assert created.id not in context.employment.items


@pytest.mark.asyncio
async def test_member_not_found_raises(context):
    with pytest.raises(NotFoundException):
        await context.service.get_member_profile(uuid4(), uuid4())


@pytest.mark.asyncio
async def test_foreign_member_raises(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    other_id = uuid4()
    context.families.items[other_id] = SimpleNamespace(id=other_id)
    m = _make_member(context.members, other_id, uuid4(), "Foreigner")

    with pytest.raises(NotFoundException):
        await context.service.get_member_profile(family_id, m.id)


# ── Location / address search ────────────────────────────────────────────


@pytest.mark.asyncio
async def test_search_members_by_address(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    m1 = _make_member(context.members, family_id, uuid4(), "Alice", address="123 Hanoi Street")
    m2 = _make_member(context.members, family_id, uuid4(), "Bob", address="456 Saigon Road")
    m3 = _make_member(context.members, family_id, uuid4(), "Charlie", address="789 Da Nang Ave")

    result = await context.service.search_members(family_id, location="Hanoi")

    assert len(result["members"]) == 1
    assert result["members"][0]["full_name"] == "Alice"
    assert result["members"][0]["address"] == "123 Hanoi Street"


@pytest.mark.asyncio
async def test_search_members_by_location_falls_back_to_school(context):
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    m1 = _make_member(context.members, family_id, uuid4(), "Alice")
    m2 = _make_member(context.members, family_id, uuid4(), "Bob")

    from types import SimpleNamespace as NS
    edu = NS(id=uuid4(), member_id=m2.id, school_name="Hanoi University", degree="BA",
             field_of_study="Economics", start_year=2015, end_year=2019, gpa=3.0)
    context.education.items[edu.id] = edu

    result = await context.service.search_members(family_id, location="Hanoi")

    assert len(result["members"]) == 1
    assert result["members"][0]["full_name"] == "Bob"


@pytest.mark.asyncio
async def test_search_members_by_location_combined(context):
    """address AND school should both match"""
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    m1 = _make_member(context.members, family_id, uuid4(), "Alice", address="Hanoi, Vietnam")
    m2 = _make_member(context.members, family_id, uuid4(), "Bob")

    from types import SimpleNamespace as NS
    edu = NS(id=uuid4(), member_id=m2.id, school_name="Saigon University", degree="BS",
             field_of_study="Engineering", start_year=2015, end_year=2019, gpa=3.5)
    context.education.items[edu.id] = edu

    # Search "Vietnam" should match Alice's address but not Bob's school
    result = await context.service.search_members(family_id, location="Vietnam")
    assert len(result["members"]) == 1
    assert result["members"][0]["full_name"] == "Alice"

    # Search "Saigon" should match Bob's school
    result = await context.service.search_members(family_id, location="Saigon")
    assert len(result["members"]) == 1
    assert result["members"][0]["full_name"] == "Bob"


# ── N+1 batch loading ───────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_directory_includes_profiles_via_batch(context):
    """Verify that get_directory returns employment/education without N+1."""
    family_id = uuid4()
    context.families.items[family_id] = SimpleNamespace(id=family_id)
    m = _make_member(context.members, family_id, uuid4(), "Alice", address="Somewhere")

    from types import SimpleNamespace as NS
    emp = NS(id=uuid4(), member_id=m.id, company_name="Big Corp", position="Engineer",
             start_date=date(2020, 1, 1), end_date=None, is_current=True, description=None)
    context.employment.items[emp.id] = emp

    result = await context.service.get_directory(family_id)

    member = result["members"][0]
    assert member["address"] == "Somewhere"
    assert len(member["employment"]) == 1
    assert member["employment"][0]["company_name"] == "Big Corp"
    assert member["employment"][0]["position"] == "Engineer"
    assert member["education"] == []