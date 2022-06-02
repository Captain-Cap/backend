from flask import request, abort, Blueprint
from cap.storage import BalloonsStorage
from cap.errors import ConflictError, NotFoundError


routes = Blueprint("balloons", __name__)
storage = BalloonsStorage()


@routes.get('/')
def get_balloons():
    return storage.get_all()


@routes.get('/<int:id>')
def get_balloon_by_id(id):
    return storage.get_balloon_by_id(id)


@routes.post('/')
def add_balloon():
    storage.add(request.json)
    return request.json


@routes.delete('/<int:id>')
def del_balloon(id):
    storage.delete(id)
    return {}, 204


@routes.put('/')
def change_balloon():
    storage.update(request.json)
    return request.json