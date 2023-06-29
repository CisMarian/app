import logging
from tools.jsondb import Database

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class Services:
    def save_user(self, fields: dict):
        db = Database('users')
        if fields.get('id'):
            log.warning('Użytkownik jest już zarejetrowany')
            log.warning('Zaktualizowano użytkownika')
            return db.update(fields)
        else:
            log.info('Dodano użytkowika"')
            return db.add(fields)

    def get_users(self, ident=None):
        db = Database('users')
        if ident:
            log.info('Pobrano użytkownika o ID: {}'.format(ident))
            return db.get_by_id(ident)
        else:
            log.info('Pobrano użytkowników')
            return db.get_all()

    def patch_user(self, fields: dict):
        db = Database('users')
        if fields.get('id'):
            user = db.get_by_id(fields['id'])
            if user:
                log.info('Zaktualizowano użytkownika {}'.format(fields['id']))
                return db.update(fields)
            else:
                log.error('Użytkownik {} nie istnieje'.format(fields['id']))
                raise Exception('Użytkownik o podanym ID nie istnieje')
        else:
            log.error('Nie znaleziono użytkownika. Dodano nowego użytkownika')
            return db.add(fields)

    def delete_user(self, ident):
        db = Database('users')
        log.info('Usunięto użytkownika')
        return db.delete(ident)

    def save_note(self, fields: dict):
        db = Database('notes')
        if fields.get('id'):
            log.warning('Zaktualizowano istniejącą notatkę')
            return db.update(fields)
        else:
            log.info('Dodano notatkę')
            return db.add(fields)

    def get_notes(self, ident=None):
        db = Database('notes')
        if ident:
            log.info('Pobrano notatkę')
            return db.get_by_id(ident)
        else:
            log.info('Pobrano wszytskie notatki')
            return db.get_all()

    def patch_note(self, fields: dict):
        db = Database('notes')
        if fields.get('id'):
            note = db.get_by_id(fields['id'])
            if note:
                log.info('Zaktualizowano notatkę')
                return db.update(fields)
            else:
                log.error('Notatka nie istnieje')
                raise Exception('Notatka o podanym ID nie istnieje')
        else:
            log.warning('Dodano nową notatkę')
            return db.add(fields)

    def delete_notes(self, ident):
        db = Database('notes')
        log.info('Usunięto notatkę')
        return db.delete(ident)
