from fastapi import APIRouter
from app.api.controllers.auth_controller import router as auth_router

api_router = APIRouter(prefix="/api")
api_router.include_router(auth_router)