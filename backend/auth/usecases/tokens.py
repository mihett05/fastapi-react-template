from users.models import User
from auth.tokens.dtos import TokenPairDto
from auth.tokens.gateway import TokensGateway


async def create_token_pair(user: User, *, gateway: TokensGateway) -> TokenPairDto:
    return await gateway.create_token_pair(user.email)
