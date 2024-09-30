from dataclasses import dataclass
from enum import Enum
from typing import Optional, Any

from fastapi import WebSocket

from core.pydantic import PydanticModel
from users.models import User
from uuid import UUID


class EventTypeRequest(str, Enum):
    AUTH: str = "AUTH"


class EventTypeResponse(str, Enum):
    SUCCESS: str = "SUCCESS"
    FORBIDDEN: str = "FORBIDDEN"

    NEW_MESSAGE: str = "NEW_MESSAGE"
    UPDATED_MESSAGE: str = "UPDATED_MESSAGE"
    DELETED_MESSAGE: str = "UPDATED_MESSAGE"


class Request(PydanticModel):
    uuid: Optional[UUID] = None
    event: EventTypeRequest


class Response(PydanticModel):
    uuid: UUID
    event: EventTypeResponse
    data: Any = None


@dataclass
class WSUserData:
    user: User
    websocket: WebSocket
