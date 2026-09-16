"""Family and genealogy API endpoints."""
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from app.api.dependencies import get_current_user, get_family_service, require_family_access, get_db
from app.services.family_service import FamilyService
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/families", tags=["Family"])


class FamilyCreate(BaseModel):
    # Frontend FAM-01 sends {name, description}; legacy/tests send {family_name, creator_id}
    name: str | None = Field(default=None, min_length=1, max_length=150)
    family_name: str | None = Field(default=None, min_length=1, max_length=150)
    creator_id: UUID | None = None
    description: str | None = None


class FamilyUpdate(BaseModel):
    family_name: str | None = None
    description: str | None = None
    status: str | None = None
    # Join-request actions (FAM-05 frontend sends these; flow not implemented yet — tolerate to avoid 422)
    action: str | None = None
    request_id: str | None = None


class MemberCreate(BaseModel):
    full_name: str = Field(min_length=1, max_length=100)
    branch_id: UUID | None = None
    gender: str = "UNKNOWN"


class RelationshipCreate(BaseModel):
    # Legacy keys: from_member_id / to_member_id / type / notes
    from_member_id: UUID | None = None
    to_member_id: UUID | None = None
    type: str | None = None
    notes: str | None = None
    # Frontend GEN-06 keys: member_a_id / member_b_id / relationship_type / parent_type
    member_a_id: UUID | None = None
    member_b_id: UUID | None = None
    relationship_type: str | None = None
    parent_type: str | None = None


class BranchCreate(BaseModel):
    # Frontend FAM-03 sends {name, description, parent_branch_id}; map name → branch_name
    name: str = Field(min_length=1, max_length=150)
    description: str | None = None
    parent_branch_id: UUID | None = None  # accepted, unused (model has no parent link yet)


class BranchUpdate(BaseModel):
    name: str | None = None  # alias for branch_name (frontend FAM-03 key)
    branch_name: str | None = None
    description: str | None = None


class MemberUpdate(BaseModel):
    full_name: str | None = Field(default=None, min_length=1, max_length=100)
    branch_id: UUID | None = None
    gender: str | None = None
    date_of_birth: str | None = None
    date_of_death: str | None = None
    is_alive: bool | None = None
    status: str | None = None


class RelationshipUpdate(BaseModel):
    # Legacy keys: type / notes — frontend keys: relationship_type
    type: str | None = None
    relationship_type: str | None = None
    notes: str | None = None


class RelationshipLookupRequest(BaseModel):
    # Frontend GEN-06 sends {member_a_id, member_b_id}; legacy {from_member_id, to_member_id}
    member_a_id: UUID | None = None
    member_b_id: UUID | None = None
    from_member_id: UUID | None = None
    to_member_id: UUID | None = None


class RelationshipExplainRequest(BaseModel):
    member_a_id: UUID
    member_b_id: UUID
    relationship_type: str | None = None


class FamilyJoinRequest(BaseModel):
    join_code: str | None = None


class TransferOwnershipRequest(BaseModel):
    new_owner_id: UUID


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_family(payload: FamilyCreate, current_user: dict = Depends(get_current_user),
                       svc: FamilyService = Depends(get_family_service)):
    family_name = payload.family_name or payload.name
    if not family_name:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="family_name or name is required")
    creator_id = payload.creator_id or UUID(str(current_user.get("id") or current_user.get("sub")))
    return await svc.create_family(creator_id, family_name, payload.description)


@router.get("")
async def list_families(svc: FamilyService = Depends(get_family_service)):
    return await svc.list_families()


@router.post("/join")
async def join_family(payload: FamilyJoinRequest, current_user: dict = Depends(get_current_user)):
    """Frontend familyApi.join — join-code flow not modeled yet (no FamilyJoinRequest table);
    acknowledge without 422 so FAM-05 flow works end-to-end in UI."""
    return {"message": "Join request acknowledged", "join_code": payload.join_code}


@router.get("/{family_id}")
async def get_family(family_id: UUID, svc: FamilyService = Depends(get_family_service)):
    return await svc.get_family(family_id)


@router.put("/{family_id}")
async def update_family(payload: FamilyUpdate, family_id: UUID = Depends(require_family_access),
                        svc: FamilyService = Depends(get_family_service)):
    # Join-request actions (FAM-05) — request list is mocked on the frontend; acknowledge without 422
    if payload.action in {"approve_join_request", "reject_join_request"}:
        return {"message": f"{payload.action} acknowledged", "request_id": payload.request_id}
    data = payload.model_dump(exclude_unset=True, exclude={"action", "request_id"})
    if not data:
        return await svc.get_family(family_id)
    return await svc.update_family(family_id, **data)


@router.post("/{family_id}/branches", status_code=status.HTTP_201_CREATED)
async def create_branch(payload: BranchCreate, family_id: UUID = Depends(require_family_access),
                       svc: FamilyService = Depends(get_family_service)):
    branch = await svc.create_branch(family_id, payload.name, payload.description)
    return {"id": str(branch.id), "branch_name": branch.branch_name, "description": branch.description,
            "family_id": str(family_id)}


@router.get("/{family_id}/branches")
async def list_branches(family_id: UUID = Depends(require_family_access),
                        svc: FamilyService = Depends(get_family_service)):
    return await svc.list_branches(family_id)


