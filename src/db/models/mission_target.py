from sqlalchemy import Column, Integer, Text, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4
from src.db.base_class import Base


class Target(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    is_complete = Column(Boolean)
    # mission_id = Column(Integer, ForeignKey("mission.id"))
    # mission_reference = relationship("Mission", back_populates="target")
    notes = Column(Text)
