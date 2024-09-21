from core.pydantic import PydanticModel
from messenger.models import Chat, Message


class MessageCreate(PydanticModel):
    chat_id: int
    user_to_id: int
    user_from_id: int
    message_text: str


class MessageRead(PydanticModel):
    id: int
    chat_id: int
    receiver_id: int
    sender_id: int
    message_text: str


class ChatRead(PydanticModel):
    id: int
    messages: list[MessageRead]


class ChatCreate(PydanticModel):
    contract_id: int
