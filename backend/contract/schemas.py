from datetime import datetime
from typing import Optional

from core.pydantic import PydanticModel
from messenger.schemas import ChatRead
from users.schemas import UserRead


class ContractCreate(PydanticModel):
    contractor_id: int


class ContractRead(PydanticModel):
    id: int
    customer_id: int
    contractor_id: int

    updated_at: datetime
    created_at: datetime

    chat: Optional[ChatRead]
    customer: UserRead
    contractor: UserRead
