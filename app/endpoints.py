from flask import request
from flask_restful import Resource
from services import Services

services = Services()


class Notes(Resource):
    def get(self):
        notes = services.get_notes()
        return notes

    def post(self):
        services.save_note(request.json)
        return {
            "message": "Dodaj notatkę"
        }


class Note(Resource):
    def get(self, note_id):
        return {
            "message": "Pobierz informacje o notatce {}".format(note_id)
        }

    def patch(self, note_id):
        updated_fields = request.json
        services.patch_note(note_id, updated_fields)
        return {
            "message": "Zaktualizuj rekord {}".format(note_id)
        }

    def delete(self, note_id):
        services.delete_notes(note_id)
        return {
            "message": "Usuń notatkę {}".format(note_id)
        }


class Users(Resource):
    def get(self):
        users = services.get_users()
        return users

    def post(self):
        services.save_user(request.json)
        return {
            "message": "Dodaj użytkownika"
        }


class Profile(Resource):
    def get(self, user_id):
        return {
            "message": "Pobierz informacje o użytkowniku {}".format(user_id)
        }

    def patch(self, user_id):
        updated_fields = request.json
        services.patch_user(user_id, updated_fields)
        return {
            "message": "Zaktualizuj profil użytkownika {}".format(user_id)
        }

    def delete(self, user_id):
        services.delete_user(user_id)
        return {
            "message": "Usuń użytkownika {}".format(user_id)
        }
