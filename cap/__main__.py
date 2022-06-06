import logging

from pydantic import ValidationError
from flask import Flask
from cap.views import balloons
from cap.errors import AppError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def handle_app_errors(error: AppError):
    logger.warning(error.reason)
    return {'error': error.reason}, error.status

def handle_validation_errors(error: ValidationError):
    logger.warning(str(error))
    return {'error': error.errors()}, 422


app = Flask(__name__)
app.register_blueprint(balloons.routes, url_prefix='/api/v1/balloons/')
app.register_error_handler(AppError, handle_app_errors)
app.register_error_handler(ValidationError, handle_validation_errors)


if __name__ == "__main__":
    app.run()