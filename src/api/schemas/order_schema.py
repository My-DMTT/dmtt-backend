from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from src.api.schemas.company_schema import CompanyInfo
from src.api.schemas.dmtt_schema import DmttInfo
from src.api.schemas.user_schema import UserInfo


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
    company: Optional[CompanyInfo]
    order_status: str
    sequence_number: Optional[int]
    datetime: Optional[datetime]
    items: List[OrderItemInfo]

    class Config:
        from_attributes = True


class FullDmttInfo(DmttInfo):
    user: Optional[UserInfo]


class FullOrderDetailResponse(OrderResponse):
    dmtt: Optional[FullDmttInfo]


class BotOrderResponse(BaseModel):
    id: int
    # dmtt: Optional[DmttInfo]
    sequence_number: Optional[int]
    order_status: str
    datetime: Optional[datetime]
    items: List[OrderItemInfo]

    class Config:
        from_attributes = True


class OrderCreate(BaseModel):
    company_id: int
    product_name: str
    count: float
