from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.responses import ORJSONResponse

from src.api.schemas.dmtt_schema import DmttCreate, DmttInfo, DmttUpdate
from src.services.dmtt_service import DmttService

router = APIRouter(default_response_class=ORJSONResponse, tags=["dmtts",])
service = DmttService()


@router.post("/dmtts/", response_model=DmttInfo)
async def create_dmtt(dmtt_data: DmttCreate):
    return await service.create_dmtt(dmtt_data)


@router.get("/dmtts/", response_model=List[DmttInfo])
async def get_all_dmtt():
    return await service.get_all_dmtt()


@router.get("/dmtts/{dmtt_id}/", response_model=DmttInfo)
async def read_dmtt(dmtt_id: int):
    dmtt = await service.get_dmtt_by_id(dmtt_id)
    if not dmtt:
        raise HTTPException(status_code=404, detail="Dmtt not found")
    return dmtt


@router.put("/dmtts/{dmtt_id}/", response_model=DmttInfo)
async def update_dmtt(dmtt_id: int, dmtt_data: DmttUpdate):
    updated_dmtt = await service.update_dmtt(dmtt_id, dmtt_data)
    if not updated_dmtt:
        raise HTTPException(status_code=404, detail="Dmtt not found")
    return updated_dmtt


@router.delete("/dmtts/{dmtt_id}/")
async def delete_dmtt(dmtt_id: int):
    result = await service.delete_dmtt(dmtt_id)
    if not result:
        raise HTTPException(status_code=404, detail="Dmtt not found")
    return result
