from users.models import User
from users.repository import UsersRepository


async def get_all_users_uc(repo: UsersRepository) -> list[User]:
    return await repo.get_all()


async def get_users_uc(user_ids: list[int], repo: UsersRepository) -> list[User]:
    return await repo.get_list(user_ids)
