from messenger.exceptions import ChatPermissionDenied
from messenger.models import Chat
from messenger.repository import ChatsRepository
from messenger.schemas import ChatCreate, ChatUpdate, ChatDelete
from users.models import User


async def get_chat_uc(chat_id: int, user: User, *, repo: ChatsRepository) -> Chat:
    chat = await repo.get(chat_id)
    if user not in chat.members:
        raise ChatPermissionDenied()
    return chat


async def get_chats_uc(user: User, *, repo: ChatsRepository) -> list[Chat]:
    return await repo.get_list(user)


async def create_chat_uc(dto: ChatCreate, *, repo: ChatsRepository) -> Chat:
    return await repo.add(dto)


async def update_chat_uc(dto: ChatUpdate, *, repo: ChatsRepository) -> Chat:
    pass


async def delete_chat_uc(dto: ChatDelete, *, repo: ChatsRepository) -> Chat:
    pass
