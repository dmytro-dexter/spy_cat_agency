from pydantic import BaseModel


class CreateTarget(BaseModel):
    name: str
    country: str
    is_complete: bool = False
    notes: str
    mission_id: int


class UpdateTarget(BaseModel):
    notes: str
