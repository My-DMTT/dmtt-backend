from typing import List, Optional

from fastapi import APIRouter, Depends

from src.api.schemas.company_schema import (CompanyCreate, CompanyInfo,
                                            CompanyUpdate)
from src.dependencies import get_user_by_tg_id
from src.services.company_service import CompanyService

service = CompanyService()


router = APIRouter(tags=["Bot_Firma"])


@router.get("/companies", response_model=List[CompanyInfo])
async def get_all_company(user=Depends(get_user_by_tg_id)):
    # user = await user_service.get_user_tg_id(tg_user_id)
    data = await service.get_all_companies(user_id=user.id)
    return data


@router.get("/companies/{id}", response_model=Optional[CompanyInfo])
async def get_company(user=Depends(get_user_by_tg_id)):
    return await service.get_company_by_id(id=id, user_id=user.id)


@router.post("/companies/", response_model=CompanyInfo)
async def create(data: CompanyCreate, user=Depends(get_user_by_tg_id)):
    return await service.create_company(user_id=user.id, data=data)


@router.put("/companies/{id}/", response_model=CompanyInfo)
async def update_company(id: int, data: CompanyUpdate, user=Depends(get_user_by_tg_id)):
    return await service.update_company(id=id, user_id=user.id, data=data)


@router.delete("/{id}")
async def delete_company(id: int, user=Depends(get_user_by_tg_id)):
    return await service.delete_company(id=id, user_id=user.id)
