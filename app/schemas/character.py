from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class CharacterBase(BaseModel):
    name: str
    occupation: str
    age: Optional[int] = None


class CharacterCreate(CharacterBase):
    pass


class CharacterResponse(CharacterBase):
    character_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
