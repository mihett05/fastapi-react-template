from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.repository import BaseRepository
from messenger.models import Message, Chat
from messenger.schemas import MessageCreate, ChatCreate, ChatUpdate
from users.models import User
from .exceptions import MessageNotFound, ChatNotFound


class MessagesRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, message_id: int) -> Message:
        if message := await self.session.get(Message, message_id):
            return message  # type: ignore
        raise MessageNotFound()

    async def get_by_chat(self, chat_id: int) -> list[Message]:
        if messages := (
            await self.session.scalars(
                select(Message).where(Message.chat_id == chat_id)  # type: ignore
            )
        ).all():
            return messages  # type: ignore
        raise MessageNotFound()

    async def get_by_user(self, user_id: int) -> list[Message]:
        if messages := (
            await self.session.scalars(
                select(Message).where(Message.receiver_id == user_id)  # type: ignore
            )
        ).all():
            return messages  # type: ignore
        raise MessageNotFound()

    async def add(self, message: MessageCreate) -> Message:
        model = Message(
            chat_id=message.chat_id,
            sender_id=message.sender_id,
            message_text=message.message_text,
        )
        self.session.add(model)
        await self.session.commit()
        return model

    async def delete(self, message: Message):
        await self.session.delete(message)
        await self.session.commit()


class ChatsRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, chat_id: int) -> Chat:
        if chat := await self.session.get(
            Chat,
            chat_id,
            options=[
                selectinload(Chat.members).selectinload(User.profile),
                selectinload(Chat.messages),
            ],
        ):
            return chat  # type: ignore
        raise ChatNotFound()

    async def get_list(self, user: User) -> list[Chat]:
        if chats := (
            await self.session.scalars(
                select(Chat)
                .where(Chat.members.contains(user))
                .options(
                    selectinload(Chat.members).selectinload(User.profile),
                    selectinload(Chat.messages),
                )
            )
        ).all():
            return chats  # type: ignore
        raise ChatNotFound()

    async def add(self, model: Chat) -> Chat:
        self.session.add(model)
        await self.session.commit()

        return model

    async def update_attrs(self, model: Chat, dto: ChatUpdate) -> Chat:
        model = await self.update_model_attrs(model, dto)

        self.session.add(model)
        await self.session.commit()

        return model  # type: ignore

    async def update_members(self, model: Chat, members: set[User]) -> Chat:
        model.members.clear()
        model.members.update(members)

        self.session.add(model)
        await self.session.commit()

        return model

    async def delete(self, chat: Chat):
        await self.session.delete(chat)
        await self.session.commit()
