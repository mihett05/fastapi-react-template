from core.pydantic import PydanticModel
from users.schemas import UserRead


class MessageCreate(PydanticModel):
    chat_id: int
    sender_id: int
    message_text: str


class MessageRead(PydanticModel):
    id: int
    chat_id: int
    receiver_id: int
    sender_id: int
    message_text: str


class ChatRead(PydanticModel):
    id: int
    name: str

    members: list[UserRead]
    messages: list[MessageRead]


class ChatCreate(PydanticModel):
    name: str
    members: list[int]
