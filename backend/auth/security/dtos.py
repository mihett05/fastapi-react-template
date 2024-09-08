from dataclasses import dataclass


@dataclass
class PasswordDto:
    hashed_password: str
    salt: str
