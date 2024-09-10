from core.exceptions import EntityNotFound

from .models import User



class UserNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(User)
