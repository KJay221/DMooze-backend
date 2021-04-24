from pydantic import BaseModel


class MoneyRecord(BaseModel):
    money: int
    proposal_addr: str
