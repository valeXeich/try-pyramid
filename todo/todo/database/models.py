from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column

from todo.database.session import Base
from todo.database.enums import Status


intpk = Annotated[int, mapped_column(primary_key=True)]



class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[intpk]
    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[Status]