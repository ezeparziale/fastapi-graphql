from datetime import datetime

import strawberry
from pydantic import BaseModel, EmailStr


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


@strawberry.type
class UserQ:
    id: int
    email: str
    created_at: datetime


@strawberry.experimental.pydantic.interface(model=UserCreate, all_fields=True)
class UserCreateQ:
    ...
