from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class UserInDBBase(User):
    id: Optional[int] = None

    class Config:
        orm_mode = True