
from typing import Optional
from typing import List

from fastapi import APIRouter, Depends

from src.api.schemas.dmtt_schema import DmttInfo
from src.api.schemas.user_schema import UserInfo
from src.dependencies import get_current_user
from src.domain.models.user_model import UserCreate
from src.services.dmtt_service import DmttService
from src.services.user_service import UsersService

dmtt_service = DmttService()
service = UsersService()

router = APIRouter(tags=["Users"])


@router.post("/users/")
async def create_manager(data: UserCreate):
    return await service.create_user(data=data)


@router.get("/users", response_model=List[UserInfo])
async def create_manager():
    return await service.get_all_users()


@router.get("/profile", response_model=UserInfo)
async def get_my_profile(user=Depends(get_current_user)):
    return user


@router.get("/users/dmtt", response_model=Optional[DmttInfo])
async def get_my_profile(user=Depends(get_current_user)):
    return await dmtt_service.get_by_user(user)
