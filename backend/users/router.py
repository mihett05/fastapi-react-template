from typing import List

from fastapi import APIRouter

from users.schemas import User

router = APIRouter()


@router.get(
    "/",
    response_model=List[User],
    response_description="Возвращает всех пользователей",
)
async def get_users():
    return await User.find_all().to_list()


@router.get(
    "/me",
    response_model=User,
    response_description="Возвращает активного пользователя",
)
async def get_users():
    return await User.find_all().to_list()

