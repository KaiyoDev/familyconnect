"""Mapping between domain data objects and SQLAlchemy models."""
from app.domain.models import FamilyBranchData, FamilyData, FamilyMemberData, RelationshipData
from app.infrastructure.models.genealogy import Family, FamilyBranch, FamilyMember, Relationship


class FamilyMapper:
    @staticmethod
    def to_domain(model: Family) -> FamilyData:
        return FamilyData(model.id, model.family_name, model.created_by, model.description, model.status)

    @staticmethod
    def to_model(data: FamilyData) -> Family:
        return Family(id=data.id, family_name=data.family_name, created_by=data.created_by,
                      description=data.description, status=data.status.value)


class BranchMapper:
    @staticmethod
    def to_domain(model: FamilyBranch) -> FamilyBranchData:
        return FamilyBranchData(model.id, model.family_id, model.branch_name, model.founder_id, model.description)


class MemberMapper:
    @staticmethod
    def to_domain(model: FamilyMember) -> FamilyMemberData:
        return FamilyMemberData(model.id, model.family_id, model.full_name, model.branch_id, model.user_id,
                                 model.gender, model.date_of_birth, model.date_of_death, model.is_alive, model.status)


class RelationshipMapper:
    @staticmethod
    def to_domain(model: Relationship) -> RelationshipData:
        return RelationshipData(model.id, model.from_member_id, model.to_member_id, model.type, model.notes)
