"""AI Assistant API controller — stub endpoints."""
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field

from app.api.dependencies import get_current_user
from app.infrastructure.databases.database import get_db
from app.infrastructure.repositories.ai_repository import AIRepository
from app.services.ai_service import AIService, NotFoundError, ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/ai", tags=["AI"])


# =========================================================
# REQUEST SCHEMAS
# =========================================================

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)


class SearchRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=500)
    family_id: UUID | None = None


class ExplainRelationshipRequest(BaseModel):
    member_a_id: UUID = Field(..., description="ID of the first member")
    member_b_id: UUID = Field(..., description="ID of the second member")
    relationship_type: str = Field(..., min_length=1, description="PARENT_CHILD | MARRIAGE")


class SummarizeRequest(BaseModel):
    content: str = Field(..., min_length=1)
    length: str = Field(default="medium", pattern="^(short|medium|full)$")


class CreateConversationRequest(BaseModel):
    title: str | None = Field(default=None, max_length=200)


# =========================================================
# DEPENDENCY
# =========================================================

def get_ai_service(db: AsyncSession = Depends(get_db)) -> AIService:
    return AIService(repository=AIRepository(db))


# =========================================================
# CONVERSATIONS
# =========================================================

@router.post("/conversations", status_code=status.HTTP_201_CREATED)
async def create_conversation(
    payload: CreateConversationRequest,
    current_user=Depends(get_current_user),
    service: AIService = Depends(get_ai_service),
):
    conv = await service.create_conversation(
        user_id=current_user["id"],
        title=payload.title,
    )
    return conv


@router.get("/conversations")
async def list_conversations(
    current_user=Depends(get_current_user),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
    service: AIService = Depends(get_ai_service),
):
    offset = (page - 1) * page_size
    conversations = await service.list_conversations(
        user_id=current_user["id"],
        limit=page_size,
        offset=offset,
    )
    return {
        "items": conversations,
        "page": page,
        "page_size": page_size,
        "count": len(conversations),
    }


@router.get("/conversations/{conversation_id}")
async def get_conversation(
    conversation_id: UUID,
    current_user=Depends(get_current_user),
    service: AIService = Depends(get_ai_service),
):
    try:
        return await service.get_conversation(conversation_id)
    except NotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@router.delete("/conversations/{conversation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_conversation(
    conversation_id: UUID,
    current_user=Depends(get_current_user),
    service: AIService = Depends(get_ai_service),
):
    try:
        await service.delete_conversation(conversation_id)
    except NotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


# =========================================================
# CHAT
# =========================================================

@router.post("/conversations/{conversation_id}/chat", status_code=status.HTTP_200_OK)
async def chat(
    conversation_id: UUID,
    payload: ChatRequest,
    current_user=Depends(get_current_user),
    service: AIService = Depends(get_ai_service),
):
    """Stub: returns a mock AI response for the given message."""
    try:
        result = await service.chat(
            conversation_id=conversation_id,
            user_id=current_user["id"],
            message=payload.message,
        )
        return result
    except NotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


# =========================================================
# SEMANTIC SEARCH
# =========================================================

@router.post("/search", status_code=status.HTTP_200_OK)
async def semantic_search(
    payload: SearchRequest,
    current_user=Depends(get_current_user),
    service: AIService = Depends(get_ai_service),
):
    """Stub: returns mock search results. Real implementation uses embedding + vector store."""
    results = await service.semantic_search(query=payload.query, family_id=payload.family_id)
    return {"query": payload.query, "results": results, "provider": "mock"}


# =========================================================
# EXPLAIN RELATIONSHIP
# =========================================================

@router.post("/explain-relationship", status_code=status.HTTP_200_OK)
async def explain_relationship(
    payload: ExplainRelationshipRequest,
    current_user=Depends(get_current_user),
    service: AIService = Depends(get_ai_service),
):
    """Stub: returns a natural-language explanation of the relationship between two members."""
    explanation = await service.explain_relationship(
        member_a_id=payload.member_a_id,
        member_b_id=payload.member_b_id,
        relationship_type=payload.relationship_type,
    )
    return explanation


# =========================================================
# SUMMARIZE
# =========================================================

@router.post("/summarize", status_code=status.HTTP_200_OK)
async def summarize(
    payload: SummarizeRequest,
    current_user=Depends(get_current_user),
    service: AIService = Depends(get_ai_service),
):
    """Stub: returns a mock summary of the given content."""
    try:
        result = await service.summarize(content=payload.content, length=payload.length)
        return result
    except ValidationError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
