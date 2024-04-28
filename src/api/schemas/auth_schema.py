# Your schemas for the app
from pydantic import BaseModel


class AuthSchema(BaseModel):
    username: str
    password: str


class PhoneAuthSchema(BaseModel):
    phone_number: str
    tg_user_id: str
