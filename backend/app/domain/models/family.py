"""Framework-independent domain models and enums."""
from dataclasses import dataclass
from datetime import date
from enum import StrEnum
from uuid import UUID


class FamilyStatus(StrEnum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"


class MemberStatus(StrEnum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    DELETED = "DELETED"


class Gender(StrEnum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"


class RelationshipType(StrEnum):
    PARENT_CHILD = "PARENT_CHILD"
    MARRIAGE = "MARRIAGE"


@dataclass(slots=True)
class FamilyData:
    id: UUID
    family_name: str
    created_by: UUID
    description: str | None = None
    status: FamilyStatus = FamilyStatus.ACTIVE


@dataclass(slots=True)
class FamilyBranchData:
    id: UUID
    family_id: UUID
    branch_name: str
    founder_id: UUID | None = None
    description: str | None = None


@dataclass(slots=True)
class FamilyMemberData:
    id: UUID
    family_id: UUID
    full_name: str
    branch_id: UUID | None = None
    user_id: UUID | None = None
    gender: Gender = Gender.UNKNOWN
    date_of_birth: date | None = None
    date_of_death: date | None = None
    is_alive: bool = True
    status: MemberStatus = MemberStatus.PENDING


@dataclass(slots=True)
class RelationshipData:
    id: UUID
    from_member_id: UUID
    to_member_id: UUID
    type: RelationshipType
    notes: str | None = None
