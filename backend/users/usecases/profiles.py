from users.models import Profile, User
from users.repository import ProfilesRepository, UsersRepository
from users.schemas import ProfileCreate, ProfileUpdate


async def get_profile(user: User) -> Profile:
    return await ProfilesRepository.get_by_user(user)


async def create_profile(
    dto: ProfileCreate, user: User, *, repository: ProfilesRepository
) -> Profile:
    return await repository.add(dto, user)


async def update_profile(
    dto: ProfileUpdate, user: User, *, repository: ProfilesRepository
) -> Profile:
    return await repository.update(user, dto)


async def delete_profile(user: User, *, repository: ProfilesRepository) -> Profile:
    return await repository.delete(user)
