from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserOut
from app.domain.services.user_service import UserService
from app.api.deps import get_user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserOut, status_code=201)
async def create_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service),
):
    return await service.create_user(data)


@router.get("/{user_id}", response_model=UserOut)
async def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
):
    return await service.get_user(user_id)
