from users.models import Profile, User
from users.repository import ProfilesRepository
from users.schemas import ProfileCreate, ProfileUpdate


async def get_profile_uc(user: User) -> Profile:
    return await ProfilesRepository.get_by_user(user)


async def create_profile_uc(
    dto: ProfileCreate, user: User, *, repo: ProfilesRepository
) -> Profile:
    return await repo.add(dto, user)


async def update_profile_uc(
    dto: ProfileUpdate, user: User, *, repo: ProfilesRepository
) -> Profile:
    return await repo.update(dto, user)


async def delete_profile_uc(user: User, *, repo: ProfilesRepository) -> Profile:
    return await repo.delete(user)
