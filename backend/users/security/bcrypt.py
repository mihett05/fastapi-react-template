import base64
import os

from passlib.context import CryptContext

from .dtos import PasswordDto
from .gateway import SecurityGateway


class BcryptSecurityGateway(SecurityGateway):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def create_salt(self) -> str:
        return base64.b64encode(os.urandom(32)).decode("utf-8")

    def create_hashed_password(self, password: str) -> PasswordDto:
        salt = self.create_salt()
        return PasswordDto(hashed_password=self.pwd_context.hash(password + salt), salt=salt)

    def verify_passwords(self, plain_password: str, hashed_password: PasswordDto) -> bool:
        return self.pwd_context.verify(plain_password + hashed_password.salt, hashed_password.hashed_password)
