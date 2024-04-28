import enum

from sqlalchemy import Column, Enum, String

from src.infrastructure.models.base import BaseModel


class UserRoleEnum(enum.Enum):
    office = "office"
    superuser = "superuser"
    manager = "manager"
    business_man = "business_man"


# user_roles_list = [role.value for role in UserRoleEnum]


class User(BaseModel):
    __tablename__ = "users"
    first_name = Column(String(50), default="user")
    last_name = Column(String(50), default="user")
    username = Column(String(50), default="")
    password = Column(String(255), default="")
    phone_number = Column(String(50), nullable=True)
    district = Column(String(255), default="")
    new_password = Column(String(63), nullable=True)
    tg_user_id = Column(String(16), nullable=True)
    role = Column(Enum(UserRoleEnum), default=UserRoleEnum.manager)

    def __str__(self):
        return self.first_name
