import enum

from sqlalchemy import (Column, DateTime, Enum, Float, ForeignKey, Integer,
                        String, func)
from sqlalchemy.orm import relationship

from src.infrastructure.models.base import BaseModel


class OrderStatus(enum.Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'in progress'
    REJECTED = 'rejected'
    ACCEPTED = 'accepted'


class Order(BaseModel):
    __tablename__ = 'orders'

    company_id = Column(Integer, ForeignKey(
        "company.id", ondelete="Cascade"), nullable=False)
    dmtt_id = Column(Integer, ForeignKey(
        "dmtt.id", ondelete="Cascade"), nullable=False)

    datetime = Column(DateTime, server_default=func.now())
    order_status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)

    company = relationship("Company")
    dmtt = relationship("Dmtt")
    items = relationship("OrderItems", back_populates="order")

    def __str__(self):
        return f"{self.dmtt} - {self.id}"


class OrderItems(BaseModel):
    __tablename__ = "order_items"
    order_id = Column(ForeignKey("orders.id", ondelete="Cascade"))
    product_name = Column(String(127), nullable=False)
    count = Column(Float, nullable=False)

    order = relationship("Order", back_populates="items")

    def __str__(self) -> str:
        return f"{self.product_name} {self.count}"
