from pydantic import BaseModel
from typing import Optional


class CharacterBase(BaseModel):
    name: str
    occupation: str
    age: Optional[int] = None


class CharacterCreate(CharacterBase):
    pass


class CharacterResponse(CharacterBase):
    class Config:
        from_attributes = True
