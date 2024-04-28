
from src.domain.models.product_model import ProductCreate
from src.infrastructure.models.product import Product
from src.infrastructure.repositories.base import CRUDRepoBase


class ProductRepo(CRUDRepoBase):
    model = Product
