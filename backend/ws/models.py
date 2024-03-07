from dataclasses import dataclass
from enum import Enum

from fastapi import WebSocket
from pydantic import BaseModel

from auth.models import UserRead
from auth.schemas import User


class EventType(str, Enum):
    AUTH: str = "AUTH"
    MESSAGE: str = "MESSAGES"
    NOTIFICATION: str = "NOTIFICATION"
    # e.t.c.


class Request(BaseModel):
    event_type: EventType


class Response(BaseModel):
    user: UserRead
    event_type: EventType
    # some addition fields


@dataclass
class WSUserData:
    user: User
    websocket: WebSocket
