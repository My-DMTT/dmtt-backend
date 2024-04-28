from typing import List

from pydantic import BaseModel


class OrderItemCreate(BaseModel):
    product_id: int
    count: int


class OrderCreate(BaseModel):
    company_id: int
    items: List[OrderItemCreate]


class ListOrderCreate(BaseModel):
    data: List[OrderCreate]
