from datetime import datetime

from pydantic import BaseModel


class ProposalCreate(BaseModel):
    owner_addr: str
    target_price: int
    project_description: str
    start_time: datetime
    end_time: datetime
    project_name: str
    representative: str
    email: str
    phone: str
