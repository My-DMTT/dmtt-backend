from typing import List, Optional

from pydantic import BaseModel

from src.api.schemas.company_schema import CompanyInfo
from src.api.schemas.user_schema import UserInfo


class LimitInfo(BaseModel):
    name: str
    measure: str
    limit: str
    image_url: Optional[str]
    count: str

    class Config:
        from_attributes = True


# ----------------------------------------------------------------

class ShortLimitInfo(BaseModel):
    name: str
    measure: str
    limit: str
    count: str

    class Config:
        from_attributes = True


class FullDmttInfo(BaseModel):
    name: str
    user_id: int
    user: UserInfo
    address: str
    stir: str
    child_count: int
    is_active: bool

    class Config:
        from_attributes = True


class LimitFactura(BaseModel):
    company: CompanyInfo
    dmtt: FullDmttInfo
    items: List[ShortLimitInfo]
