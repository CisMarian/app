# from flask import request
from flask_restful import Resource

# from services import NotesServices


class Notes(Resource):
    def get(self):
        return {
            "message": "Lista notatek",
        }

    def post(self):
        return {
            "message": "Dodaj notatkê"
        }


class Note(Resource):
    def get(self, note_id):
        return {
            "message": f"Pobierz informacje o notatce {note_id}"
        }

    def patch(self, note_id):
        return {
            "message": f"Zaktualizuj rekord {note_id}"
        }

    def delete(self, note_id):
        return {
            "message": f"Usuñ notatkê {note_id}"
        }


class Users(Resource):
    def get(self):
        return {
            "message": "Lista u¿ytkowników"
        }

    def post(self):
        return {
            "message": "Dodaj u¿ytkownika"
        }


class Profile(Resource):
    def get(self, user_id):
        return {
            "message": f"Informacje o u¿ytkowniku {user_id}"
        }

    def patch(self, user_id):
        return {
            "message": f"Edytuj dane u¿ytkownika {user_id}"
        }

    def delete(self, user_id):
        return {
            "message": f"Usuñ u¿ytkownika {user_id}"
        }
