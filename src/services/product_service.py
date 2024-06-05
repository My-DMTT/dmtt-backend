import os

from src.api.schemas.product import ProductCreate
from src.domain.exceptions import image_not_found
from src.infrastructure.repositories.product_repo import ProductRepo
from src.infrastructure.services.excel_service import SheetDataFetcher


class ProductService():

    def __init__(self):
        self.product_repo = ProductRepo()
        self._sheet_data_fetcher = SheetDataFetcher()

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

    async def get_product_prices(self,):
        valid_products = []
        data = await self._sheet_data_fetcher.get_data_frame("https://docs.google.com/spreadsheets/d/1rblVzQahN49HfWqUnFub-riA7kfXT3f-IUyomhi7IrA/edit#gid=0", "Iyun")
        for index, row in data.iterrows():
            if row["Mahsulot nomi"] and row["Narxi"]:
                product = {"name": row['Mahsulot nomi'],
                           "price": int(row['Narxi'].replace(" ", "")), "measure": row["O'lchov birligi"]}
                valid_products.append(product)

        return valid_products

# from src.infrastructure.services.excel_service import
