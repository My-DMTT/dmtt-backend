from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.responses import ORJSONResponse

from src.api.schemas.order_schema import ListOrderCreate
from src.services.order_service import OrderService

router = APIRouter(default_response_class=ORJSONResponse, tags=["Orders",])
service = OrderService()


@router.post("/orders/")
async def create_dmtt(dmtt_data: ListOrderCreate):
    return await service.create_order_with_items(dmtt_data)


@router.get("/orders")
async def get_all_dmtt():
    return await service.get_all_dmtt()
