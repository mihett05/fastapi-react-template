from typing import Annotated

from fastapi import APIRouter, Depends

from contract.deps import get_contracts_repository
from contract.mappers import contract_mapper
from contract.repository import ContractsRepository
from contract.schemas import ContractRead, ContractCreate

router = APIRouter()


@router.get("/contract/{contract_id}", response_model=ContractRead)
async def get_contract(
    contract_id: int, contracts_repository: Annotated[ContractsRepository, Depends(get_contracts_repository)]
):
    return contract_mapper(await contracts_repository.get(contract_id))


@router.post("/contract", response_model=ContractRead)
async def create_contract(
    dto: ContractCreate, contract_repository: Annotated[ContractsRepository, Depends(get_contracts_repository)]
):
    contract = await contract_repository.add(dto)
    return contract_mapper(contract)


@router.delete("/contract/{contract_id}", response_model=ContractRead)
async def delete_contract(
    contract_id: int, contract_repository: Annotated[ContractsRepository, Depends(get_contracts_repository)]
):
    contract = await contract_repository.get(contract_id)
    await contract_repository.delete(contract)
    return contract_mapper(contract)


@router.put("/contract/{contract_id}", response_model=ContractRead)
async def update_contract(
        contract_id: int, contract_repository: Annotated[ContractsRepository, Depends(get_contracts_repository)]
):
    contract = await contract_repository.get(contract_id)
    await contract_repository.update(contract)
    return contract_mapper(contract)
