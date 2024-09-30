import traceback
from typing import Optional, Annotated

from fastapi import APIRouter, WebSocket, Depends
from pydantic import ValidationError
from starlette.websockets import WebSocketDisconnect

from auth.deps import get_tokens
from auth.tokens import TokensGateway
from users.deps import get_users_repository
from users.repository import UsersRepository
from ws.events import handlers
from ws.schemas import Request, EventTypeRequest, WSUserData
from ws.managers import Singleton

router = APIRouter()


@router.websocket("")
async def websocket_endpoint(
    websocket: WebSocket,
    tokens_gateway: Annotated[TokensGateway, Depends(get_tokens)],
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
):
    connect_manager = Singleton.get()
    await websocket.accept()

    user_data: Optional[WSUserData] = None

    while True:
        try:
            data = await websocket.receive_json()
        except WebSocketDisconnect:
            connect_manager.remove(user_data.user, user_data.websocket)
            break

        try:
            event = Request(**data).event
            resp = await handlers[event].run(
                data=data,
                event=event,
                manager=connect_manager,
                websocket=websocket,
                user_data=user_data,
                tokens_gateway=tokens_gateway,
                users_repository=users_repository,
            )
            if event == EventTypeRequest.AUTH:
                user_data = resp

        except (ValidationError, ValueError) as err:
            print(traceback.format_exc())
            await websocket.send_json(
                {"error": f"Invalid request\nMore Info:\n({err})"}
            )
