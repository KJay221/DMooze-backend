from datetime import datetime
from typing import List

from pydantic import BaseModel


class ProposalCreate(BaseModel):
    owner_addr: str = ""
    target_price: float = 0
    project_description: str = ""
    project_name: str = ""
    representative: str = ""
    email: str = ""
    phone: str = ""
    create_hash: str = ""


class DBProposal(BaseModel):
    proposal_id: int
    owner_addr: str
    target_price: float
    project_description: str
    start_time: datetime
    project_name: str
    representative: str
    email: str
    phone: str
    create_hash: str


class ProposalItem(BaseModel):
    proposal_id: int
    owner_addr: str
    target_price: float
    current_price: float
    project_description: str
    start_time: datetime
    left_time: str
    project_name: str
    representative: str
    email: str
    phone: str
    create_hash: str
    img_url: List[str]
    money_input: List[float]
    sponsor_addr: List[str]
    transaction_hash_input: List[str]
    input_time: List[str]
    money_output: List[float]
    use_description: List[str]
    transaction_hash_output: List[str]
    output_time: List[str]
