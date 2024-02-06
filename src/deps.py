from src.database.uow import UnitOfWork
from src.database.session import session_factory
from src.services.tasks import TaskService


def get_task_service():
    return TaskService(UnitOfWork(session_factory))