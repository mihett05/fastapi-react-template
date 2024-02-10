from typing import Optional

from fastapi import APIRouter, FastAPI, WebSocket
from pydantic import ValidationError

from ws.events import handlers
from ws.managers import ConnectionManager
from ws.models import Request, EventType, WSUserData

router = APIRouter()
connect_manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    user_data: Optional[WSUserData] = None

    while True:
        data = await websocket.receive_json()
        try:
            event = Request(**data).event_type
            resp = await handlers[event].run(
                data=data,
                event=event,
                manager=connect_manager,
                websocket=websocket,
                user_data=user_data
            )
            if event == EventType.AUTH:
                user_data = resp

        except (ValidationError, ValueError) as err:
            await websocket.send_json({"error": f"Invalid request\nMore Info:\n({err})"})
