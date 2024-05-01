from typing import List, Optional

from pydantic import BaseModel


class LimitInfo(BaseModel):
    name: str
    measure: str
    limit: str
    image_url: Optional[str]
    count: str

    class Config:
        from_attributes = True


class Limit(BaseModel):
    dmtt_id: int
    # items: List[LimitItem]
