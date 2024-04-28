import uuid

from src.domain.exceptions import not_permission_error_login, user_not_found
from src.domain.models.jti_model import OtpCodeSchema, SecuirtyJtiSchema
from src.infrastructure.repositories.jwt_token_repo import (JWTTokenRepo,
                                                            OtpCodesRepo)
from src.infrastructure.repositories.user_repo import ManagerRepo, UserRepo
from src.infrastructure.services.sms_service import send_sms
from src.infrastructure.services.token_service import TokenService


class AuthService():

    def __init__(self) -> None:
        self._jti_repo = JWTTokenRepo()
        self._user_repo = UserRepo()
        self._token_service = TokenService()
        self._manager_repo = ManagerRepo()
        self._otp_code_repo = OtpCodesRepo()

    async def _authenticate(self, username="", password=""):
        user = await self._user_repo.filter_one(username=username)
        if user:
            if self._token_service.verify_password(password=password, hashed_pass=user.password):
                return user
        raise user_not_found

    async def check_phone(self, phone_number: str):
        phone_number = self._validate_phone(phone_number=phone_number)

        p = await self._manager_repo.is_exists(phone_number=phone_number)
        if not p:
            raise not_permission_error_login
        code = self._token_service.generate_verification_code()
        await self._otp_code_repo.create(
            OtpCodeSchema(phone_number=phone_number, code=code)
        )
        send_sms(phone_number=phone_number, data=code)
        return {
            "detail": "Code sent sucessfully"
        }

    def _validate_phone(self, phone_number: str):
        if "+" in phone_number:
            phone_number = phone_number[1:]
        return phone_number

    async def login(self, username, password):
        user = None
        try:
            user = await self._authenticate(username, password)
        except Exception as e:
            raise user_not_found
        if user:
            seans = await self._jti_repo.create(SecuirtyJtiSchema(user_id=user.id, jti=str(uuid.uuid4())))
            token = self._token_service.create_access_token(
                user_id=user.id, jti=seans.jti)
            return {
                "id": user.id,
                "username": user.username,
                "access_token": token
            }

        raise user_not_found

    async def _authenticate_otp(self, phone_number, code):
        otp_code_object = await self._otp_code_repo.filter_one(phone_number=phone_number, code=code)
        if otp_code_object:
            user = await self._user_repo.filter_one(phone_number=phone_number)
            if user:
                return user
        raise user_not_found

    async def login_by_phone(self, phone_number="", code=""):
        user = None
        try:
            phone_number = self._validate_phone(phone_number=phone_number)
            user = await self._authenticate_otp(phone_number, code)
        except Exception as e:
            raise user_not_found
        if user:
            seans = await self._jti_repo.create(SecuirtyJtiSchema(user_id=user.id, jti=str(uuid.uuid4())))
            token = self._token_service.create_access_token(
                user_id=user.id, jti=seans.jti)
            return {
                "id": user.id,
                "username": user.username,
                "access_token": token
            }

        raise user_not_found

    async def check_phone_number(self, phone_number, tg_user_id):
        user = await self._user_repo.filter_one(phone_number=phone_number)
        if user:
            await self._user_repo.update(user.id, {"tg_user_id": tg_user_id})
            return user
        else:
            raise user_not_found
