from typing import List

from src.database.uow import IUnitOfWork
from src.services.dto import TaskDTO


class TaskService:

    def __init__(self, uow: IUnitOfWork):
        self._uow = uow

    def get_task(self, pk: int) -> TaskDTO:
        with self._uow as uow:
            if not uow.tasks.exists(id=pk):
                return False
            task = uow.tasks.get_task(pk=pk)
        return task
    
    def get_tasks(self) -> List[TaskDTO]:
        with self._uow as uow:
            tasks = uow.tasks.get_tasks()
        return tasks
    
    def update(self, pk: int, **values) -> TaskDTO:
        with self._uow as uow:
            task = uow.tasks.update_task(pk=pk, **values)
            uow.commit()
        return task
    
    def create(self, **values) -> TaskDTO:
        with self._uow as uow:
            task = uow.tasks.create_task(**values)
            uow.commit()
        return task
    
    def delete(self, pk: int) -> None:
        with self._uow as uow:
            uow.tasks.delete_task(pk=pk)
            uow.commit()
    