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
            "message": "Dodaj notatkę"
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
            "message": f"Usuń notatkę {note_id}"
        }


class Users(Resource):
    def get(self):
        return {
            "message": "Lista użytkowników",
        }

    def post(self):
        return {
            "message": "Dodaj użytkownika"
        }


class Profile(Resource):
    def get(self, user_id):
        return {
            "message": f"Pobierz informacje o użytkowniku {user_id}"
        }

    def patch(self, user_id):
        return {
            "message": f"Zaktualizuj profil użytkownika {user_id}"
        }

    def delete(self, user_id):
        return {
            "message": f"Usuń użytkownika {user_id}"
        }
