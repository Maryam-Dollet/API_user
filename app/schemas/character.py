from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID
from app.schemas.user import UserOut


class CharacterBase(BaseModel):
    name: str
    occupation: str
    age: Optional[int] = None


class CharacterCreate(CharacterBase):
    pass


class CharacterResponse(CharacterBase):
    # character_id: UUID
    # created_at: datetime
    user_id: UUID
    user: UserOut

    class Config:
        from_attributes = True


class CharacterOut(BaseModel):
    Character: CharacterResponse
    votes: int
