import json
from flask import Flask, request, abort
from views import ballons



app = Flask(__name__)
app.register_blueprint(ballons.routes, url_prefix='/api/v1/balloons')


baloons = {
    1: {'id': 1, 'Firm': 'Maker Street', 'paint_code': 'ms400-504', 'color': 'grey-blue', 'volume': 400, 'starting_weight': 300},
    2: {'id': 2, 'Firm': 'Maker Street', 'paint_code': 'ms400-101', 'color': 'yellow', 'volume': 400, 'starting_weight': 300},
}
        

@app.get('/api/v1/baloons/')
def get_baloons():
    return json.dumps(baloons)


@app.get('/api/v1/baloons/<int:id>')
def get_baloon_by_id(id):
    baloon = baloons.get(id)
    if not baloon:
        abort(404, "balloon not found")
    return baloon


@app.post('/api/v1/baloons/')
def add_baloons():
    payload = request.json
    id_payload = payload['id']
    baloon = baloons.get(id_payload)
    if baloon:
        abort(409, "such id already exists")
    baloons[id_payload] = payload
    return payload


@app.delete('/api/v1/baloons/<int:id>')
def del_baloon(id):
    baloon = baloons.get(id)
    if not baloon:
        abort(404, "id does not exist")
    del baloons[id]
    return {}, 204


@app.put('/api/v1/baloons/')
def changed_balloon():
    payload = request.json
    id_payload = payload['id']
    baloon = baloons.get(id_payload)
    if not baloon:
        abort(404, "id does not exist")
    baloons[id_payload] = payload
    return payload


if __name__ == "__main__":
    app.run(debug=True)