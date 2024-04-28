from typing import List

from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from src.api.schemas.company_schema import (CompanyCreate, CompanyInfo,
                                            CompanyUpdate)
from src.services.company_service import CompanyService

service = CompanyService()

router = APIRouter(tags=["Firma"])


@router.get("/companies", response_model=List[CompanyInfo], response_class=ORJSONResponse)
async def get_all_company():
    return await service.get_all_companies()


@router.get("/companies/{id}", response_model=CompanyInfo)
async def get_company(id: int):
    return await service.get_company_by_id(id=id)


@router.post("/companies/", response_model=CompanyInfo)
async def create(data: CompanyCreate):
    return await service.create_company(data=data)


@router.put("/companies/{id}/", response_model=CompanyInfo)
async def update_company(id: int, data: CompanyUpdate):
    return await service.update_company(id=id, data=data)


@router.delete("/{id}")
async def delete_company(id: int):
    return await service.delete_company(id=id)
