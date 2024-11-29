from pydantic import BaseModel
from uuid import UUID


class CreateTarget(BaseModel):
    name: str
    country: str
    is_complete: bool = False
    notes: str
    mission_id: int
    description: str


class TargetBase(BaseModel):
    id: UUID
    name: str
    country: str
    is_complete: bool = False
    notes: str
    mission_id: int
    description: str


class UpdateTarget(BaseModel):
    id: UUID
    notes: str
    is_complete: bool
