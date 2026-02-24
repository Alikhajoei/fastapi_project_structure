from fastapi import APIRouter
from app.api.v1.endpoints.users import router as users_router

router = APIRouter()
router.include_router(users_router)
