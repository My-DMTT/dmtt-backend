from pydantic import BaseModel


class SecuirtyJtiSchema(BaseModel):
    user_id: int
    jti: str


class OtpCodeSchema(BaseModel):
    code: str
    phone_number: str
