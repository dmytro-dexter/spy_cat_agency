from sqlalchemy import Column, Integer, Text, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4
from src.db.base_class import Base


class Mission(Base):
    id = Column(Integer, primary_key=True, index=True)
    info = Column(Text, nullable=False)
    assignee_id = Column(Integer, ForeignKey("agents_cats.id"))
    assignee = relationship("SpyCat", back_populates="mission")
    target = relationship("Target", back_populates="mission_reference")
