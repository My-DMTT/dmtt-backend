from typing import List, Optional

from pydantic import BaseModel

from src.api.schemas.dmtt_schema import DmttInfo


class OrderItemInfo(BaseModel):
    product_name: str
    count: float

    class Config:
        from_attributes = True


class OrderCreateInfo(BaseModel):
    company_id: int


class ListOrderCreate(BaseModel):
    data: List[OrderCreateInfo]


class OrderResponse(BaseModel):
    id: int
    dmtt: Optional[DmttInfo]
    order_status: str

    items: List[OrderItemInfo]

    class Config:
        from_attributes = True


class BotOrderResponse(BaseModel):
    id: int
    # dmtt: Optional[DmttInfo]
    order_status: str

    items: List[OrderItemInfo]

    class Config:
        from_attributes = True


class OrderCreate(BaseModel):
    company_id: int
    product_name: str
    count: float
