from typing import List,Optional

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse

from src.api.schemas.order_schema import OrderCreate, OrderResponse
from src.dependencies import get_current_user
from src.services.order_service import OrderService

router = APIRouter(default_response_class=ORJSONResponse, tags=["Orders",])
service = OrderService()

order_service = OrderService()


@router.get("/orders/accepted", response_model=List[OrderResponse])
async def get_accepted_orders(user=Depends(get_current_user)):
    return await order_service.get_accepted_orders_dmtt(user.id)


@router.get("/orders/rejected", response_model=List[OrderResponse])
async def get_rejected_orders(user=Depends(get_current_user)):
    return await order_service.get_rejected_orders_dmtt(user.id)


@router.get("/orders/pending", response_model=List[OrderResponse])
async def get_pending_orders(user=Depends(get_current_user)):
    return await order_service.get_pending_orders_dmtt(user.id)


@router.get("/orders/in-progress", response_model=List[OrderResponse])
async def get_in_progress_orders(user=Depends(get_current_user)):
    return await order_service.get_in_progress_orders_dmtt(user.id)


@router.post("/orders/")
async def create_order_with_dmtt(dmtt_data: List[OrderCreate], user=Depends(get_current_user)):
    return await service.create_order_with_items(user.id, dmtt_data)


@router.get("/orders/{order_id}", response_model=Optional[OrderResponse])
async def get_all_dmtt(order_id: int):
    data = await service.get_order_by_id(order_id)
    return data
