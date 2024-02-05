from typing import Protocol

from todo.repositories.tasks import TaskRepository


class IUnitOfWork(Protocol):
    def __init__(self):
        raise NotImplementedError

    async def __aenter__(self):
        raise NotImplementedError

    async def __aexit__(self, *args):
        raise NotImplementedError

    async def commit(self):
        raise NotImplementedError

    async def rollback(self):
        raise NotImplementedError


class UnitOfWork(IUnitOfWork):
    def __init__(self, db_session_factory):
        self.db_session_factory = db_session_factory
    
    def __enter__(self):
        self.db_session = self.db_session_factory()
        self.tasks = TaskRepository(self.db_session)
        return self
    
    def __exit__(self, *args):
        self.rollback()
        self.db_session.close()

    def commit(self):
        self.db_session.commit()

    def rollback(self):
        self.db_session.rollback()