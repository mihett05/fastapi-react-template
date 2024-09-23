from typing import Dict

from fastapi import WebSocket

from auth.schemas import UserRead
from users.models import User
from ws.schemas import WSUserData


class ConnectionManager:
    active_connections: Dict[int, WSUserData] = {}

    def add(self, user: User, websocket: WebSocket):
        self.active_connections[user.id] = WSUserData(
            user=user,
            websocket=websocket,
        )

    def remove(self, user: UserRead, websocket: WebSocket):
        if self.active_connections.get(user.id) is websocket:
            self.active_connections.pop(user.id)

    def is_user_authenticated(self, user: UserRead):
        if user is None:
            return False
        return self.active_connections.get(user.id) is not None
