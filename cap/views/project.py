import orjson
from flask import Blueprint, request

from cap.project_storage import ProjectStorage
from cap.schemas import CorrectProject

routes = Blueprint('project', __name__)
pro_storage = ProjectStorage()


@routes.post('/')
def add():
    payload = request.json
    project = CorrectProject(**payload)
    entity = pro_storage.add(project)
    return orjson.dumps(CorrectProject.from_orm(entity).dict())


@routes.get('/')
def get_projects():
    projects = pro_storage.get_all()
    return orjson.dumps([CorrectProject.from_orm(entity).dict() for entity in projects])


@routes.delete('/<int:uid>')
def del_balloon(uid):
    pro_storage.delete(uid)
    return {}, 204


@routes.get('/<int:uid>')
def get_balloon_by_id(uid):
    entity = pro_storage.get_balloon_by_id(uid)
    return CorrectProject.from_orm(entity).dict()


@routes.put('/')
def change_project():
    payload = request.json
    balloon = CorrectProject(**payload)
    entity = pro_storage.update(balloon)
    return CorrectProject.from_orm(entity).dict()
