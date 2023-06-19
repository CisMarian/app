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
            "message": "Dodaj notatkƒô"
        }


class Note(Resource):
    def get(self, note_id):
        return {
            "message": "Pobierz informacje o notatce {}".format(note_id)
        }

    def patch(self, note_id):
        return {
            "message": "Zaktualizuj rekord {}".format(note_id)
        }

    def delete(self, note_id):
        return {
            "message": "Usu≈Ñ notatkƒô {}".format(note_id)
        }


class Users(Resource):
    def get(self):
        return {
            "message": "Lista u≈ºytkownik√≥w",
        }

    def post(self):
        return {
            "message": "Dodaj u≈ºytkownika"
        }


class Profile(Resource):
    def get(self, user_id):
        return {
            "message": "Pobierz informacje o u≈ºytkowniku {}".format(user_id)
        }

    def patch(self, user_id):
        return {
            "message": "Zaktualizuj profil u≈ºytkownika {}".format(user_id)
        }

    def delete(self, user_id):
        return {
            "message": "Usu≈Ñ u≈ºytkownika {}".format(user_id)
        }


class Users(Resource):
    def get(self):
        return {
            "message": "Lista uøytkownikÛw",
        }

    def post(self):
        return {
            "message": "Dodaj uøytkownika"
        }


class Profile(Resource):
    def get(self, user_id):
        return {
            "message": f"Pobierz informacje o uøytkowniku {user_id}"
        }

    def patch(self, user_id):
        return {
            "message": f"Zaktualizuj profil uøytkownika {user_id}"
        }

    def delete(self, user_id):
        return {
            "message": f"UsuÒ uøytkownika {user_id}"
        }
