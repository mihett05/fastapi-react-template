from typing import Annotated

from fastapi import APIRouter, Depends

from auth.deps import get_current_user
from auth.schemas import UserRead
from users.deps import get_profiles_repository, get_users_repository
from users.models import User
from users.repository import ProfilesRepository, UsersRepository
from users.schemas import ProfileRead, ProfileCreate, ProfileUpdate
from users.usecases import (
    create_profile,
    update_profile,
    delete_profile,
    get_profile,
)
from users.usecases import get_all_users

router = APIRouter()


@router.get("/", response_model=list[UserRead])
async def get_users_handler(
    user: Annotated[User, Depends(get_current_user)],  # noqa
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
):
    return await get_all_users(repository=users_repository)


@router.get("/me", response_model=UserRead)
async def get_user_handler(
    user: Annotated[User, Depends(get_current_user)],
):
    return user


@router.get("/profile", response_model=ProfileRead)
async def get_profile_handler(
    user: Annotated[User, Depends(get_current_user)],
):
    return await get_profile(user)


@router.post("/profile", response_model=ProfileRead)
async def create_profile_handler(
    dto: ProfileCreate,
    user: Annotated[User, Depends(get_current_user)],
    profile_repository: Annotated[ProfilesRepository, Depends(get_profiles_repository)],
):
    return await create_profile(dto, user, repository=profile_repository)


@router.patch("/profile", response_model=ProfileRead)
async def update_profile_handler(
    dto: ProfileUpdate,
    user: Annotated[User, Depends(get_current_user)],
    profile_repository: Annotated[ProfilesRepository, Depends(get_profiles_repository)],
):
    return await update_profile(dto, user, repository=profile_repository)


@router.delete("/profile", response_model=ProfileRead)
async def delete_profile_handler(
    user: Annotated[User, Depends(get_current_user)],
    profile_repository: Annotated[ProfilesRepository, Depends(get_profiles_repository)],
):
    return await delete_profile(user, repository=profile_repository)
