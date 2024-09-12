from users.models import Profile, User
from users.repository import ProfilesRepository
from users.schemas import ProfileCreate, ProfileUpdate


async def create_profile_usc(
        dto: ProfileCreate,
        user: User,
        *,
        profile_repository: ProfilesRepository
) -> Profile:
    return await profile_repository.add(dto, user)


async def update_profile_usc(
        dto: ProfileUpdate,
        user: User,
        *,
        profile_repository: ProfilesRepository
) -> Profile:
    return await profile_repository.update(dto, user)


async def delete_profile_usc(
        user: User,
        *,
        profile_repository: ProfilesRepository
) -> Profile:
    return await profile_repository.delete(user)
