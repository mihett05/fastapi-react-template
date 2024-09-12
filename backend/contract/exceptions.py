from core.exceptions import EntityNotFound

from contract.models import Contract


class ContractNotFound(EntityNotFound):

    def __init__(self):
        super().__init__(Contract)
