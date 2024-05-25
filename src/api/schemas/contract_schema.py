from pydantic import BaseModel


class ContractShcema(BaseModel):
    company_id: int
    dmtt_id: int
    excel_url: int
    active_sheet_name: int

    class Config:
        from_attributes = True
