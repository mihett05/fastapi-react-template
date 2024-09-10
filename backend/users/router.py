from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from auth.deps import get_current_user
from auth.mappers import user_mapper
from auth.models import User
from auth.schemas import UserRead

router = APIRouter()


@router.get("/me", response_model=UserRead)
async def get_user(
        user: Annotated[User, Depends(get_current_user)],
):
    return JSONResponse(content=user_mapper(user).model_dump(by_alias=True))

