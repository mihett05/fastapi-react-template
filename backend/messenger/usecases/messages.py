from messenger.exceptions import MessageNotFound, MessagePermissionDenied
from messenger.models import Message, Chat
from messenger.repository import MessagesRepository
from messenger.schemas import MessageCreate, MessageUpdate, MessageReadWS
from users.models import User
from ws.managers import ConnectionManager, Singleton
from ws.schemas import EventTypeResponse, Response
from ws.usecases.updates import get_message_ws, get_response, send_message


async def get_message(
    message_id: int, chat_id: int, *, repository: MessagesRepository
) -> Message:
    message = await repository.get(message_id)
    if message.chat_id != chat_id:
        raise MessageNotFound()
    return message


async def create_message(
    dto: MessageCreate, user: User, *, repository: MessagesRepository
) -> Message:
    return await repository.add(dto, user)


async def send_message_notification(
    resp: Response, user: User, *, manager: ConnectionManager
):
    if socket := manager.get(user):
        await send_message(resp, socket=socket)


async def send_message_notifications(chat: Chat, user: User, *, response: Response):
    manager = Singleton.get()
    for member in chat.members:
        if member.id == user.id:
            continue
        await send_message_notification(response, member, manager=manager)


async def update_message(
    message: Message, dto: MessageUpdate, user: User, *, repository: MessagesRepository
) -> Message:
    if message.sender_id != user.id:
        raise MessagePermissionDenied()
    return await repository.update(message, dto)


async def delete_message(
    message: Message, user: User, *, repository: MessagesRepository
) -> Message:
    if message.sender_id != user.id:
        raise MessagePermissionDenied()
    return await repository.delete(message)
