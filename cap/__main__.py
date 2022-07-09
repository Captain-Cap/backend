import logging

from flask import Flask
from pydantic import ValidationError

from cap.db import db_session
from cap.errors import AppError
from cap.views import balloons, project

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def handle_app_errors(error: AppError):
    logger.warning(error.reason)
    return {'error': error.reason}, error.status


def handle_validation_errors(error: ValidationError):
    logger.warning(str(error))
    return {'error': error.errors()}, 422


def shutdown_session(exception=None):
    db_session.remove()


app = Flask(__name__)

app.register_blueprint(project.routes, url_prefix='/api/v1/projects/')
app.register_blueprint(balloons.routes, url_prefix='/api/v1/balloons/')

app.register_error_handler(AppError, handle_app_errors)
app.register_error_handler(ValidationError, handle_validation_errors)

app.teardown_appcontext(shutdown_session)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
