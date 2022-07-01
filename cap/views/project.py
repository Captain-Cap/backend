import orjson
from flask import Blueprint, request

from cap.project_storage import ProjectStorage
from cap.schemas import Project, CorrectBalloon

routes = Blueprint('project', __name__)
pro_storage = ProjectStorage()


@routes.post('/')
def add():
    payload = request.json
    payload['uid'] = -1
    project = Project(**payload)
    entity = pro_storage.add(project)
    return orjson.dumps(Project.from_orm(entity).dict())


@routes.get('/')
def get_projects():
    projects = pro_storage.get_all()
    return orjson.dumps([Project.from_orm(entity).dict() for entity in projects])


@routes.delete('/<int:uid>')
def delete(uid):
    pro_storage.delete(uid)
    return {}, 204


@routes.get('/<int:uid>')
def get_balloon_by_id(uid):
    entity = pro_storage.get_by_id(uid)
    return orjson.dumps(Project.from_orm(entity).dict())


@routes.put('/')
def change_project():
    payload = request.json
    balloon = Project(**payload)
    entity = pro_storage.update(balloon)
    return orjson.dumps(Project.from_orm(entity).dict())


@routes.get('/<int:uid>/balloons')
def get_balloons(uid):
    balloons = pro_storage.get_for_project(uid)
    return orjson.dumps([CorrectBalloon.from_orm(entity).dict() for entity in balloons])
