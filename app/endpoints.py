from flask import request
from flask_restful import Resource
from .services import Services
import logging

log = logging.getLogger(__name__)

services = Services()


class Notes(Resource):
    def get(self):
        log.info('Pobrano notatki')
        notes = services.get_notes()
        return notes

    def post(self):
        log.info('zapisano notatkę')
        services.save_note(request.json)
        return {
            "message": "Dodaj notatkę"
        }


class Note(Resource):
    def get(self, note_id):
        log.info('Pobrano informację o notatce{}'.format(note_id))
        return {
            "message": "Pobierz informacje o notatce {}".format(note_id)
        }

    def patch(self, note_id):
        log.info('Zaktualizowano rekord{}'.format(note_id))
        updated_fields = request.json
        services.patch_note(note_id, updated_fields)
        return {
            "message": "Zaktualizuj rekord {}".format(note_id)
        }

    def delete(self, note_id):
        log.info('Usunięto notatkę {}'.format(note_id))
        services.delete_notes(note_id)
        return {
            "message": "Usuń notatkę {}".format(note_id)
        }


class Users(Resource):
    def get(self):
        log.info('Pobrano użytkowników')
        users = services.get_users()
        return users

    def post(self):
        log.info('Pobrano użytkownika')
        services.save_user(request.json)
        return {
            "message": "Dodaj użytkownika"
        }


class Profile(Resource):
    def get(self, user_id):
        log.info('Pobrano informację o użytkowniku {}'.format(user_id))
        return {
            "message": "Pobierz informacje o użytkowniku {}".format(user_id)
        }

    def patch(self, user_id):
        log.info('Zaktualizowano profil użytkownika {}'.format(user_id))
        updated_fields = request.json
        services.patch_user(user_id, updated_fields)
        return {
            "message": "Zaktualizuj profil użytkownika {}".format(user_id)
        }

    def delete(self, user_id):
        log.info('Usunięto użytkownika {}'.format(user_id))
        services.delete_user(user_id)
        return {
            "message": "Usuń użytkownika {}".format(user_id)
        }
