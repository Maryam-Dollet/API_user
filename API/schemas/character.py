from pydantic import BaseModel
from typing import Optional


class Character(BaseModel):
    name: str
    occupation: str
    age: int | str = "Not specified"
    affiliation: Optional[str] = "Not provided"
