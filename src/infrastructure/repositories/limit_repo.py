from src.infrastructure.models.limit import ExcelLimit
from src.infrastructure.repositories.base import CRUDRepoBase


class ExcelLimitRepo(CRUDRepoBase):
    model = ExcelLimit
