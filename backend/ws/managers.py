from typing import List

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def add(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def remove(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
