from typing import Annotated

from fastapi import APIRouter, Depends

from auth.deps import get_current_user
from auth.schemas import UserRead
from users.deps import get_profiles_repository
from users.mappers import user_mapper, profile_mapper_default as profile_mapper
from users.models import User
from users.repository import ProfilesRepository
from users.schemas import ProfileRead, ProfileCreate, ProfileUpdate
from users.usecases.profiles import (
    create_profile_usc,
    update_profile_usc,
    delete_profile_usc,
    get_profile_usc,
)

router = APIRouter()


@router.get("/me", response_model=UserRead)
async def get_user(
    user: Annotated[User, Depends(get_current_user)],
):
    return user_mapper(user)


@router.get("/profile", response_model=ProfileRead)
async def get_profile(
    user: Annotated[User, Depends(get_current_user)],
):
    profile = await get_profile_usc(user)
    return profile_mapper(profile)


@router.post("/profile", response_model=ProfileRead)
async def create_profile(
    dto: ProfileCreate,
    user: Annotated[User, Depends(get_current_user)],
    profile_repository: Annotated[ProfilesRepository, Depends(get_profiles_repository)],
):
    profile = await create_profile_usc(dto, user, profile_repository=profile_repository)
    return profile_mapper(profile)


@router.patch("/profile", response_model=ProfileRead)
async def update_profile(
    dto: ProfileUpdate,
    user: Annotated[User, Depends(get_current_user)],
    profile_repository: Annotated[ProfilesRepository, Depends(get_profiles_repository)],
):
    profile = await update_profile_usc(dto, user, profile_repository=profile_repository)
    return profile_mapper(profile)


@router.delete("/profile", response_model=ProfileRead)
async def delete_profile(
    user: Annotated[User, Depends(get_current_user)],
    profile_repository: Annotated[ProfilesRepository, Depends(get_profiles_repository)],
):
    profile = await delete_profile_usc(user, profile_repository=profile_repository)
    return profile_mapper(profile)
