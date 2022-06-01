import json
from flask import Flask, request, abort
from flask import Blueprint


routes = Blueprint("balloons", __name__)


baloons = {
    1: {'id': 1, 'Firm': 'Maker Street', 'paint_code': 'ms400-504', 'color': 'grey-blue', 'volume': 400, 'starting_weight': 300},
    2: {'id': 2, 'Firm': 'Maker Street', 'paint_code': 'ms400-101', 'color': 'yellow', 'volume': 400, 'starting_weight': 300},
}


@routes.get('/')
def get_baloons():
    return json.dumps(baloons)


@routes.get('/<int:id>')
def get_baloon_by_id(id):
    baloon = baloons.get(id)
    if not baloon:
        abort(404, "balloon not found")
    return baloon


@routes.post('/')
def add_baloons():
    payload = request.json
    id_payload = payload['id']
    baloon = baloons.get(id_payload)
    if baloon:
        abort(409, "such id already exists")
    baloons[id_payload] = payload
    return payload


@routes.delete('/<int:id>')
def del_baloon(id):
    baloon = baloons.get(id)
    if not baloon:
        abort(404, "id does not exist")
    del baloons[id]
    return {}, 204


@routes.put('/')
def changed_balloon():
    payload = request.json
    id_payload = payload['id']
    baloon = baloons.get(id_payload)
    if not baloon:
        abort(404, "id does not exist")
    baloons[id_payload] = payload
    return payload
