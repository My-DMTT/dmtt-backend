from sqlalchemy.orm import joinedload

from src.infrastructure.database.adapters.database import get_db
from src.infrastructure.models.order import Order, OrderItems
from src.infrastructure.repositories.base import CRUDRepoBase


class OrderRepo(CRUDRepoBase):
    model = Order

    async def get_orders_by_status_with_items(self, status):
        with get_db() as session:
            return session.query(Order).filter(Order.order_status == status).join(OrderItems).all()

    async def get_all_orders_with_items(self):
        with get_db() as session:
            return session.query(Order).join(OrderItems).all()

    async def create_order_with_items(self, obj_in) -> Order:
        with get_db() as session:
            new_order = Order(user_id=obj_in.user_id, dmtt_id=obj_in.dmtt_id)
            session.add(new_order)
            session.flush()

            for item_data in obj_in.items:
                order_item = OrderItems(
                    order_id=new_order.id, product_id=item_data.product_id, count=item_data.count)
                session.add(order_item)

            session.commit()
            session.refresh(new_order)
            return new_order


class OrderItemsRepo(CRUDRepoBase):
    model = OrderItems
