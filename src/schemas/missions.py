from pydantic import BaseModel
from typing import List


class CreateMission(BaseModel):
    cat: int
    target: List[int]
    is_complete: bool
    assignee: int
    info: str
