from app.extensions import api
from flask import Flask

import logging
log = logging.getLogger(__name__)


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    with app.app_context():
        api.app = app

        # from .app import routes

        api.init_app(app)
        return app