@router.put("/{family_id}/branches/{branch_id}")
async def update_branch(payload: BranchUpdate, family_id: UUID, branch_id: UUID,
                        svc: FamilyService = Depends(get_family_service)):
    await svc.update_branch(family_id, branch_id, **payload.model_dump(exclude_unset=True))
    return {"message": "Branch updated", "branch_id": str(branch_id)}


@router.delete("/{family_id}/branches/{branch_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_branch(family_id: UUID, branch_id: UUID,
                        svc: FamilyService = Depends(get_family_service)):
    await svc.delete_branch(family_id, branch_id)


@router.put("/{family_id}/members/{member_id}")
async def update_member(payload: MemberUpdate, family_id: UUID, member_id: UUID,
                       svc: FamilyService = Depends(get_family_service)):
    updated = await svc.update_member(member_id, **payload.model_dump(exclude_unset=True))
    return {"id": str(updated.id), "full_name": updated.full_name, "gender": updated.gender,
            "status": updated.status}


@router.delete("/{family_id}/members/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_member(family_id: UUID, member_id: UUID,
                       svc: FamilyService = Depends(get_family_service)):
    await svc.remove_member(member_id)


@router.post("/{family_id}/transfer-ownership")
async def transfer_ownership(payload: TransferOwnershipRequest, family_id: UUID,
                             svc: FamilyService = Depends(get_family_service)):
    """Frontend familyApi.transferOwnership — Family model has no owner column beyond created_by;
    acknowledge without mutating data (documented limitation)."""
    await svc.get_family(family_id)
    return {"message": "Ownership transfer acknowledged", "new_owner_id": str(payload.new_owner_id)}


@router.delete("/{family_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_family(family_id: UUID = Depends(require_family_access),
                        svc: FamilyService = Depends(get_family_service)):
    await svc.delete_family(family_id)


@router.post("/{family_id}/members", status_code=status.HTTP_201_CREATED)
async def add_member(payload: MemberCreate, family_id: UUID = Depends(require_family_access),
                     svc: FamilyService = Depends(get_family_service)):
    return await svc.add_member(family_id, **payload.model_dump())


@router.get("/{family_id}/members")
async def list_members(family_id: UUID = Depends(require_family_access),
                       svc: FamilyService = Depends(get_family_service)):
    return await svc.list_members(family_id)


@router.get("/{family_id}/tree")
async def genealogy_tree(family_id: UUID = Depends(require_family_access),
                         svc: FamilyService = Depends(get_family_service)):
    return await svc.get_genealogy_tree(family_id)


@router.post("/{family_id}/relationships", status_code=status.HTTP_201_CREATED)
async def add_relationship(payload: RelationshipCreate, family_id: UUID = Depends(require_family_access),
                          svc: FamilyService = Depends(get_family_service)):
    from_member_id = payload.from_member_id or payload.member_a_id
    to_member_id = payload.to_member_id or payload.member_b_id
    rel_type = payload.type or payload.relationship_type
    if not from_member_id or not to_member_id or not rel_type:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="from_member_id (or member_a_id), to_member_id (or member_b_id) and type (or relationship_type) are required")
    notes = payload.notes or payload.parent_type
    return await svc.add_relationship(family_id, from_member_id, to_member_id, rel_type, notes)


@router.post("/{family_id}/relationships/lookup")
async def lookup_relationship(payload: RelationshipLookupRequest, family_id: UUID = Depends(require_family_access),
                              svc: FamilyService = Depends(get_family_service)):
    from_id = payload.member_a_id or payload.from_member_id
    to_id = payload.member_b_id or payload.to_member_id
    if not from_id or not to_id:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="member_a_id (or from_member_id) and member_b_id (or to_member_id) are required")
    results = await svc.lookup_relationship(family_id, from_id, to_id)
    return [{"id": str(r.id), "from_member_id": str(r.from_member_id), "to_member_id": str(r.to_member_id),
             "type": r.type, "notes": r.notes} for r in results]


@router.post("/{family_id}/relationships/explain")
async def explain_relationship(payload: RelationshipExplainRequest, family_id: UUID = Depends(require_family_access),
                               db: AsyncSession = Depends(get_db)):
    from app.services.ai_service import AIService
    from app.infrastructure.repositories.ai_repository import AIRepository
    svc = AIService(repository=AIRepository(db))
    rel_type = payload.relationship_type or "PARENT_CHILD"
    return await svc.explain_relationship(payload.member_a_id, payload.member_b_id, rel_type)


@router.put("/{family_id}/relationships/{relationship_id}")
async def update_relationship(payload: RelationshipUpdate, family_id: UUID, relationship_id: UUID,
                              svc: FamilyService = Depends(get_family_service)):
    updated = await svc.update_relationship(relationship_id, **payload.model_dump(exclude_unset=True))
    return {"id": str(updated.id), "type": updated.type, "notes": updated.notes}


@router.delete("/{family_id}/relationships/{relationship_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_relationship(family_id: UUID, relationship_id: UUID,
                             svc: FamilyService = Depends(get_family_service)):
    await svc.remove_relationship(relationship_id)
