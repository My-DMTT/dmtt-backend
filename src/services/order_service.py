from src.api.schemas.order_schema import ListOrderCreate
from src.domain.exceptions import not_found_exception
from src.infrastructure.models.order import OrderStatus
from src.infrastructure.repositories.order_repo import OrderRepo
from src.infrastructure.repositories.product_repo import ProductRepo


class OrderService():
    def __init__(self) -> None:
        self._order_repo = OrderRepo()
        self._product_repo = ProductRepo()

    async def create_order_with_items(self, order_data_list: ListOrderCreate):
        for order_data in order_data_list.data:
            for item in order_data.items:
                if not await self._product_exists(item.product_id):
                    raise not_found_exception(
                        f"Product ID {item.product_id} not found")

            await self._order_repo.create_order_with_items(order_data)
        return {"detail": "Ok"}

    async def _product_exists(self, product_id: int) -> bool:
        return await self._product_repo.is_exists(id=product_id)

    async def get_all_orders_with_items(self):
        return await self._order_repo.get_all_orders_with_items()

    # async def get_orders_by_status_with_items(self, status):
    #     return await self._order_repo.get_orders_by_status_with_items(status)

    async def get_accepted_orders_with_items(self):
        return await self.get_orders_by_status_with_items(OrderStatus.ACCEPTED)

    async def get_rejected_orders_with_items(self):
        return await self.get_orders_by_status_with_items(OrderStatus.REJECTED)

    async def get_pending_orders_with_items(self):
        return await self.get_orders_by_status_with_items(OrderStatus.PENDING)

    async def get_in_progress_orders_with_items(self):
        return await self.get_orders_by_status_with_items(OrderStatus.IN_PROGRESS)
