from fastapi import APIRouter

from src.api.bot_controller import company_router, order_router, product_router

router = APIRouter(prefix='/bot')


router.include_router(company_router.router)
router.include_router(order_router.router)
router.include_router(product_router.router)
