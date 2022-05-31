import json
from flask import Flask, request

app = Flask(__name__)


baloons = [{'id': 1, 'Firm': 'Maker Street', 'paint_code': 'ms400-504', 'color': 'grey-blue', 'volume': 400, 'starting_weight': 300},
           {'id': 2, 'Firm': 'Maker Street', 'paint_code': 'ms400-101', 'color': 'yellow', 'volume': 400, 'starting_weight': 300},
        ]

@app.get('/api/v1/baloons/')
def get_baloons():
    return json.dumps(baloons)


@app.post('/api/v1/baloons/')
def add_baloons():
    payload = request.json
    baloons.append(payload)
    return payload


@app.put('/api/v1/baloons/')
def changed_balloon():
    payload = request.json

    for baloon in baloons:
        if baloon['id'] == payload['id']:
            baloons[baloons.index(baloon)] = payload
            return payload
    raise IndexError('id does not exist')


if __name__ == "__main__":
    app.run(debug=True)