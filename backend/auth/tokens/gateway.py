from abc import ABCMeta, abstractmethod
from .dtos import TokenPairDto, TokenInfo


class TokensGateway(metaclass=ABCMeta):
    @abstractmethod
    async def create_token_pair(self, subject: str) -> TokenPairDto: ...

    @abstractmethod
    async def extract_token_info(
        self, token: str, check_expires: bool = True
    ) -> TokenInfo: ...
