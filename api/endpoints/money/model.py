from pydantic import BaseModel


class MoneyRecord(BaseModel):
    money: int
    proposal_id: int
    sponsor_addr: str
    transaction_hash: str
