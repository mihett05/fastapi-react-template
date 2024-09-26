from starlette.websockets import WebSocket

from messenger.models import Message
from messenger.schemas import MessageReadWS
from ws.schemas import EventTypeResponse, Response


async def get_message_ws(message: Message) -> MessageReadWS:
    return MessageReadWS(id=message.id, chat_id=message.chat_id)


async def get_response(data: MessageReadWS, event: EventTypeResponse):
    return Response(event=event, data=data.model_dump())


async def send_message(resp: Response, *, socket: WebSocket):
    return await socket.send_json(resp.model_dump())
