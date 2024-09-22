from typing import Iterable

from messenger.exceptions import ChatPermissionDenied
from messenger.models import Chat
from messenger.repository import ChatsRepository
from messenger.schemas import ChatCreate, ChatUpdate
from users.models import User
from users.repository import UsersRepository
from users.usecases.users import get_users_uc


async def get_chat_uc(chat_id: int, user: User, *, repo: ChatsRepository) -> Chat:
    chat = await repo.get(chat_id)
    if user not in chat.members:
        raise ChatPermissionDenied()

    return chat


async def get_chats_uc(user: User, *, repo: ChatsRepository) -> Iterable[Chat]:
    return await repo.get_list(user)


async def create_chat_uc(
    dto: ChatCreate, *, repo: ChatsRepository, users_repo: UsersRepository
) -> Chat:
    users = await get_users_uc(dto.members, repo=users_repo)
    chat = Chat(name=dto.name, messages=[], members=users)  # type: ignore

    return await repo.add(chat)


async def update_chat_uc(
    chat_id: int,
    dto: ChatUpdate,
    user: User,
    *,
    repo: ChatsRepository,
    users_repo: UsersRepository
) -> Chat:
    chat = await get_chat_uc(chat_id, user, repo=repo)
    users = await get_users_uc(dto.members, repo=users_repo)
    model = await repo.update_model_attrs(chat, dto)

    model.members.update(users)  # type: ignore

    return await repo.update(model)  # type: ignore


async def delete_chat_uc(chat_id: int, user: User, *, repo: ChatsRepository) -> Chat:
    # TODO надо подумать, что делать с чатами,
    #  т.к. пользователей много и какой-то один не вправе удалять группу
    #  добавить права (?)
    chat = await get_chat_uc(chat_id, user, repo=repo)
    await repo.delete(chat)
    return chat
