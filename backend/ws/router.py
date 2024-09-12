from typing import Optional, Annotated

from fastapi import APIRouter, FastAPI, WebSocket, Depends
from pydantic import ValidationError

from auth.deps import get_tokens
from auth.tokens import TokensGateway
from users.deps import get_users_repository
from users.repository import UsersRepository
from ws.events import handlers
from ws.managers import ConnectionManager
from ws.schemas import Request, EventType, WSUserData

router = APIRouter()
connect_manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    tokens_gateway: Annotated[TokensGateway, Depends(get_tokens)],
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
):
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
                user_data=user_data,
                tokens_gateway=tokens_gateway,
                users_repository=users_repository,
            )
            if event == EventType.AUTH:
                user_data = resp

        except (ValidationError, ValueError) as err:
            await websocket.send_json(
                {"error": f"Invalid request\nMore Info:\n({err})"}
            )
