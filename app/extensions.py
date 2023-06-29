from flask_restful import Api
from .tools import restful_error_messages

import logging
log = logging.getLogger(__name__)

api = Api(
    prefix='/api_v1', catch_all_404s=True, errors=restful_error_messages.errors
    )
