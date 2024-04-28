from enum import Enum
from typing import Optional

from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field


class UserRoleEnum(str, Enum):
    office = "office"
    superuser = "superuser"
    manager = "manager"


class UserBase(PydanticBaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    phone_number: Optional[str] = Field(..., max_length=15)
    username: Optional[str] = Field(..., max_length=50)
    password: Optional[str] = Field(..., max_length=255)
    district: Optional[str] = Field(..., max_length=255)


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    role: UserRoleEnum

    class Config:
        from_attributes = True
