from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    user_id: UUID
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True
