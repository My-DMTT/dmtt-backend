from time import time

from src.domain.exceptions import not_found_exception, user_not_found
from src.domain.models.dmtt_model import DmttCreate, DmttUpdate
from src.infrastructure.repositories.dmtt_repo import DmttRepo
from src.infrastructure.repositories.user_repo import UserRepo


class DmttService():
    def __init__(self):
        self.repository = DmttRepo()
        self._user_repo = UserRepo()

    async def create_dmtt(self, dmtt_data: DmttCreate):
        if await self._user_repo.is_exists(id=dmtt_data.user_id):
            return await self.repository.create(dmtt_data)
        raise not_found_exception("User")

    async def get_all_dmtt(self):
        return await self.repository.get_all()

    async def get_dmtt_by_id(self, dmtt_id: int):
        return await self.repository.get(dmtt_id)

    async def update_dmtt(self, dmtt_id: int, dmtt_data: DmttUpdate):
        return await self.repository.update(dmtt_id, dmtt_data)

    async def delete_dmtt(self, dmtt_id: int):
        return await self.repository.delete(dmtt_id)

    async def get_by_user(self, user):
        return await self.repository.filter_one(user_id=user.id)
