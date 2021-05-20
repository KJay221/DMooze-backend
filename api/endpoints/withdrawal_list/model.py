from pydantic import BaseModel


class WithdrawalRecord(BaseModel):
    money: float
    proposal_id: str
    use_description: str
    transaction_hash: str
