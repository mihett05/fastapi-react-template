class EntityNotFound(Exception):
    def __init__(self, cls: type) -> None:
        super().__init__(f"{cls.__name__} wasn't found")
