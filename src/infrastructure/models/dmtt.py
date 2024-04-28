from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.infrastructure.models.base import BaseModel


class Dmtt(BaseModel):
    __tablename__ = 'dmtt'

    name = Column(String(255))
    address = Column(String(127), nullable=True)
    stir = Column(String(10), nullable=True)
    child_count = Column(Integer, default=0)
    is_active = Column(Boolean(), default=True)
    user_id = Column(ForeignKey("users.id", ondelete="SET NULL"))

    user = relationship("User")

    def __repr__(self):
        return f"{self.name}"
