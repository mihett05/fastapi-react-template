from pydantic import ValidationError
from starlette.websockets import WebSocket

from auth.deps import get_jwt_strategy
from auth.managers import UserManager
from auth.models import UserRead
from auth.schemas import get_user_db, User
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
    # user: UserRead
    pass


@auth_handler.handler
async def handle(
        sender: SendResponse,
        websocket: WebSocket,
        request: UpdateAuthRequest,
        manager: ConnectionManager
):
    access_token = request.access_token

    # TODO fix this crutch hehehehe
    user_payload: User = await get_jwt_strategy().read_token(
        access_token, UserManager(await get_user_db().__anext__())
    )

    if user_payload is None:
        raise ValueError("Invalid access token")

    user_read = UserRead(**(user_payload.model_dump(mode='json')))
    user_data = manager.add(user_payload, websocket)
    response = UpdateAuthResponse(user=user_read, event_type=request.event_type)

    await sender.send(response)

    return user_data
