from typing import Optional

from fastapi_users.models import UserProtocol
from pydantic import ValidationError
from starlette.websockets import WebSocket

from auth.deps import get_jwt_strategy
from auth.managers import UserManager, get_user_manager
from auth.models import UserRead
from ws.handlers import EventHandler, SendResponse
from ws.managers import ConnectionManager
from ws.models import EventType, Request, Response

auth_handler = EventHandler(EventType.AUTH)


@auth_handler.request
class UpdateAuthRequest(Request):
    access_token: str
    event_type: EventType = EventType.AUTH


@auth_handler.response
class UpdateAuthResponse(Response):
    user: Optional[UserRead]


@auth_handler.handler
async def handle(
        sender: SendResponse,
        websocket: WebSocket,
        request: UpdateAuthRequest,
        manager: ConnectionManager
):
    access_token = request.access_token
    print(access_token)
    user_payload: UserProtocol = await get_jwt_strategy().read_token(access_token, await get_user_manager().__anext__())

    if user_payload is None:
        raise ValidationError("Invalid access token")

    user = UserRead(user_payload)
    user_data = await manager.add(user, websocket)

    response = UpdateAuthResponse(user)
    await sender.send(response)

    return user_data
