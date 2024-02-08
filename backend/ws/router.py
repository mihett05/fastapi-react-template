from fastapi import APIRouter, FastAPI, WebSocket
from pydantic import ValidationError

from ws.deps import handlers
from ws.managers import ConnectionManager
from ws.models import Request, EventType

router = APIRouter()
connect_manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # uid = ...
    # await connect_manager.add(uid, websocket)

    while True:
        data = await websocket.receive_json()
        try:
            event = Request(**data).event
            await handlers[event].run(
                data=data,
                event=event,
                manager=connect_manager,
                websocket=websocket,
                event_data=None
            )

        except ValidationError:
            await websocket.send_json({"error": "Invalid request"})
        # await websocket.send_text(f"Message text was: {data}")


