from datetime import datetime
from typing import Optional

from core.pydantic import PydanticModel
from users.schemas import UserRead


class MessageCreate(PydanticModel):
    chat_id: int
    sender_id: int
    message_text: str


class MessageRead(PydanticModel):
    id: int
    chat_id: int
    sender_id: int
    created_at: datetime
    message_text: str


class ChatCreate(PydanticModel):
    name: str
    members: list[int]


class ChatRead(PydanticModel):
    id: int
    name: str

    members: list[UserRead]
    messages: list[MessageRead]


class ChatUpdate(PydanticModel):
    name: Optional[str] = None
    members: Optional[list[int]] = []
