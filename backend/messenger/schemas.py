from core.pydantic import PydanticModel


class MessageCreate(PydanticModel):
    chat_id: int
    user_to_id: int
    user_from_id: int
    message_text: str


class ChatCreate(PydanticModel):
    contract_id: int
