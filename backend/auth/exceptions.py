class InvalidCredentials(Exception):
    def __init__(self) -> None:
        super().__init__("Invalid credentials were provided")
