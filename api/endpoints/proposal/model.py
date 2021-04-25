from datetime import datetime
from typing import List

from pydantic import BaseModel


class ProposalCreate(BaseModel):
    proposal_addr: str
    owner_addr: str
    target_price: int
    project_description: str
    start_time: datetime
    project_name: str
    representative: str
    email: str
    phone: str
    img_url: List[str]


class DBProposal(BaseModel):
    proposal_addr: str
    owner_addr: str
    target_price: int
    project_description: str
    start_time: datetime
    project_name: str
    representative: str
    email: str
    phone: str


class ProposalReturn(BaseModel):
    proposal_addr: str
    owner_addr: str
    target_price: int
    project_description: str
    start_time: datetime
    project_name: str
    representative: str
    email: str
    phone: str
    img_url: List[str]


class ProposalItem(BaseModel):
    project_name: str
    representative: str
    img_url: str
    target_price: int
    current_price: int
    left_time: str
