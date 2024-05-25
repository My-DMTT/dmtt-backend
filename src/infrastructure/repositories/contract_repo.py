from src.infrastructure.database.adapters.database import get_db
from src.infrastructure.models.company import Company
from src.infrastructure.models.contract import Contract
from src.infrastructure.repositories.base import CRUDRepoBase


class ContractRepo(CRUDRepoBase):
    model = Contract

    async def get_companies(self, dmtt_id):
        with get_db() as session:
            instance_list = session.query(Company).join(
                Contract, Contract.company_id == Company.id).filter(Contract.dmtt_id == dmtt_id).all()
            return instance_list

    async def get_contracts(self, user_id):
        with get_db() as session:
            instance_list = session.query(Contract).join(
                Company, Contract.company_id == Company.id).filter(Company.user_id == user_id).all()
            return instance_list
