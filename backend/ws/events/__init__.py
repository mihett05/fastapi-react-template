from typing import Dict

from . import auth
from ..handlers import EventHandler
from ..schemas import EventTypeRequest

_handlers = [auth.auth_handler]
handlers: Dict[EventTypeRequest, EventHandler] = {
    handler.type: handler for handler in _handlers
}
