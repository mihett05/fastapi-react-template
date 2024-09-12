from contract.models import Contract
from contract.schemas import ContractRead
from core.mappers import sqlalchemy_retort

retort = sqlalchemy_retort.extend(recipe=[])

contract_mapper = retort.get_converter(Contract, ContractRead)


