from copy import copy
from typing import Iterable

from messenger.exceptions import ChatPermissionDenied
from messenger.models import Chat
from messenger.repository import ChatsRepository
from messenger.schemas import ChatCreate, ChatUpdate
from users.models import User


async def get_chat(chat_id: int, user: User, *, repository: ChatsRepository) -> Chat:
    chat = await repository.get(chat_id)
    if user not in chat.members:
        raise ChatPermissionDenied()

    return chat


async def get_chats(user: User, *, repository: ChatsRepository) -> Iterable[Chat]:
    return await repository.get_list(user)


async def create_chat(
    dto: ChatCreate, users: Iterable[User], *, repository: ChatsRepository
) -> Chat:
    return await repository.add(dto, users)


async def update_chat_attrs(
    chat: Chat,
    dto: ChatUpdate,
    *,
    repository: ChatsRepository,
) -> Chat:
    return await repository.update_attrs(chat, dto)


async def update_chat_members(
    chat: Chat,
    include: list[User],
    exclude: list[User],
    *,
    repository: ChatsRepository,
) -> Chat:
    users = copy(chat.members)
    users.update(include)
    for user in exclude:
        users.discard(user)

    return await repository.update_members(chat, users)


async def delete_chat(chat_id: int, user: User, *, repository: ChatsRepository) -> Chat:
    # TODO надо подумать, что делать с чатами,
    #  т.к. пользователей много и какой-то один не вправе удалять группу
    #  добавить права (?)
    chat = await get_chat(chat_id, user, repository=repository)
    await repository.delete(chat)
    return chat
