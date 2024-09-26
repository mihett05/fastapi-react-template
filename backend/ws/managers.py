from typing import Dict, Optional

from fastapi import WebSocket

from users.models import User
from ws.schemas import WSUserData


class ConnectionManager:
    active_connections: Dict[int, WSUserData] = {}

    def get(self, user: User) -> Optional[WebSocket]:
        socket = self.active_connections.get(user.id, None)
        return socket and socket.websocket

    def add(self, user: User, websocket: WebSocket):
        self.active_connections[user.id] = WSUserData(
            user=user,
            websocket=websocket,
        )

    def remove(self, user: User, websocket: WebSocket):
        if self.active_connections.get(user.id) is websocket:
            self.active_connections.pop(user.id)
