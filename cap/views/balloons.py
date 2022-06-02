import logging
from flask import request, Blueprint
from cap.storage import BalloonsStorage


logger = logging.getLogger(__name__)

routes = Blueprint("balloons", __name__)
storage = BalloonsStorage()


@routes.get('/')
def get_balloons():
    logger.debug("request get balloons")
    return storage.get_all()


@routes.get('/<int:id>')
def get_balloon_by_id(id):
    logger.debug("request get balloon on id")
    return storage.get_balloon_by_id(id)


@routes.post('/')
def add_balloon():
    logger.debug("request add balloon")
    storage.add(request.json)
    return request.json


@routes.delete('/<int:id>')
def del_balloon(id):
    logger.debug("request delete balloon")
    storage.delete(id)
    return {}, 204


@routes.put('/')
def change_balloon():
    storage.update(request.json)
    return request.json