from sqlalchemy import Column, Integer, Text, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.db.base_class import Base
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


class Target(Base):
    __tablename__ = "targets"

    id = Column(UUID(as_uuid=True), unique=True, primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    is_complete = Column(Boolean)
    # mission_id = Column(Integer, ForeignKey("mission.id"))
    # mission_reference = relationship("Mission", back_populates="target")
    description = Column(Text)
    notes = Column(Text)
