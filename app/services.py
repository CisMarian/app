from tools.jsondb import Database


class Services:
    def __init__(self):
        self.db = Database()

    def save_user(self, fields: dict):
        db = Database('users')
        if fields.get('id'):
            return db.update(fields)
        else:
            return db.add(fields)

    def get_users(self, ident=None):
        db = Database('users')
        if ident:
            return db.get_by_id(ident)
        else:
            return db.get_all()

    def patch_user(self, fields: dict):
        db = Database('users')
        if fields.get('id'):
            user = db.get_by_id(fields['id'])
            if user:
                return db.update(fields)
            else:
                raise Exception('Użytkownik o podanym ID nie istnieje')
        else:
            return db.add(fields)

    def delete_user(self, ident):
        db = Database('users')
        return db.delete(ident)

    def save_note(self, fields: dict):
        db = Database('notes')
        if fields.get('id'):
            return db.update(fields)
        else:
            return db.add(fields)

    def get_notes(self, ident=None):
        db = Database('notes')
        if ident:
            return db.get_by_id(ident)
        else:
            return db.get_all()

    def patch_note(self, fields: dict):
        db = Database('notes')
        if fields.get('id'):
            note = db.get_by_id(fields['id'])
            if note:
                return db.update(fields)
            else:
                raise Exception('Notatka o tym ID nie istnieje')
        else:
            return db.add(fields)

    def delete_notes(self, ident):
        db = Database('notes')
        return db.delete(ident)
