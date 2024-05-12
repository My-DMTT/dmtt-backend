from pydantic import BaseModel


class ProductPrices(BaseModel):
    name: str
    price: int
    measure: str


class ProductCreate(BaseModel):
    name: str
    measure: str
    code: str
    image_url: str


class ProductUpdate(ProductCreate):
    pass


class ProductInfo(ProductCreate):
    id: int

    class ConfigDict:
        from_attributes = True
