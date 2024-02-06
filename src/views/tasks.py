import json

from pyramid.view import view_config, view_defaults
from pyramid.request import Request
from pyramid.response import Response


from src.deps import get_task_service
from src.schemas.tasks import Task

@view_defaults(renderer='json')
class TaskView:
    def __init__(self, request: Request):
        self.request = request

    @view_config(route_name='task', request_method='GET')
    def retrieve(self):
        pk = self.request.matchdict.get('pk')
        task = get_task_service().get_task(pk)
        if task is False:
            respones = Response(json.dumps({"message": "Task does not exist"}), status=404)
            respones.content_type = 'application/json'
            return respones
        return task.model_dump()
    
    @view_config(route_name='list', request_method='GET')
    def list(self):
        tasks = get_task_service().get_tasks()
        return [task.model_dump() for task in tasks]
    
    @view_config(route_name='task', request_method='PUT')
    def update(self):
        pk = self.request.matchdict.get('pk')
        data = Task.model_validate(self.request.json_body)
        task = get_task_service().update(pk, **data.model_dump())
        if task is False:
            respones = Response(json.dumps({"message": "Task does not exist"}), status=404)
            respones.content_type = 'application/json'
            return respones
        return task.model_dump()
    
    @view_config(route_name='create', request_method='POST')
    def create(self):
        data = Task.model_validate(self.request.json_body)
        task = get_task_service().create(**data.model_dump())
        return task.model_dump()
    
    @view_config(route_name='task', request_method='DELETE')
    def delete(self):
        pk = self.request.matchdict.get('pk')
        task = get_task_service().delete(pk)
        if task is False:
            respones = Response(json.dumps({"message": "Task does not exist"}), status=404)
            respones.content_type = 'application/json'
            return respones
    

    
