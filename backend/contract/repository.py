from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from contract.exceptions import ContractNotFound
from contract.models import Contract
from contract.schemas import ContractCreate
from users.models import User


class ContractsRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, contract_id: int) -> Contract:
        if contract := await self.session.get(
            Contract,
            contract_id,
            options=[
                selectinload(Contract.chat),
                selectinload(Contract.customer),
                selectinload(Contract.contractor),
            ],
        ):
            return contract
        raise ContractNotFound()

    async def add(self, dto: ContractCreate, user: User) -> Contract:
        model = Contract(customer_id=user.id, contractor_id=dto.contractor_id)
        self.session.add(model)
        await self.session.commit()

        return await self.get(model.id)

    async def delete(self, contract: Contract):
        await self.session.delete(contract)
        await self.session.commit()

    async def update(self, contract: Contract):
        self.session.add(contract)
        await self.session.commit()
