from enum import Enum

from pydantic import BaseModel

from auth.models import UserRead


class EventType(str, Enum):
    AUTH = "AUTH"
    MESSAGE = "MESSAGES"
    NOTIFICATION = "NOTIFICATION"
    # e.t.c.


class Request(BaseModel):
    event_type: EventType


class Response(BaseModel):
    user: UserRead
    event_type: EventType
    # some addition fields
