"""In-memory repository doubles for FamilyService unit tests."""
from copy import copy
from uuid import UUID


class FakeFamilyRepository:
    def __init__(self):
        self.items = {}

    async def get_by_id(self, family_id):
        return self.items.get(family_id)

    async def get_all(self, skip=0, limit=100):
        return list(self.items.values())[skip:skip + limit]

    async def create(self, family):
        self.items[family.id] = family
        return family

    async def update(self, family):
        self.items[family.id] = family
        return family

    async def delete(self, family):
        self.items.pop(family.id, None)

    async def get_by_creator(self, creator_id):
        return [item for item in self.items.values() if item.created_by == creator_id]

    async def get_members(self, family_id):
        return []

    async def get_branches(self, family_id):
        return []


class FakeBranchRepository:
    def __init__(self):
        self.items = {}

    async def get_by_id(self, branch_id):
        return self.items.get(branch_id)

    async def get_by_family(self, family_id):
        return [item for item in self.items.values() if item.family_id == family_id]

    async def create(self, branch):
        self.items[branch.id] = branch
        return branch

    async def update(self, branch):
        self.items[branch.id] = branch
        return branch

    async def delete(self, branch):
        self.items.pop(branch.id, None)


class FakeMemberRepository:
    def __init__(self):
        self.items = {}

    async def get_by_id(self, member_id):
        return self.items.get(member_id)

    async def get_by_family(self, family_id):
        return [item for item in self.items.values() if item.family_id == family_id]

    async def create(self, member):
        self.items[member.id] = member
        return member

    async def update(self, member):
        self.items[member.id] = member
        return member

    async def delete(self, member):
        self.items.pop(member.id, None)


class FakeRelationshipRepository:
    def __init__(self):
        self.items = {}

    async def get_by_id(self, relationship_id):
        return self.items.get(relationship_id)

    async def get_by_family_members(self, member_ids):
        return [
            item for item in self.items.values()
            if str(item.from_member_id) in member_ids
            and str(item.to_member_id) in member_ids
        ]

    async def create(self, relationship):
        self.items[relationship.id] = relationship
        return relationship

    async def delete(self, relationship):
        self.items.pop(relationship.id, None)


class FakeUnitOfWork:
    def __init__(self):
        self.commit_count = 0
        self.rollback_count = 0

    async def commit(self):
        self.commit_count += 1

    async def rollback(self):
        self.rollback_count += 1
