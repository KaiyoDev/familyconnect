"""In-memory repository doubles for DirectoryService unit tests."""


class FakeEmploymentRepository:
    def __init__(self):
        self.items = {}

    async def get_by_id(self, profile_id):
        return self.items.get(profile_id)

    async def get_by_member(self, member_id):
        return [p for p in self.items.values() if p.member_id == member_id]

    async def create(self, profile):
        self.items[profile.id] = profile
        return profile

    async def update(self, profile):
        self.items[profile.id] = profile
        return profile

    async def delete(self, profile):
        self.items.pop(profile.id, None)

    async def search_by_company(self, company_name, member_ids):
        c = company_name.lower()
        return [
            p for p in self.items.values()
            if p.member_id in member_ids and c in p.company_name.lower()
        ]

    async def search_by_position(self, position, member_ids):
        pos = position.lower()
        return [
            p for p in self.items.values()
            if p.member_id in member_ids and p.position and pos in p.position.lower()
        ]


class FakeEducationRepository:
    def __init__(self):
        self.items = {}

    async def get_by_id(self, profile_id):
        return self.items.get(profile_id)

    async def get_by_member(self, member_id):
        return [p for p in self.items.values() if p.member_id == member_id]

    async def create(self, profile):
        self.items[profile.id] = profile
        return profile

    async def update(self, profile):
        self.items[profile.id] = profile
        return profile

    async def delete(self, profile):
        self.items.pop(profile.id, None)

    async def search_by_school(self, school_name, member_ids):
        s = school_name.lower()
        return [
            p for p in self.items.values()
            if p.member_id in member_ids and s in p.school_name.lower()
        ]
