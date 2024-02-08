from typing import Dict

from . import auth
from ..handlers import EventHandler
from ..models import EventType

_handlers = [auth.auth_handler]
handlers: Dict[EventType, EventHandler] = {handler.type: handler for handler in _handlers}