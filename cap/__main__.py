from flask import Flask
from cap.views import ballons



app = Flask(__name__)
app.register_blueprint(ballons.routes, url_prefix='/api/v1/balloons')


baloons = {
    1: {'id': 1, 'Firm': 'Maker Street', 'paint_code': 'ms400-504', 'color': 'grey-blue', 'volume': 400, 'starting_weight': 300},
    2: {'id': 2, 'Firm': 'Maker Street', 'paint_code': 'ms400-101', 'color': 'yellow', 'volume': 400, 'starting_weight': 300},
}
 

if __name__ == "__main__":
    app.run(debug=True)