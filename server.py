import json
from flask import Flask

app = Flask(__name__)


baloons = [{'Firm': 'Maker Street', 'paint_code': 'ms400-504', 'color': 'grey-blue', 'volume': 400, 'starting weight': 300},
           {'Firm': 'Maker Street', 'paint_code': 'ms400-101', 'color': 'yellow', 'volume': 400, 'starting weight': 300},]

app.get('/api/baloons')
def get_baloons():
    return baloons


if __name__ == "__main__":
    app.run(debug=True)