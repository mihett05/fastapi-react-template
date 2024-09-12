from starlette.websockets import WebSocket

from auth.tokens import TokensGateway
from users.mappers import user_mapper
from users.repository import UsersRepository
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
        manager: ConnectionManager,

        tokens_gateway: TokensGateway,
        users_repository: UsersRepository,
):
    info = await tokens_gateway.extract_token_info(request.access_token)
    user = await users_repository.get_by_email(info.subject)

    user_read = user_mapper(user).model_dump(by_alias=True)
    user_data = manager.add(user_read, websocket)
    response = UpdateAuthResponse(user=user_read, event_type=request.event_type)

    await sender.send(response)

    return user_data
