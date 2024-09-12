from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from contract.repository import ContractsRepository
from core.deps import get_session


async def get_contracts_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> ContractsRepository:
    return ContractsRepository(session)
