from database_utils import Base
from sqlalchemy import Column, String, Integer, text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP


class Character(Base):
    __tablename__ = "characters"
    character_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v1()")
    )
    name = Column(String, nullable=False)
    occupation = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    affiliation = Column(String, nullable=True, server_default="Not Provided")
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False,
    )

    user = relationship("User")


class User(Base):
    __tablename__ = "users"
    user_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v1()")
    )
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


class Vote(Base):
    __tablename__ = "votes"
    character_id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), primary_key=True)
