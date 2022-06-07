import json
import logging
from flask import request, Blueprint
from cap.schemas import CorrectBalloon

from cap.storageSQL import BalloonsStorageSQL
from cap.models import Balloons


logger = logging.getLogger(__name__)

routes = Blueprint("balloons", __name__)
storageSQL = BalloonsStorageSQL()


def get_json(balloon: Balloons):
    json = {
        "uid": balloon.uid,
        "firm": balloon.firm,
        "paint_code": balloon.paint_code,
        "color": balloon.color,
        "volume": balloon.volume,
        "weight": balloon.weight,
        "created": balloon.created,
    }
    return json


@routes.get('/')
def get_balloons():
    logger.debug("request get balloons")
    balloons =  storageSQL.get_all()
    return json.dumps([get_json(balloon) for balloon in balloons], default=str)


@routes.get('/<int:uid>')
def get_balloon_by_id(uid):
    logger.debug("request get balloon on id")
    enitity = storageSQL.get_balloon_by_id(uid)
    return get_json(enitity)


@routes.post('/')
def add_balloon():
    logger.debug("request add balloon")
    payload = request.json
    balloon = CorrectBalloon(**payload)
    balloon = storageSQL.add(balloon)
    return get_json(balloon)


@routes.delete('/<int:uid>')
def del_balloon(uid):
    logger.debug("request delete balloon")
    storageSQL.delete(uid)
    return {}, 204


@routes.put('/<int:uid>')
def change_balloon(uid):
    payload = request.json
    balloon = CorrectBalloon(**payload)
    balloon = storageSQL.update(balloon)
    return get_json(balloon)