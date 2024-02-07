from enum import Enum
from typing import Union

from pydantic import BaseModel

from auth.models import UserRead


class EventType(Enum):
    ALL = "ALL"
    MESSAGES = "MESSAGES"
    NOTIFICATION = "NOTIFICATION"
    # e.t.c.


class Request(BaseModel):
    uid: Union[str, int]
    event_type: EventType


class Response(BaseModel):
    user: UserRead
    event_type: EventType
    # some addition field
