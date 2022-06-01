from flask import Flask
from cap.views import ballons



app = Flask(__name__)
app.register_blueprint(ballons.routes, url_prefix='/api/v1/balloons/')


if __name__ == "__main__":
    app.run(debug=True)