from typing import Literal

from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str
    status: Literal["doing", "done", "planned"]