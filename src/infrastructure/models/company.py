from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.infrastructure.models.base import BaseModel


class Company(BaseModel):
    __tablename__ = 'company'

    user_id = Column(ForeignKey("users.id", ondelete="Cascade"))
    name = Column(String(255))
    address = Column(String(255))
    phone_number = Column(String(15))
    stir = Column(String(10), nullable=True)
    is_active = Column(Boolean(), default=True)

    user = relationship("User")

    def __repr__(self):
        return self.name
