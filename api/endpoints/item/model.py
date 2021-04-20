from datetime import datetime

from pydantic import BaseModel


class ItemCreate(BaseModel):
    target_price: int
    project_content: str
    start_time: datetime
    end_time: datetime
    project_name: str
    representative: str
    email: str
    phone: str
