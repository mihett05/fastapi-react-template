from datetime import datetime

from core.pydantic import PydanticModel
from messenger.models import Chat, Message


class ContractCreate(PydanticModel):
    customer_id: int
    contractor_id: int
    chat_id: int
    chat: Chat


class ContractRead(PydanticModel):
    id: int
    customer_id: int
    contractor_id: int
    chat_id: int
    updated_at: datetime
    created_at: datetime
    chat: Chat