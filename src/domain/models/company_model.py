from pydantic import BaseModel, Field


class CompanyBase(BaseModel):
    """
    Base model for common attributes of a company.
    """
    name: str = Field(..., max_length=255)
    phone_number: str = Field(..., max_length=15)
    stir: str = Field(default=None, max_length=10)
    tg_user_id: str = Field(default=None, max_length=10)
    is_active: bool = Field(default=True)


class CompanyCreate(CompanyBase):
    """
    Model for creating a new company.
    Ensures that the 'name' and 'phone_number' fields are required for creation.
    """
    name: str = Field(..., max_length=255)
    phone_number: str = Field(..., max_length=15)


class CompanyUpdate(CompanyBase):
    """
    Model for updating an existing company.
    All attributes are optional as this model will be used for partial updates.
    """
    name: str = Field(default=None, max_length=255)
    phone_number: str = Field(default=None, max_length=15)
    stir: str = Field(default=None, max_length=10)
    tg_user_id: str = Field(default=None, max_length=10)
    is_active: bool = Field(default=None)


class CompanyInfo(CompanyBase):

    id: int

    class Config:
        from_attributes = True
