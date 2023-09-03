from database_utils import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Column, String, Integer


class Character(Base):
    __tablename__ = "characters"
    character_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid1)
    name = Column(String, nullable=False)
    occupation = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    affiliation = Column(String, nullable=True, default="Not Provided")
