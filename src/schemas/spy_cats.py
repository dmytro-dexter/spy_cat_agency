from pydantic import BaseModel
from uuid import UUID


class CreateCat(BaseModel):
    name: str
    years_of_experience: int
    is_available: bool = True
    salary: int


class ShowCat(BaseModel):
    id: UUID
    name: str
    years_of_experience: int
    salary: int
    is_available: bool
    # current_mission: int | None = None


class UpdateCat(BaseModel):
    salary: int
