import uuid 
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID


from database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)