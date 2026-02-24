from fastapi import HTTPException
from app.schemas.user import UserCreate
from app.infrastructure.repositories.user_repo import UserRepository
import hashlib


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def create_user(self, data: UserCreate):
        existing = await self.repo.get_by_email(data.email)
        if existing:
            raise HTTPException(status_code=409, detail="Email already exists")

        hashed = hashlib.sha256(data.password.encode()).hexdigest()
        return await self.repo.create(
            email=data.email,
            full_name=data.full_name,
            hashed_password=hashed,
        )

    async def get_user(self, user_id: int):
        user = await self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
