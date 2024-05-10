from sqlalchemy.orm import contains_eager, joinedload

from src.api.schemas.order_schema import FullOrderDetailResponse
from src.infrastructure.database.adapters.database import get_db
from src.infrastructure.models.company import Company
from src.infrastructure.models.dmtt import Dmtt
from src.infrastructure.models.order import Order, OrderItems
from src.infrastructure.repositories.base import CRUDRepoBase


class OrderRepo(CRUDRepoBase):
    model = Order

    async def get_orders_by_status_with_items(self, user_id, status):
        with get_db() as session:
            return (
                session.query(Order)
                .filter(Order.order_status == status)
                .options(joinedload(Order.dmtt), joinedload(Order.items))
                .join(Company, Company.id == Order.company_id)
                .options(contains_eager(Order.company))
                .filter(Company.user_id == user_id)
                .all()
            )

    async def change_status(self, id, status):
        with get_db() as session:
            with get_db() as session:
                session.query(Order).filter_by(id=id).update({
                    "order_status": status
                })
                session.commit()

    async def get_orders_by_status_dmtt(self, user_id, status):
        with get_db() as session:
            return (
                session.query(Order)
                .filter(Order.order_status == status)
                .options(joinedload(Order.items), joinedload(Order.company))
                .join(Dmtt, Dmtt.id == Order.dmtt_id)
                .options(contains_eager(Order.dmtt))
                .filter(Dmtt.user_id == user_id)
                .all()
            )

    async def get_order_with_items(self, order_id):
        with get_db() as session:
            data = (
                session.query(Order)
                .options(joinedload(Order.items), joinedload(Order.dmtt), joinedload(Order.company))
                .filter(Order.id == order_id)
                .first()
            )
            return FullOrderDetailResponse.model_validate(data)

    async def create_order_with_items(self, dmtt_id, company_id, deadline, obj_in) -> Order:
        with get_db() as session:
            new_order = Order(company_id=company_id,
                              dmtt_id=dmtt_id, deadline=deadline)
            session.add(new_order)
            session.flush()

            for item_data in obj_in:
                order_item = OrderItems(
                    order_id=new_order.id,
                    product_name=item_data.get("product_name"),
                    count=item_data.get("count"),
                )
                session.add(order_item)

            session.commit()
            session.refresh(new_order)
            return new_order


class OrderItemsRepo(CRUDRepoBase):
    model = OrderItems
