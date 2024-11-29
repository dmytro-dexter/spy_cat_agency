from sqlalchemy import Column, Integer, Text, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.db.base_class import Base
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


class Mission(Base):
    __tablename__ = "missions"

    id = Column(UUID(as_uuid=True), unique=True, primary_key=True, default=uuid4)
    info = Column(Text, nullable=False)
    # assignee_id = Column(Integer, ForeignKey("agents_cats.id"))
    # assignee = relationship("SpyCatAgency", back_populates="mission")
    # targets = relationship("Target", back_populates="mission_reference")
