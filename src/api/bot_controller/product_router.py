from typing import List

from fastapi import APIRouter, Depends

from src.api.schemas.product import ProductPrices
from src.dependencies import get_user_by_tg_id
from src.services.product_service import ProductService

service = ProductService()

router = APIRouter(tags=["Bot-Product"])
# Инициализация сервиса пользователей


@router.get("/products-prices", response_model=List[ProductPrices])
async def get_accepted_orders(user=Depends(get_user_by_tg_id)):
    return await service.get_product_prices()
