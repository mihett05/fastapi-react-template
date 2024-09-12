from dataclasses import dataclass
from enum import Enum

from fastapi import WebSocket
from pydantic import BaseModel

from core.pydantic import PydanticModel
from users.models import User
from users.schemas import UserRead


class EventType(str, Enum):
    AUTH: str = "AUTH"
    MESSAGE: str = "MESSAGES"
    NOTIFICATION: str = "NOTIFICATION"
    # e.t.c.


class Request(PydanticModel):
    event_type: EventType


class Response(PydanticModel):
    user: UserRead
    event_type: EventType
    # some addition fields


@dataclass
class WSUserData:
    user: User
    websocket: WebSocket
