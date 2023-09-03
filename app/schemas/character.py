from pydantic import BaseModel
from typing import Optional


class Character(BaseModel):
    name: str
    occupation: str
    age: int = None


class CreateCharacter(BaseModel):
    name: str
    occupation: str
    age: int = None


class UpdateCharacter(BaseModel):
    name: str
    occupation: str
    age: int
