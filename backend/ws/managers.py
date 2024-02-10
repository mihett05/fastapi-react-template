from typing import Dict, Tuple
from uuid import UUID

from beanie import PydanticObjectId
from fastapi import WebSocket

from auth.models import UserRead
from auth.schemas import User
from ws.models import WSUserData


class ConnectionManager:
    active_connections: Dict[PydanticObjectId, WSUserData] = {}

    def add(self, user: User, websocket: WebSocket):
        self.active_connections[user.id] = WSUserData(
            user=user,
            websocket=websocket,
        )

    def remove(self, user: User, websocket: WebSocket):
        if self.active_connections.get(user.id) is websocket:
            self.active_connections.pop(user.id)

    def is_user_authenticated(self, user: User):
        if user is None:
            return False
        return self.active_connections.get(user.id) is not None
