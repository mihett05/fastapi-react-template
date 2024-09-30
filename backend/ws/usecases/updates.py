import uuid
from typing import Optional

from starlette.websockets import WebSocket

from messenger.models import Message
from messenger.schemas import MessageReadWS
from ws.schemas import EventTypeResponse, Response, Request


async def get_message_ws(message: Message) -> MessageReadWS:
    return MessageReadWS(id=message.id, chat_id=message.chat_id)


async def get_response(
    data: MessageReadWS, event: EventTypeResponse, *, request: Optional[Request] = None
) -> Response:
    return Response(
        uuid=request and request.uuid or uuid.uuid1(),
        event=event,
        data=data.model_dump(),
    )


async def send_message(resp: Response, *, socket: WebSocket):
    return await socket.send_json(resp.model_dump())
