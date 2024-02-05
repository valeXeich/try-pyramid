from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from todo.settings import settings


engine = create_engine(
    url=settings.DB_URL,
)

session_factory = sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass