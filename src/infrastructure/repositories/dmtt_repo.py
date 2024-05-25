from sqlalchemy.orm import joinedload

from src.infrastructure.database.adapters.database import get_db
from src.infrastructure.models.dmtt import Dmtt
from src.infrastructure.repositories.base import CRUDRepoBase


class DmttRepo(CRUDRepoBase):
    model = Dmtt

    async def get_full_info(self, instance_id):
        with get_db() as session:
            return (
                session.query(self.model)
                .options(joinedload(Dmtt.user))
                .filter(Dmtt.id == instance_id)
                .first()
            )
