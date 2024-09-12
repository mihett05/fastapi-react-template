from typing import Annotated

from fastapi import APIRouter, Depends

from auth.deps import get_current_user
from contract.deps import get_contracts_repository
from contract.mappers import contract_mapper
from contract.repository import ContractsRepository
from contract.schemas import ContractRead, ContractCreate
from messenger.deps import get_chats_repository
from messenger.repository import ChatsRepository
from messenger.schemas import ChatCreate
from users.models import User

router = APIRouter()


@router.get("/contract/{contract_id}", response_model=ContractRead)
async def get_contract(
    contract_id: int,
    contracts_repository: Annotated[ContractsRepository, Depends(get_contracts_repository)],
    user: Annotated[User, Depends(get_current_user)],
):
    return contract_mapper(await contracts_repository.get(contract_id))


@router.post("/contract", response_model=ContractRead)
async def create_contract(
    dto: ContractCreate,
    chat_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
    contract_repository: Annotated[ContractsRepository, Depends(get_contracts_repository)],
    user: Annotated[User, Depends(get_current_user)],
):
    contract = await contract_repository.add(dto, user)
    chat = await chat_repository.add_by_contract(contract)
    contract.chat = chat

    return contract_mapper(contract)


@router.delete("/contract/{contract_id}", response_model=ContractRead)
async def delete_contract(
    contract_id: int,
    contract_repository: Annotated[ContractsRepository, Depends(get_contracts_repository)],
    user: Annotated[User, Depends(get_current_user)],
):
    contract = await contract_repository.get(contract_id)
    await contract_repository.delete(contract)  
    return contract_mapper(contract)


@router.patch("/contract/{contract_id}", response_model=ContractRead)
async def update_contract(
    contract_id: int,
    contract_repository: Annotated[ContractsRepository, Depends(get_contracts_repository)],
    user: Annotated[User, Depends(get_current_user)],
):
    contract = await contract_repository.get(contract_id)
    await contract_repository.update(contract)
    return contract_mapper(contract)
