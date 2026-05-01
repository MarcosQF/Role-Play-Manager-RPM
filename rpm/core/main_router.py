from fastapi import APIRouter
from ..games.router import router as games_router

api_router = APIRouter(prefix="/api")

api_router.include_router(games_router)
