from abc import ABCMeta, abstractmethod

from .dtos import PasswordDto


class SecurityGateway(metaclass=ABCMeta):
    @abstractmethod
    def create_salt(self) -> str: ...

    @abstractmethod
    def create_hashed_password(self, password: str) -> PasswordDto: ...

    @abstractmethod
    def verify_passwords(
        self, plain_password: str, hashed_password: PasswordDto
    ) -> bool: ...
