from pydantic import BaseModel


class UserBase(BaseModel):
    account: str
    password: str
