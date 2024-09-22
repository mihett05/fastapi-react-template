from typing import Iterable

from messenger.exceptions import ChatPermissionDenied
from messenger.models import Chat
from messenger.repository import ChatsRepository
from messenger.schemas import ChatCreate, ChatUpdate
from users.models import User
from users.repository import UsersRepository
from users.usecases.users import get_users


async def get_chat(chat_id: int, user: User, *, repository: ChatsRepository) -> Chat:
    chat = await repository.get(chat_id)
    if user not in chat.members:
        raise ChatPermissionDenied()

    return chat


async def get_chats(user: User, *, repository: ChatsRepository) -> Iterable[Chat]:
    return await repository.get_list(user)


async def create_chat(
    dto: ChatCreate, *, repository: ChatsRepository, users_repository: UsersRepository
) -> Chat:
    users = await get_users(dto.members, repository=users_repository)
    chat = Chat(name=dto.name, messages=[], members=users)  # type: ignore

    return await repository.add(chat)


async def update_chat(
    chat_id: int,
    dto: ChatUpdate,
    user: User,
    *,
    repository: ChatsRepository,
    users_repository: UsersRepository
) -> Chat:
    chat = await get_chat(chat_id, user, repository=repository)
    users = await get_users(dto.members, repository=users_repository)
    model = await repository.update_model_attrs(chat, dto)

    model.members.update(users)  # type: ignore

    return await repository.update(model)  # type: ignore


async def delete_chat(chat_id: int, user: User, *, repository: ChatsRepository) -> Chat:
    # TODO надо подумать, что делать с чатами,
    #  т.к. пользователей много и какой-то один не вправе удалять группу
    #  добавить права (?)
    chat = await get_chat(chat_id, user, repository=repository)
    await repository.delete(chat)
    return chat
