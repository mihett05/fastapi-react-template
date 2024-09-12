from core.exceptions import EntityNotFound

from .models import User, Profile


class UserNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(User)


class ProfileNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(Profile)
