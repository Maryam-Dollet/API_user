from database_utils import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer, text


class Character(Base):
    __tablename__ = "characters"
    character_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v1()")
    )
    name = Column(String, nullable=False)
    occupation = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    affiliation = Column(String, nullable=True, server_default="Not Provided")