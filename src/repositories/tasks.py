from typing import List

from sqlalchemy import select, update, insert, delete, exists

from src.database.models import Task
from src.services.dto import TaskDTO


class TaskRepository:
    model = Task

    def __init__(self, session):
        self._session = session

    def get_task(self, pk: int) -> TaskDTO:
        query = select(self.model).filter_by(id=pk)
        res = self._session.execute(query)
        task = res.scalar_one()
        return TaskDTO.model_validate(task, from_attributes=True)
    
    def get_tasks(self) -> List[TaskDTO]:
        query = select(self.model)
        res = self._session.execute(query)
        tasks = res.scalars().all()
        return [TaskDTO.model_validate(task, from_attributes=True) for task in tasks]
    
    def update_task(self, pk: int, **values) -> TaskDTO:
        stmt = (
            update(self.model)
            .filter_by(id=pk)
            .values(**values)
            .returning(self.model)
        )
        res = self._session.execute(stmt)
        task = res.scalar_one()
        return TaskDTO.model_validate(task, from_attributes=True)
    
    def create_task(self, **values) -> TaskDTO:
        stmt = (
            insert(self.model)
            .values(**values)
            .returning(self.model)
        )
        res = self._session.execute(stmt)
        task = res.scalar_one()
        return TaskDTO.model_validate(task, from_attributes=True)
    
    def delete_task(self, pk: int) -> None:
        stmt = (
            delete(self.model)
            .filter_by(id=pk)
            .returning(self.model)
        )
        self._session.execute(stmt)

    def exists(self, **filter_by) -> bool:
        stmt = select(self.model).filter_by(**filter_by)
        stmt = exists(stmt).select()
        res = self._session.execute(stmt)
        return res.scalar_one()

        

