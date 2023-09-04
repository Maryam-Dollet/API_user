from pydantic import BaseModel
from pydantic.types import conint
from uuid import UUID


class Vote(BaseModel):
    character_id: UUID
    dir: conint(gt=-1, le=1)
