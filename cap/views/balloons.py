import logging

import orjson
from flask import Blueprint, request

from cap.schemas import CorrectBalloon
from cap.sql_storage import BalloonsStorage

logger = logging.getLogger(__name__)

routes = Blueprint('balloons', __name__)
sql_storage = BalloonsStorage()


@routes.get('/')
def get_balloons():
    logger.debug('request get balloons')
    balloons = sql_storage.get_all()
    return orjson.dumps([CorrectBalloon.from_orm(entity).dict() for entity in balloons])


@routes.get('/<int:uid>')
def get_balloon_by_id(uid):
    logger.debug('request get balloon on id')
    entity = sql_storage.get_balloon_by_id(uid)
    return CorrectBalloon.from_orm(entity).dict()


@routes.post('/')
def add_balloon():
    logger.debug('request add balloon')
    payload = request.json
    balloon = CorrectBalloon(**payload)
    entity = sql_storage.add(balloon)
    return orjson.dumps(CorrectBalloon.from_orm(entity).dict())


@routes.delete('/<int:uid>')
def del_balloon(uid):
    logger.debug('request delete balloon')
    sql_storage.delete(uid)
    return {}, 204


@routes.put('/')
def change_balloon():
    payload = request.json
    balloon = CorrectBalloon(**payload)
    entity = sql_storage.update(balloon)
    return CorrectBalloon.from_orm(entity).dict()
