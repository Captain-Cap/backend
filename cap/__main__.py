from flask import Flask
from cap.views import balloons



app = Flask(__name__)
app.register_blueprint(balloons.routes, url_prefix='/api/v1/balloons/')


if __name__ == "__main__":
    app.run(debug=True)