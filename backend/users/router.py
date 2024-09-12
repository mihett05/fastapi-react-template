from typing import Annotated

from fastapi import APIRouter, Depends

from auth.deps import get_current_user
from auth.schemas import UserRead
from users.mappers import user_mapper
from users.models import User

router = APIRouter()


@router.get("/me", response_model=UserRead)
async def get_user(
        user: Annotated[User, Depends(get_current_user)],
):
    return user_mapper(user)
