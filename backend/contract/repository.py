from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from contract.exceptions import ContractNotFound

from contract.models import Contract
from contract.schemas import ContractCreate


class ContractsRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, contract_id: int) -> Contract:
        if contract := await self.session.get(Contract, contract_id, options=[selectinload(Contract.chat, Contract.customer, Contract.contractor)]):
            return contract
        raise ContractNotFound()

    async def add(self, contract: ContractCreate) -> Contract:
        model = Contract(
            customer_id=contract.customer_id,
            contractor_id=contract.contractor_id,
            chat_id=contract.chat_id,
        )
        self.session.add(model)
        await self.session.commit()
        model.chat = None
        model.contractor = None
        model.customer = None
        return model

    async def delete(self, contract: Contract):
        await self.session.delete(contract)
        await self.session.commit()

    async def update(self, contract: Contract):
        self.session.add(contract)
        await self.session.commit()
