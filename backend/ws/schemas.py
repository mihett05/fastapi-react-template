from dataclasses import dataclass
from enum import Enum
from typing import Optional, Any

from fastapi import WebSocket

from core.pydantic import PydanticModel
from users.models import User
from uuid import UUID


class EventTypeRequest(str, Enum):
    AUTH: str = "AUTH"
    GET_UPDATES: str = "GET_UPDATES"
    # e.t.c.


class EventTypeResponse(str, Enum):
    EMPTY: str = "EMPTY"
    SUCCESS: str = "SUCCESS"
    FORBIDDEN: str = "FORBIDDEN"
    NEW_MESSAGE: str = "NEW_MESSAGE"
    # e.t.c.


class Request(PydanticModel):
    # uuid: UUID
    event: EventTypeRequest


class Response(PydanticModel):
    # user: UserRead
    # uuid: UUID
    event: EventTypeResponse
    data: Any = None
    # some addition fields


@dataclass
class WSUserData:
    user: User
    websocket: WebSocket
