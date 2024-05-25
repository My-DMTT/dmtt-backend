
from src.domain.exceptions import not_found_exception, user_not_found
from src.domain.models.dmtt_model import DmttCreate, DmttUpdate
from src.infrastructure.repositories.contract_repo import ContractRepo
from src.infrastructure.repositories.dmtt_repo import DmttRepo
from src.infrastructure.repositories.user_repo import UserRepo


class ContractService():
    def __init__(self):
        self._repo = ContractRepo()
        self._dmtt_repo = DmttRepo()
        self._user_repo = UserRepo()

    async def get_all_companies(self, user_id):
        dmtt = await self._dmtt_repo.filter_one(user_id=user_id)
        if not dmtt:
            raise not_found_exception("dmtt")

        return await self._repo.get_companies(dmtt_id=dmtt.id)

    async def get_all_contracts(self, user_id):
        return await self._repo.get_contracts(user_id)
