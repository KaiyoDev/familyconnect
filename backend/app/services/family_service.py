"""Application service for family and genealogy use cases."""
from uuid import UUID, uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.exceptions import NotFoundException, ValidationException
from app.domain.interfaces.branch_repository import IBranchRepository
from app.domain.interfaces.family_repository import IFamilyRepository
from app.domain.interfaces.member_repository import IMemberRepository
from app.domain.interfaces.relationship_repository import IRelationshipRepository
from app.domain.interfaces.unit_of_work import IUnitOfWork
from app.infrastructure.models.genealogy import Family, FamilyBranch, FamilyMember, Relationship


class FamilyService:
    """Coordinates family aggregate and genealogy operations."""

    def __init__(self, session: AsyncSession, family_repository: IFamilyRepository | None = None,
                 member_repository: IMemberRepository | None = None,
                 relationship_repository: IRelationshipRepository | None = None,
                 branch_repository: IBranchRepository | None = None,
                 unit_of_work: IUnitOfWork | None = None):
        self.session = session
        if not all((family_repository, member_repository, relationship_repository, branch_repository, unit_of_work)):
            raise ValueError("Repositories and unit_of_work must be injected")
        self.families = family_repository
        self.members = member_repository
        self.relationships = relationship_repository
        self.branches = branch_repository
        self.unit_of_work = unit_of_work

    async def _commit(self):
        await self.unit_of_work.commit()

    async def _rollback(self):
        await self.unit_of_work.rollback()

    async def _write(self, operation):
        try:
            result = await operation()
            await self._commit()
            return result
        except Exception:
            await self._rollback()
            raise

    async def create_family(self, creator_id: UUID, family_name: str, description: str | None = None):
        family = Family(id=uuid4(), family_name=family_name, description=description, created_by=creator_id, status="ACTIVE")
        await self.families.create(family)
        branch = FamilyBranch(id=uuid4(), family_id=family.id, branch_name="Main Branch")
        if self.branches:
            await self.branches.create(branch)
        else:
            self.session.add(branch)
        await self._commit()
        await self.session.refresh(family)
        return family

    async def get_family(self, family_id: UUID):
        family = await self.families.get_by_id(family_id)
        if not family:
            raise NotFoundException("Family not found")
        return family

    async def list_families(self, creator_id: UUID | None = None):
        return await self.families.get_by_creator(creator_id) if creator_id else await self.families.get_all()

    async def update_family(self, family_id: UUID, **data):
        family = await self.get_family(family_id)
        for key in ("family_name", "description", "status"):
            if key in data and data[key] is not None:
                setattr(family, key, data[key])
        await self.families.update(family)
        await self._commit()
        return family

    async def delete_family(self, family_id: UUID):
        await self.families.delete(await self.get_family(family_id))
        await self._commit()

    async def add_member(self, family_id: UUID, full_name: str, branch_id: UUID | None = None, **data):
        await self.get_family(family_id)
        if branch_id and self.branches:
            branch = await self.branches.get_by_id(branch_id)
            if not branch or branch.family_id != family_id:
                raise ValidationException("Branch does not belong to the family")
        member = FamilyMember(id=uuid4(), family_id=family_id, branch_id=branch_id, full_name=full_name,
                              gender=data.get("gender", "UNKNOWN"), date_of_birth=data.get("date_of_birth"),
                              address=data.get("address"),
                              is_alive=data.get("is_alive", True), date_of_death=data.get("date_of_death"),
                              status=data.get("status", "PENDING"))
        await self.members.create(member)
        await self._commit()
        return member

    async def update_member(self, member_id: UUID, **data):
        member = await self.members.get_by_id(member_id)
        if not member:
            raise NotFoundException("Member not found")
        for key in ("full_name", "branch_id", "gender", "date_of_birth", "date_of_death", "address", "is_alive", "status"):
            if key in data and data[key] is not None:
                setattr(member, key, data[key])
        await self.members.update(member)
        await self._commit()
        return member

    async def remove_member(self, member_id: UUID):
        member = await self.members.get_by_id(member_id)
        if not member:
            raise NotFoundException("Member not found")
        await self.members.delete(member)
        await self._commit()

    async def add_relationship(self, family_id: UUID, from_member_id: UUID, to_member_id: UUID, relationship_type: str, notes=None):
        if from_member_id == to_member_id:
            raise ValidationException("A member cannot relate to itself")
        member_ids = {m.id for m in await self.members.get_by_family(family_id)}
        if from_member_id not in member_ids or to_member_id not in member_ids:
            raise ValidationException("Both members must belong to the family")
        if relationship_type not in {"PARENT_CHILD", "MARRIAGE"}:
            raise ValidationException("Unsupported relationship type")
        relationship = Relationship(id=uuid4(), from_member_id=from_member_id, to_member_id=to_member_id,
                                    type=relationship_type, notes=notes)
        await self.relationships.create(relationship)
        await self._commit()
        return relationship

    async def remove_relationship(self, relationship_id: UUID):
        relationship = await self.relationships.get_by_id(relationship_id)
        if not relationship:
            raise NotFoundException("Relationship not found")
        await self.relationships.delete(relationship)
        await self._commit()

    async def get_genealogy_tree(self, family_id: UUID):
        members = await self.members.get_by_family(family_id)
        relations = await self.relationships.get_by_family_members({str(m.id) for m in members})
        nodes = {str(m.id): {"id": str(m.id), "full_name": m.full_name, "children": [], "spouse_ids": []} for m in members}
        child_ids = set()
        for relation in relations:
            source, target = str(relation.from_member_id), str(relation.to_member_id)
            if relation.type == "PARENT_CHILD" and source in nodes and target in nodes:
                nodes[source]["children"].append(nodes[target])
                child_ids.add(target)
            elif relation.type == "MARRIAGE" and source in nodes and target in nodes:
                nodes[source]["spouse_ids"].append(target)
        return [node for member_id, node in nodes.items() if member_id not in child_ids]

    async def lookup_relationship(self, family_id: UUID, from_member_id: UUID, to_member_id: UUID):
        member_ids = {str(from_member_id), str(to_member_id)}
        relations = await self.relationships.get_by_family_members(member_ids)
        return [r for r in relations if {str(r.from_member_id), str(r.to_member_id)} == member_ids]
