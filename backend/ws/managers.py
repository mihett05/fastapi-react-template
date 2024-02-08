from typing import Dict, Tuple
from uuid import UUID

from fastapi import WebSocket

from auth.models import UserRead


class ConnectionManager:
    active_connections: Dict[UUID, Tuple[UserRead, WebSocket]] = {}

    def add(self, user: UserRead, websocket: WebSocket):
        self.active_connections[user.id] = (user, websocket)

    def remove(self, user: UserRead, websocket: WebSocket):
        if self.active_connections.get(user.id) is websocket:
            self.active_connections.pop(user.id)

    def is_user_authenticated(self, user: UserRead):
        if user is None:
            return False
        return self.active_connections.get(user.id) is not None
