from typing import Type

from pydantic import BaseModel

from src.infrastructure.database.adapters.database import get_db
from src.infrastructure.models.user import User
from src.infrastructure.repositories.base import CRUDRepoBase
from src.infrastructure.services.token_service import TokenService


class UserRepo(CRUDRepoBase):
    model = User

    async def filter(self, **kwargs):
        with get_db as session:
            return session.query(self.model).filter_by(**kwargs).first()

    async def create(self, obj_in: Type[BaseModel]) -> BaseModel:
        with get_db() as session:
            new_obj = self.model(**obj_in.model_dump())
            session.add(new_obj)
            if obj_in.password:
                new_obj.password = _service.get_hashed_password(
                    obj_in.password)
            session.commit()
            session.refresh(new_obj)
            return new_obj


class SuperUserRepo(CRUDRepoBase):
    model = User


_service = TokenService()


class ManagerRepo(CRUDRepoBase):
    model = User
