from src.api.endpoints import spy_cat
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(spy_cat.api_router, prefix="/spycat", tags=["SpyCat"])