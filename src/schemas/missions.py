from pydantic import BaseModel, Field
from typing import List
from uuid import UUID
from src.schemas.mission_target import TargetBase


class CreateMission(BaseModel):
    number_of_targets: Field(..., qe=1, le=3)
    target: List[TargetBase] | None = []
    is_complete: bool
    assignee: UUID
    info: str


class MissionBase(BaseModel):
    id: UUID
    target: List[TargetBase] | None = []
    is_complete: bool
    assignee: UUID
    info: str


class MissionUpdate(BaseModel):
    id: UUID
    info: str
    is_complete: bool
    assignee: bool
