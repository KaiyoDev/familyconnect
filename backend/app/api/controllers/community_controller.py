from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
)

from pydantic import BaseModel, Field

from app.services.community_service import (
    CommunityService,
    ConflictError,
    ForbiddenError,
    NotFoundError,
    ValidationError,
)

from app.infrastructure.repositories.post_repository import (
    PostRepository,
)

from app.infrastructure.repositories.comment_repository import (
    CommentRepository,
)

from app.infrastructure.repositories.reaction_repository import (
    ReactionRepository,
)

# =========================================================
# IMPORTANT:
# Đổi 2 import này nếu project của bạn dùng path khác.
# =========================================================

from app.infrastructure.databases.database import get_db
from app.api.dependencies import get_current_user


router = APIRouter(
    tags=["Community"]
)


# =========================================================
# SERVICE DEPENDENCY
# =========================================================

def get_community_service(
    db=Depends(get_db),
) -> CommunityService:

    return CommunityService(
        post_repository=PostRepository(db),
        comment_repository=CommentRepository(db),
        reaction_repository=ReactionRepository(db),
    )


# =========================================================
# REQUEST SCHEMAS
# =========================================================

class CreatePostRequest(BaseModel):

    content: str = Field(
        ...,
        min_length=1,
    )

    media_urls: list | None = None

    visibility_scope: str = "FAMILY"

    branch_id: UUID | None = None


class UpdatePostRequest(BaseModel):

    content: str | None = Field(
        default=None,
        min_length=1,
    )

    media_urls: list | None = None

    visibility_scope: str | None = None

    branch_id: UUID | None = None


class AddCommentRequest(BaseModel):

    content: str = Field(
        ...,
        min_length=1,
        max_length=1000,
    )


class AddReactionRequest(BaseModel):

    type: str = Field(
        ...,
        min_length=1,
        max_length=20,
    )


# =========================================================
# CREATE POST
# POST /api/families/{family_id}/posts
# =========================================================

@router.post(
    "/families/{family_id}/posts",
    status_code=status.HTTP_201_CREATED,
)
async def create_post(
    family_id: UUID,
    payload: CreatePostRequest,
    current_user=Depends(get_current_user),
    service: CommunityService = Depends(
        get_community_service
    ),
):

    try:

        return await service.create_post(
            family_id=family_id,
            author_id=current_user["id"],
            content=payload.content,
            media_urls=payload.media_urls,
            visibility_scope=payload.visibility_scope,
            branch_id=payload.branch_id,
        )

    except ValidationError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


# =========================================================
# GET FEED
# GET /api/families/{family_id}/feed
# =========================================================

@router.get(
    "/families/{family_id}/feed"
)
async def get_feed(
    family_id: UUID,

    page: int = Query(
        default=1,
        ge=1,
    ),

    page_size: int = Query(
        default=20,
        ge=1,
        le=100,
    ),

    service: CommunityService = Depends(
        get_community_service
    ),
):

    try:

        posts = await service.get_feed(
            family_id=family_id,
            page=page,
            page_size=page_size,
        )

        return {
            "items": posts,
            "page": page,
            "page_size": page_size,
            "count": len(posts),
        }

    except ValidationError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


# =========================================================
# GET POST
# GET /api/posts/{post_id}
# =========================================================

@router.get(
    "/posts/{post_id}"
)
async def get_post(
    post_id: UUID,

    service: CommunityService = Depends(
        get_community_service
    ),
):

    try:

        return await service.get_post(
            post_id=post_id
        )

    except NotFoundError as exc:

        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


# =========================================================
# UPDATE POST
# PUT /api/posts/{post_id}
# =========================================================

@router.put(
    "/posts/{post_id}"
)
async def update_post(
    post_id: UUID,

    payload: UpdatePostRequest,

    current_user=Depends(
        get_current_user
    ),

    service: CommunityService = Depends(
        get_community_service
    ),
):

    try:

        return await service.update_post(
            post_id=post_id,
            author_id=current_user["id"],
            content=payload.content,
            media_urls=payload.media_urls,
            visibility_scope=payload.visibility_scope,
            branch_id=payload.branch_id,
        )

    except NotFoundError as exc:

        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )

    except ForbiddenError as exc:

        raise HTTPException(
            status_code=403,
            detail=str(exc),
        )

    except ValidationError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


# =========================================================
# DELETE POST
# DELETE /api/posts/{post_id}
# =========================================================

@router.delete(
    "/posts/{post_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_post(
    post_id: UUID,

    current_user=Depends(
        get_current_user
    ),

    service: CommunityService = Depends(
        get_community_service
    ),
):

    try:

        await service.delete_post(
            post_id=post_id,
            current_user_id=current_user["id"],
        )

    except NotFoundError as exc:

        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )

    except ForbiddenError as exc:

        raise HTTPException(
            status_code=403,
            detail=str(exc),
        )


# =========================================================
# ADD COMMENT
# POST /api/posts/{post_id}/comments
# =========================================================

@router.post(
    "/posts/{post_id}/comments",
    status_code=status.HTTP_201_CREATED,
)
async def add_comment(
    post_id: UUID,

    payload: AddCommentRequest,

    current_user=Depends(
        get_current_user
    ),

    service: CommunityService = Depends(
        get_community_service
    ),
):

    try:

        return await service.add_comment(
            post_id=post_id,
            author_id=current_user["id"],
            content=payload.content,
        )

    except NotFoundError as exc:

        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )

    except ValidationError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


# =========================================================
# ADD REACTION
# POST /api/posts/{post_id}/reactions
# =========================================================

@router.post(
    "/posts/{post_id}/reactions",
    status_code=status.HTTP_201_CREATED,
)
async def add_reaction(
    post_id: UUID,

    payload: AddReactionRequest,

    current_user=Depends(
        get_current_user
    ),

    service: CommunityService = Depends(
        get_community_service
    ),
):

    try:

        return await service.add_reaction(
            post_id=post_id,
            user_id=current_user["id"],
            reaction_type=payload.type,
        )

    except NotFoundError as exc:

        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )

    except ValidationError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    except ConflictError as exc:

        raise HTTPException(
            status_code=409,
            detail=str(exc),
        )


# =========================================================
# REMOVE REACTION
# DELETE /api/posts/{post_id}/reactions?type=like
# =========================================================

@router.delete(
    "/posts/{post_id}/reactions",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def remove_reaction(
    post_id: UUID,

    type: str = Query(
        ...,
        min_length=1,
        max_length=20,
    ),

    current_user=Depends(
        get_current_user
    ),

    service: CommunityService = Depends(
        get_community_service
    ),
):

    try:

        await service.remove_reaction(
            post_id=post_id,
            user_id=current_user.id,
            reaction_type=type,
        )

    except NotFoundError as exc:

        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )

    except ValidationError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )