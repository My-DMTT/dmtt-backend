
from typing import Dict, List

from fastapi import APIRouter, Depends

from src.api.schemas.limit_schema import LimitFactura
from src.dependencies import get_current_manager, get_user_by_tg_id
from src.services.limit_service import LimitService

router = APIRouter()
limit_service = LimitService()

# limitlar: Dict[str, Dict] = {}


@router.get("/limit")
async def get_limit_dmtt(company_id: int, manager=Depends(get_current_manager)):
    data = await limit_service.get_limit_by_dmtt(
        manager=manager, company_id=company_id
    )
    return data


@router.get("/limit-factura", response_model=List[LimitFactura])
async def get_limit_dmtt(user=Depends(get_user_by_tg_id)):
    data = await limit_service.get_limit_faktura(
        user_id=user.id
    )
    return data
