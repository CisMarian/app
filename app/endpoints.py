from flask import request
from marshmallow import Schema, fields, ValidationError
from flask_restful import Resource
from services import Services
import logging

log = logging.getLogger(__name__)

services = Services()


class NoteInputSchema(Schema):
    title = fields.String(required=True)
    content = fields.String(required=True)


class UserInputSchema(Schema):
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)


class Notes(Resource):
    def get(self):
        log.info('Pobrano notatki')
        notes = services.get_notes()
        return notes

    def post(self):
        log.info('zapisano notatkę')
        try:
            data = NoteInputSchema().load(request.json)
            services.save_note(data)
            return {
                "message": "Dodaj notatkę"
            }
        except ValidationError as e:
            return {
                'error', str(e)
            }, 400


class Note(Resource):
    def get(self, note_id):
        log.info('Pobrano informację o notatce{}'.format(note_id))

    def patch(self, note_id):
        log.info('Zaktualizowano rekord{}'.format(note_id))
        try:
            data = NoteInputSchema().load(request.json)
            services.patch_note(note_id, data)
            return {
                "message": "Zaktualizuj rekord {}".format(note_id)
            }
        except ValidationError as e:
            return {
                'error': str(e)
            }, 400

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
        try:
            data = UserInputSchema().load(request.json)
            services.save_user(data)
            return {
                "message": "Dodaj użytkownika"
            }
        except ValidationError as e:
            return {
                'error': str(e)
            }, 400


class Profile(Resource):
    def get(self, user_id):
        log.info('Pobrano informację o użytkowniku {}'.format(user_id))

    def patch(self, user_id):
        log.info('Zaktualizowano profil użytkownika {}'.format(user_id))
        try:
            data = UserInputSchema().load(request.json)
            services.patch_user(user_id, data)
            return {
                "message": "Zaktualizuj profil użytkownika {}".format(user_id)
            }
        except ValidationError as e:
            return {
                'error': str(e)
            }, 400

    def delete(self, user_id):
        log.info('Usunięto użytkownika {}'.format(user_id))
        services.delete_user(user_id)
        return {
            "message": "Usuń użytkownika {}".format(user_id)
        }
