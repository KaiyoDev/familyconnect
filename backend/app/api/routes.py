from fastapi import APIRouter
from backend.app.api.controllers.community_controller import router as community_router

api_router = APIRouter()
api_router.include_router(community_router)
