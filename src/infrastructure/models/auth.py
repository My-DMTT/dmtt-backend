import uuid

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.infrastructure.models.base import BaseModel


class SecurityJti(BaseModel):
    __tablename__ = "securityjtis"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    jti = Column(String(63))


class OtpCodes(BaseModel):
    __tablename__ = "otp_codes"
    phone_number = Column(String(50))
    code = Column(String(10))
