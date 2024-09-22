from typing import Annotated

from fastapi import APIRouter, Depends

from auth.deps import get_current_user
from auth.schemas import UserRead
from users.deps import get_profiles_repository, get_users_repository
from users.models import User
from users.repository import ProfilesRepository, UsersRepository
from users.schemas import ProfileRead, ProfileCreate, ProfileUpdate
from users.usecases.profiles import (
    create_profile_uc,
    update_profile_uc,
    delete_profile_uc,
    get_profile_uc,
)
from users.usecases.users import get_all_users_uc

router = APIRouter()


@router.get("/", response_model=list[UserRead])
async def get_user(
    user: Annotated[User, Depends(get_current_user)],  # noqa
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
):
    return await get_all_users_uc(repo=users_repository)


@router.get("/me", response_model=UserRead)
async def get_user(
    user: Annotated[User, Depends(get_current_user)],
):
    return user


@router.get("/profile", response_model=ProfileRead)
async def get_profile(
    user: Annotated[User, Depends(get_current_user)],
):
    return await get_profile_uc(user)


@router.post("/profile", response_model=ProfileRead)
async def create_profile(
    dto: ProfileCreate,
    user: Annotated[User, Depends(get_current_user)],
    profile_repository: Annotated[ProfilesRepository, Depends(get_profiles_repository)],
):
    return await create_profile_uc(dto, user, repo=profile_repository)


@router.patch("/profile", response_model=ProfileRead)
async def update_profile(
    dto: ProfileUpdate,
    user: Annotated[User, Depends(get_current_user)],
    profile_repository: Annotated[ProfilesRepository, Depends(get_profiles_repository)],
):
    return await update_profile_uc(dto, user, repo=profile_repository)


@router.delete("/profile", response_model=ProfileRead)
async def delete_profile(
    user: Annotated[User, Depends(get_current_user)],
    profile_repository: Annotated[ProfilesRepository, Depends(get_profiles_repository)],
):
    return await delete_profile_uc(user, repo=profile_repository)
