
from src.domain.models.product_model import ProductCreate
from src.infrastructure.database.adapters.database import get_db
from src.infrastructure.models.product import Product
from src.infrastructure.repositories.base import CRUDRepoBase


class ProductRepo(CRUDRepoBase):
    model = Product

    async def get_or_create(product_name, measure):
        with get_db() as session:
            instance = session.query(Product).filter_by(
                name=product_name).first()
            if instance:
                return instance
            instance = Product(name=product_name, measure=measure)
            session.add(instance)
            session.commit()
            session.refresh(instance)
            return instance
