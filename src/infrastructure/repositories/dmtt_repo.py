from src.infrastructure.models.dmtt import Dmtt
from src.infrastructure.repositories.base import CRUDRepoBase


class DmttRepo(CRUDRepoBase):
    model = Dmtt
