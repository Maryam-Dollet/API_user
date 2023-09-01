from pydantic import BaseModel


class Character(BaseModel):
    name: str
    occupation: str
