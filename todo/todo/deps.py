from todo.database.uow import UnitOfWork
from todo.database.session import session_factory
from todo.services.tasks import TaskService


def get_task_service():
    return TaskService(UnitOfWork(session_factory))