
from typing import Dict

from fastapi import APIRouter, Depends

from src.dependencies import get_current_manager
from src.services.limit_service import LimitService

router = APIRouter()
limit_service = LimitService()

limitlar: Dict[str, Dict] = {}


@router.get("/limit")
async def get_limit_dmtt(company_id: int, manager=Depends(get_current_manager)):
    if company_id in limitlar:
        return limitlar.get(company_id)
    data = await limit_service.get_limit_by_dmtt(
        manager=manager, company_id=company_id
    )
    limitlar[company_id] = data
    return data
