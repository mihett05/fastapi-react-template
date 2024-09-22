from messenger.exceptions import MessageNotFound, MessagePermissionDenied
from messenger.models import Message
from messenger.repository import MessagesRepository
from messenger.schemas import MessageCreate, MessageUpdate
from users.models import User


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
