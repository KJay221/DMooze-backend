from pydantic import BaseModel


class UserCreate(BaseModel):
    account: str
    password: str
