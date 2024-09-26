from datetime import datetime
from typing import Optional

from core.pydantic import PydanticModel
from users.schemas import UserRead


class MessageCreate(PydanticModel):
    chat_id: int
    message_text: str


class MessageRead(PydanticModel):
    id: int
    chat_id: int
    sender_id: int
    modified_at: datetime
    message_text: str


class MessageReadWS(PydanticModel):
    id: int
    chat_id: int


class MessageUpdate(PydanticModel):
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
    include: Optional[list[int]] = []
    exclude: Optional[list[int]] = []
