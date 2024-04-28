from pydantic import BaseModel, Field


class DmttBase(BaseModel):
    name: str = Field(..., max_length=255)
    user_id: int
    address: str = Field(None, max_length=127)
    stir: str = Field(None, max_length=10)
    child_count: int = 0
    is_active: bool = True


class DmttCreate(DmttBase):
    pass


class DmttUpdate(DmttBase):
    pass
