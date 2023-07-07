from app.endpoints import Note, Notes, Users, Profile
from extensions import api

api.add_resource(Note, '/note/<int:note_id')
api.add_resource(Notes, '/notes')
api.add_resource(Users, '/users')
api.add_resource(Profile, '/profile/<int:user_id')
