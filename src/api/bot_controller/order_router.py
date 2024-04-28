from typing import List

from fastapi import APIRouter, Depends

from src.api.schemas.order_schema import ListOrderCreate, OrderResponse
from src.dependencies import get_user_by_tg_id
from src.infrastructure.models.order import OrderStatus
from src.services.order_service import OrderService
from src.services.user_service import \
    UsersService  # Если у вас есть такой сервис

router = APIRouter(tags=["Order"])
order_service = OrderService()
user_service = UsersService()  # Инициализация сервиса пользователей


@router.get("/orders/accepted/", response_model=List[OrderResponse])
async def get_accepted_orders(user=Depends(get_user_by_tg_id)):
    return await order_service.get_accepted_orders_with_items(user.id)


@router.post("/orders/accepted/")
async def post_accepted_orders(order_id: int, user=Depends(get_user_by_tg_id)):
    return await order_service.change_order_status(order_id, OrderStatus.ACCEPTED)


@router.post("/orders/rejected/")
async def post_accepted_orders(order_id: int, user=Depends(get_user_by_tg_id)):
    return await order_service.change_order_status(order_id, OrderStatus.REJECTED)


@router.post("/orders/in-progress/")
async def post_accepted_orders(order_id: int, user=Depends(get_user_by_tg_id)):
    return await order_service.change_order_status(order_id, OrderStatus.IN_PROGRESS)


@router.get("/orders/rejected/", response_model=List[OrderResponse])
async def get_rejected_orders(user=Depends(get_user_by_tg_id)):
    return await order_service.get_rejected_orders_with_items(user.id)


@router.get("/orders/pending/", response_model=List[OrderResponse])
async def get_pending_orders(user=Depends(get_user_by_tg_id)):
    return await order_service.get_pending_orders_with_items(user.id)


@router.get("/orders/in-progress/", response_model=List[OrderResponse])
async def get_in_progress_orders(user=Depends(get_user_by_tg_id)):
    return await order_service.get_in_progress_orders_with_items(user.id)
