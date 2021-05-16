from pydantic import BaseModel


class WithdrawalRecord(BaseModel):
    money: int
    proposal_id: int
    use_description: str
    transaction_hash: str
