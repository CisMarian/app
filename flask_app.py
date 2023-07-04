from app.extensions import api
from flask import Flask
from app.endpoints import Note, Notes, Users, Profile

import logging
log = logging.getLogger(__name__)


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    with app.app_context():
        api.app = app
        api.add_resource(Note, '/note/<int:note_id>')
        api.add_resource(Notes, '/notes')
        api.add_resource(Users, '/users')
        api.add_resource(Profile, '/profile/<int:user_id>')
        api.init_app(app)
        return app
