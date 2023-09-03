from pydantic import BaseModel, EmailStr
from uuid import UUID


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    user_id: UUID
    email: EmailStr

    class Config:
        from_attributes = True
