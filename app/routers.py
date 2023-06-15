from .init import api
from .endpoints import Notes


api.add_resource(Notes, '/')
