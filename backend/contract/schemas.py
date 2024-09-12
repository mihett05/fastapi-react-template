from datetime import datetime

from core.pydantic import PydanticModel
from messenger.schemas import ChatRead


class ContractCreate(PydanticModel):
    customer_id: int
    contractor_id: int
    chat_id: int
    chat: ChatRead


class ContractRead(PydanticModel):
    id: int
    customer_id: int
    contractor_id: int
    chat_id: int
    updated_at: datetime
    created_at: datetime
    chat: ChatRead
