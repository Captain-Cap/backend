import json
from flask import Flask, request, abort
from flask import Blueprint
from storage import BaloonsStorage


routes = Blueprint("balloons", __name__)
storage = BaloonsStorage()


@routes.get('/')
def get_baloons():
    storage.get_all()


@routes.get('/<int:id>')
def get_baloon_by_id(id):
    try:
        return storage.get_balloon_by_id(id)
    except ValueError:
        abort(404, "balloon not found")


@routes.post('/')
def add_baloons():
    try:
        return storage.add(request.json)
    except ValueError:
        abort(409, "such id already exists")


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
