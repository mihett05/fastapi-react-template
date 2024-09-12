from datetime import datetime, timezone

import jwt

from auth.exceptions import InvalidCredentials

from .config import TokenConfig
from .dtos import TokenInfo, TokenPairDto
from .gateway import TokensGateway


class JwtTokensGateway(TokensGateway):
    def __init__(self, config: TokenConfig):
        self.config = config

    async def create_token_pair(self, subject: str) -> TokenPairDto:
        access_token = jwt.encode(
            {
                "exp": datetime.now(tz=timezone.utc) + self.config.access_token_expires_time,
                "sub": subject,
            },
            key=self.config.secret_key,
            algorithm=self.config.algorithm,
        )
        refresh_token = jwt.encode(
            {
                "exp": datetime.now(tz=timezone.utc) + self.config.refresh_token_expires_time,
                "sub": subject,
            },
            key=self.config.secret_key,
            algorithm=self.config.algorithm,
        )
        return TokenPairDto(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    async def extract_token_info(self, token: str, check_expires: bool = True) -> TokenInfo:
        try:
            payload = jwt.decode(
                token,
                key=self.config.secret_key,
                algorithms=[self.config.algorithm],
                options={"verify_signature": check_expires},
            )
        except jwt.ExpiredSignatureError:
            raise InvalidCredentials()

        return TokenInfo(
            subject=payload["sub"],
            expires_in=datetime.fromtimestamp(payload["exp"], tz=timezone.utc),
        )
