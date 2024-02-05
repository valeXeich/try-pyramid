from typing import Literal

from pydantic import BaseModel, field_validator


class TaskDTO(BaseModel):
    id: int
    title: str
    description: str
    status: Literal["doing", "done", "planned"]

    @field_validator('status', mode='before')
    @classmethod
    def get_value_status(cls, status: str) -> str:
        return status.value