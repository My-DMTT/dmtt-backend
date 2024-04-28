from typing import List

from pydantic import BaseModel


class LimitInfo(BaseModel):
    name: str
    measure: str
    limit: str
    count: str

    class Config:
        from_attributes = True


class Limit(BaseModel):
    dmtt_id: int
    # items: List[LimitItem]
