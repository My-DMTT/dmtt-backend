from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.infrastructure.models.base import BaseModel


class Contract(BaseModel):
    __tablename__ = "contracts"
    company_id = Column(Integer, ForeignKey('company.id', ondelete='CASCADE'))
    dmtt_id = Column(Integer, ForeignKey('dmtt.id', ondelete='CASCADE'))
    excel_url = Column(String(255), nullable=True)
    active_sheet_name = Column(String(31), nullable=True)

    dmtt = relationship("Dmtt")
    company = relationship("Company")

    def __str__(self):
        return self.excel_url
