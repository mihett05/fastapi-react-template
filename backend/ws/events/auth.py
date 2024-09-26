from starlette.websockets import WebSocket

from auth.tokens import TokensGateway
from users.repository import UsersRepository
from ws.handlers import EventHandler, SendResponse
from ws.managers import ConnectionManager
from ws.schemas import EventTypeRequest, Request, Response, EventTypeResponse

auth_handler = EventHandler(EventTypeRequest.AUTH)


@auth_handler.request
class UpdateAuthRequest(Request):
    access_token: str
    event: EventTypeRequest = EventTypeRequest.AUTH


@auth_handler.response
class UpdateAuthResponse(Response):
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

    user_data = manager.add(user, websocket)
    response = UpdateAuthResponse(event=EventTypeResponse.SUCCESS)

    await sender.send(response)

    return user_data
