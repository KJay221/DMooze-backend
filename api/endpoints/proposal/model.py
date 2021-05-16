from datetime import datetime
from typing import List

from pydantic import BaseModel


class ProposalCreate(BaseModel):
    owner_addr: str = ""
    target_price: int = 0
    project_description: str = ""
    project_name: str = ""
    representative: str = ""
    email: str = ""
    phone: str = ""


class DBProposal(BaseModel):
    proposal_id: int
    owner_addr: str
    target_price: int
    project_description: str
    start_time: datetime
    project_name: str
    representative: str
    email: str
    phone: str


class ProposalItem(BaseModel):
    proposal_id: int
    owner_addr: str
    target_price: int
    current_price: int
    project_description: str
    start_time: datetime
    left_time: str
    project_name: str
    representative: str
    email: str
    phone: str
    img_url: List[str]
    money: List[int]
    sponsor_addr: List[str]
    transaction_hash: List[str]
