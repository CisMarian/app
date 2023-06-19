from .init import api
from .endpoints import Notes, Note, Profile, Users


api.add_resource(Note, '/notes/<int:note_id')
api.add_resource(Notes, '/notes')
api.add_resource(Users, '/users')
api.add_resource(Profile, 'profile/<int:user_id')
