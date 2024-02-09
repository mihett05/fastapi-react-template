from inspect import getfullargspec
from typing import Callable, Dict, Optional, Any

from fastapi import WebSocket
from pydantic import ValidationError

from auth.deps import fastapi_users
from auth.models import UserRead
from ws.managers import ConnectionManager
from ws.models import EventType, Request, Response, WSUserData


class SendResponse:
    def __init__(self, request: Request, websocket: WebSocket):
        self.request = request
        self.websocket = websocket

    def update_response(self, response: Response):
        response.user = UserRead(**fastapi_users.get_user_manager().get(self.request.uid).__dict__)
        response.event_type = self.request.event_type

    async def send(self, response: Response):
        self.update_response(response)
        await self.websocket.send_text(response.model_dump_json())


class EventHandler:
    def __init__(self, event_type: EventType):
        self.type = event_type
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
            event: EventType,
            websocket: WebSocket,
            manager: ConnectionManager,
            user_data: Optional[WSUserData] = None,
    ):
        if event != self.type:
            return

        if event != EventType.AUTH and (user_data is None or manager.is_user_authenticated(user_data.user)):
            raise ValidationError(f"Permission denied (user should be authorized)")

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
