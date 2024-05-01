from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

# from src.api.schemas.product import ProductCreate
from src.api.schemas.limit_schema import LimitInfo
from src.domain.exceptions import not_found_exception
# from src.infrastructure.models.product import Product
from src.infrastructure.repositories.contract_repo import ContractRepo
from src.infrastructure.repositories.dmtt_repo import DmttRepo
from src.infrastructure.repositories.product_repo import ProductRepo
from src.infrastructure.services.excel_service import SheetDataFetcher


class LimitService():
    name_column = 1
    measure_column = 2
    limit_column = 3  # Обратите внимание на исправление опечатки в 'Limit'
    count_column = -1

    def __init__(self) -> None:
        self._sheet_data_fetcher = SheetDataFetcher()
        self._dmtt_repo = DmttRepo()
        self._contract_repo = ContractRepo()
        self._product_repo = ProductRepo()

    async def get_limit_by_dmtt(self, manager, company_id):
        dmtt_instance = await self._dmtt_repo.filter_one(user_id=manager.id)
        if not dmtt_instance:
            raise not_found_exception("Dmtt")
        contract = await self._contract_repo.filter_one(company_id=company_id, dmtt_id=dmtt_instance.id)
        if not contract:
            raise not_found_exception("Contract")

        data = await self._sheet_data_fetcher.get_data(sheet_url=contract.excel_url, sheet_name=contract.active_sheet_name)

        # Преобразование данных в список объектов LimitInfo
        limit_info_list = []

        for index, row in enumerate(data):
            name = row[self.name_column]
            measure = row[self.measure_column]
            limit = row[self.limit_column]
            count = row[self.count_column]
            if index == 0:
                continue
            product = await self._product_repo.get_or_create(name, measure)

            limit_info = LimitInfo(
                name=name,
                measure=measure,
                limit=limit,
                count=count,
                image_url=product.image_url
            )
            limit_info_list.append(limit_info)
        return limit_info_list
