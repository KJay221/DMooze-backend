from pydantic import BaseModel


class MoneyRecord(BaseModel):
    money: int
    proposal_id: int


class RecordReturn(BaseModel):
    current_price: int
    target_price: int
