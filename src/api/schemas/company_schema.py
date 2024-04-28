from typing import Optional

from pydantic import BaseModel, Field, validator


class CompanyBase(BaseModel):
    """
    Base model for common attributes of a company.
    """
    name: str
    address: str
    phone_number: str
    stir: str
    is_active: Optional[bool]


class CompanyCreate(CompanyBase):
    """
    Model for creating a new company.
    Ensures that the 'name' and 'phone_number' fields are required for creation.
    """
    pass



class CompanyUpdate(CompanyBase):
    """
    Model for updating an existing company.
    All attributes are optional as this model will be used for partial updates.
    """
    pass


class CompanyInfo(CompanyBase):

    id: int
    user_id: int

    class Config:
        from_attributes = True
