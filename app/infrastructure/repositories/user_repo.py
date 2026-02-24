from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.db.models.user_model import UserModel


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, user_id: int) -> UserModel | None:
        stmt = select(UserModel).where(UserModel.id == user_id)
        res = await self.db.execute(stmt)
        return res.scalar_one_or_none()

    async def get_by_email(self, email: str) -> UserModel | None:
        stmt = select(UserModel).where(UserModel.email == email)
        res = await self.db.execute(stmt)
        return res.scalar_one_or_none()

    async def create(
        self, email: str, full_name: str, hashed_password: str
    ) -> UserModel:
        obj = UserModel(
            email=email, full_name=full_name, hashed_password=hashed_password
        )
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj
