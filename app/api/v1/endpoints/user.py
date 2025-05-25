# Sample endpoint
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_users():
    return ["user1", "user2"]
