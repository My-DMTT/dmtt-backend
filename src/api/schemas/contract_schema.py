from pydantic import BaseModel


class ContractShcema(BaseModel):
    id: int
    company_id: int
    dmtt_id: int
    excel_url: str
    active_sheet_name: str

    class Config:
        from_attributes = True
