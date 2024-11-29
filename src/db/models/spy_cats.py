from sqlalchemy import Column, Integer, Text, String, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from src.db.session import Base
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


class SpyCatAgency(Base):
    __tablename__ = "agents_cats"

    id = Column(UUID(as_uuid=True), unique=True, primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    years_of_experience = Column(Integer, nullable=False)
    # breed = relationship("Breed", back_populates="cat")
    salary = Column(Integer, nullable=False)
    mission = relationship("Mission", back_populates="assignee")
    is_available = Column(Boolean)
