from .init import api
from .endpoints import Notes, NotesList


api.add_resource(Notes, '/notes/<int:note_id')
api.add_resource(NotesList, '/notes')
