import json
import logging
from flask import request, Blueprint
from cap.storage import BalloonsStorage
from cap.schemas import CorrectBalloon


logger = logging.getLogger(__name__)

routes = Blueprint("balloons", __name__)
storage = BalloonsStorage()


@routes.get('/')
def get_balloons():
    logger.debug("request get balloons")
    balloons =  storage.get_all()
    return json.dumps([balloon.dict() for balloon in balloons])


@routes.get('/<int:uid>')
def get_balloon_by_id(uid):
    logger.debug("request get balloon on id")
    return storage.get_balloon_by_id(uid)


@routes.post('/')
def add_balloon():
    logger.debug("request add balloon")
    payload = request.json
    balloon = CorrectBalloon(**payload)
    balloon = storage.add(balloon)
    return balloon.dict()


@routes.delete('/<int:uid>')
def del_balloon(uid):
    logger.debug("request delete balloon")
    storage.delete(uid)
    return {}, 204


@routes.put('/<int:uid>')
def change_balloon(uid):
    payload = request.json
    balloon = CorrectBalloon(**payload)
    balloon = storage.update(balloon)
    return balloon.dict()