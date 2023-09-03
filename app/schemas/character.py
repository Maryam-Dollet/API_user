from pydantic import BaseModel
from typing import Optional


class CharacterBase(BaseModel):
    name: str
    occupation: str
    age: int = None


class CharacterCreate(CharacterBase):
    pass
