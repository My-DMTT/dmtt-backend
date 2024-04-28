from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse

from src.api.schemas.company_schema import CompanyInfo
from src.api.schemas.dmtt_schema import DmttCreate, DmttInfo, DmttUpdate
from src.dependencies import get_current_user
from src.services.contract_service import ContractService

router = APIRouter(default_response_class=ORJSONResponse,
                   tags=["contract",])
service = ContractService()


@router.get("/contracts/companies", response_model=List[CompanyInfo])
async def create_dmtt(user=Depends(get_current_user)):
    return await service.get_all_companies(user.id)
