from .init import api
from .endpoints import Notes, Note


api.add_resource(Note, '/notes/<int:note_id')
api.add_resource(Notes, '/notes')
