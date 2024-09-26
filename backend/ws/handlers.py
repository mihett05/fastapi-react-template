from inspect import getfullargspec
from typing import Callable, Optional

from fastapi import WebSocket

from auth.tokens import TokensGateway
from users.repository import UsersRepository
from ws.managers import ConnectionManager
from ws.schemas import EventTypeRequest, Request, Response, WSUserData


class SendResponse:
    def __init__(self, request: Request, websocket: WebSocket):
        self.request = request
        self.websocket = websocket

    def update_response(self, response: Response):
        # response.uuid = self.request.uuid
        pass

    async def send(self, response: Response):
        self.update_response(response)
        await self.websocket.send_text(response.model_dump_json())


class EventHandler:
    def __init__(self, event: str):
        self.type = event
        self.request_type = None
        self.response_type = None
        self.handlers = []

    def request(self, cls):
        self.request_type = cls
        return cls

    def response(self, cls):
        self.response_type = cls
        return cls

    def handler(self, func: Callable):
        self.handlers.append(func)
        return func

    async def run(
        self,
        data: dict,
        event: EventTypeRequest,
        websocket: WebSocket,
        manager: ConnectionManager,
        tokens_gateway: TokensGateway,
        users_repository: UsersRepository,
        user_data: Optional[WSUserData] = None,
    ):
        if event != self.type:
            return

        if event != EventTypeRequest.AUTH and user_data is None:
            raise ValueError(f"Permission denied (user should be authorized)")

        if not self.request_type or not issubclass(self.request_type, (Request,)):
            raise ValueError(f"'{self.type}' handler has invalid 'request_type'")

        request = self.request_type(**data)
        send_response = SendResponse(request, websocket)

        deps = {
            self.request_type: request,
            WebSocket: websocket,
            WSUserData: user_data,
            SendResponse: send_response,
            ConnectionManager: manager,
            TokensGateway: tokens_gateway,
            UsersRepository: users_repository,
        }

        for handler in self.handlers:
            annotations = getfullargspec(handler).annotations
            _ = annotations.pop("return", None)
            kwargs = {}

            for arg, t in annotations.items():
                for cls in deps:
                    if issubclass(t, cls):
                        kwargs[arg] = deps[cls]
            return await handler(**kwargs)
            # asyncio.create_task(handler(**kwargs))
