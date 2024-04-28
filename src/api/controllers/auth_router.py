from fastapi import APIRouter, Depends

from src.api.schemas.auth_schema import AuthSchema, PhoneAuthSchema
from src.api.schemas.token import TokenSchema
from src.services.auth_service import AuthService

auth_service = AuthService()
router = APIRouter(tags=["auth"])


@router.post('/auth/login/', response_model=TokenSchema)
async def login(data: AuthSchema):
    return await auth_service.login(username=data.username, password=data.password)


@router.post('/auth/otp-code/')
async def login(phone_number: str):
    return await auth_service.check_phone(phone_number=phone_number)


@router.post('/auth/verify-code/')
async def login(phone_number: str, code: str):
    return await auth_service.login_by_phone(phone_number=phone_number, code=code)


@router.post('/auth/check-phone/')
async def check_phone(data: PhoneAuthSchema):
    return await auth_service.check_phone_number(phone_number=data.phone_number, tg_user_id=data.tg_user_id)
