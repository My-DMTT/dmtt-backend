from src.domain.exceptions import user_not_found
from src.domain.models.user_model import UserCreate
from src.infrastructure.repositories.user_repo import UserRepo


class UsersService():
    def __init__(self):
        self._repo = UserRepo()

    async def create_user(self, data: UserCreate):
        return await self._repo.create(data)

    async def get_all_users(self):
        return await self._repo.get_all()

    async def get_user_tg_id(self, tg_user_id):
        user = await self._repo.filter_one(tg_user_id=tg_user_id)
        if user:
            return user
        raise user_not_found
