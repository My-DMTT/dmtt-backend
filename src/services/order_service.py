from typing import List

import requests

from src.api.schemas.order_schema import ListOrderCreate, OrderCreate
from src.domain.constants import BOT_API_URL
from src.domain.exceptions import not_found_exception
from src.infrastructure.models.order import OrderStatus
from src.infrastructure.repositories.company_repo import CompanyRepo
from src.infrastructure.repositories.contract_repo import ContractRepo
from src.infrastructure.repositories.dmtt_repo import DmttRepo
from src.infrastructure.repositories.order_repo import (OrderItemsRepo,
                                                        OrderRepo)
from src.infrastructure.repositories.product_repo import ProductRepo
from src.infrastructure.repositories.user_repo import UserRepo
from src.infrastructure.services.excel_service import (DataModel,
                                                       SheetDataFetcher)


class OrderService():
    def __init__(self) -> None:
        self._order_repo = OrderRepo()
        self._product_repo = ProductRepo()
        self._dmtt_repo = DmttRepo()
        self._user_repo = UserRepo()
        self._company_repo = CompanyRepo()
        self._spread_service = SheetDataFetcher()
        self._contract_repo = ContractRepo
        self._order_items_repo = OrderItemsRepo()

    async def create_order_with_items(self, user_id, order_data_list: List[OrderCreate]):
        dmtt = await self._dmtt_repo.filter_one(user_id=user_id)
        if not dmtt:
            raise not_found_exception("dmtt")

        company_items = {}
        for order_data in order_data_list:
            comp_id = order_data.company_id
            if not comp_id in company_items:
                company_items[comp_id] = []
            company_items[comp_id].append(
                {"product_name": order_data.product_name, "count": order_data.count})

        for company_id, order_data in company_items.items():
            company = await self._company_repo.get(company_id)
            if not company:
                raise not_found_exception("Company")
            new_order = await self._order_repo.create_order_with_items(dmtt.id, company_id, order_data)
            company_user = await self._user_repo.get(company.user_id)
            if company_user and company_user.tg_user_id:
                params = {
                    "msg": f"{dmtt.name} zakaz berdi \n Buyurtma raqami: {new_order.id}",
                    "user_id": company_user.tg_user_id,
                    "order_id": new_order.id
                }
                requests.post(f"{BOT_API_URL}/send-message/", params=params)
        return {"detail": "Ok"}

    async def change_order_status(self, order_id, status):
        await self._order_repo.change_status(order_id, status)
        if status == OrderStatus.ACCEPTED:
            order = await self._order_repo.get(order_id)
            if not order:
                raise not_found_exception("order")
            contract = await self._company_repo.filter_one(dmtt_id=order.dmtt_id, company_id=order.company_id)
            if not contract:
                return None
            data_list = []
            items = self._order_items_repo
            # await self._spread_service.add_data(

            # )

    async def get_order_by_id(self, order_id):
        return await self._order_repo.get_order_with_items(order_id)

    async def get_accepted_orders_with_items(self, user_id):
        return await self._order_repo.get_orders_by_status_with_items(user_id, OrderStatus.ACCEPTED)

    async def get_rejected_orders_with_items(self, user_id):
        return await self._order_repo.get_orders_by_status_with_items(user_id, OrderStatus.REJECTED)

    async def get_pending_orders_with_items(self, user_id):
        return await self._order_repo.get_orders_by_status_with_items(user_id, OrderStatus.PENDING)

    async def get_in_progress_orders_with_items(self, user_id):
        return await self._order_repo.get_orders_by_status_with_items(user_id, OrderStatus.IN_PROGRESS)


#

    async def get_accepted_orders_dmtt(self, user_id):
        return await self._order_repo.get_orders_by_status_dmtt(user_id, OrderStatus.ACCEPTED)

    async def get_rejected_orders_dmtt(self, user_id):
        return await self._order_repo.get_orders_by_status_dmtt(user_id, OrderStatus.REJECTED)

    async def get_pending_orders_dmtt(self, user_id):
        return await self._order_repo.get_orders_by_status_dmtt(user_id, OrderStatus.PENDING)

    async def get_in_progress_orders_dmtt(self, user_id):
        return await self._order_repo.get_orders_by_status_dmtt(user_id, OrderStatus.IN_PROGRESS)
