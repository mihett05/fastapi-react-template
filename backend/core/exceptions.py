class EntityNotFound(Exception):
    def __init__(self, cls: type) -> None:
        super().__init__(f"{cls.__name__} wasn't found")


class PermissionDenied(Exception):
    def __init__(self, cls: type) -> None:
        super().__init__(
            f"The current user does not have enough rights "
            f"to work with the requested object. Requested {cls.__name__}"
        )
