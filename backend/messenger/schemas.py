from core.pydantic import PydanticModel
from models import Chat, Message


class MessageCreate(PydanticModel):
    chat_id: int
    user_to_id: int
    user_from_id: int
    message_text: str


class MessageRead(PydanticModel):
    id: int
    chat_id: int
    user_to_id: int
    user_from_id: int
    message_text: str


class ChatRead(PydanticModel):
    id: int
    contract_id: int
    messages: list[Message]


class ChatCreate(PydanticModel):
    contract_id: int
