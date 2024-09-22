from users.models import User
from users.repository import UsersRepository


async def get_all_users(repository: UsersRepository) -> list[User]:
    return await repository.get_all()


async def get_users(user_ids: list[int], repository: UsersRepository) -> list[User]:
    return await repository.get_list(user_ids)
