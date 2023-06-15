from .init import api
from .endpoints import Notes, Notes2, Notes3


api.add_resource(Notes, '/')

api.add_resource(Notes2, "/2")

api.add_resource(Notes3, "/3")
