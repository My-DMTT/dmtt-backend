from fastapi import APIRouter

from src.api.bot_controller import company_router

router = APIRouter(prefix='/bot')


router.include_router(company_router.router)
