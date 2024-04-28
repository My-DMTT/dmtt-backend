import os

from src.api.schemas.product import ProductCreate
from src.domain.exceptions import image_not_found
from src.infrastructure.repositories.product_repo import ProductRepo


class ProductService():

    def __init__(self):
        self.product_repo = ProductRepo()

    async def create_product(self, product_data: ProductCreate):
        if not os.path.exists(product_data.image_url):
            raise image_not_found
        db_product = await self.product_repo.create(product_data)
        return db_product

    async def get_product_by_id(self, product_id):
        product = await self.product_repo.get(product_id)
        return product

    async def get_all_product(self):
        products = await self.product_repo.get_all()
        return products

    async def update_product(self, product_id, product_data):
        db_product = await self.product_repo.update(product_id, product_data)
        return db_product

    async def delete_product(self, product_id):
        await self.product_repo.delete(id=product_id)
        return {"detail": "success"}
