from tools.jsondb import Database


class Services:
    def __init__(self):
        self.db = Database('namespace')

    def save_user(self, fields: dict):
        user_id = fields.get('id')
        users = self.db.get_all()

        if user_id:
            for user in users:
                if user['id'] == user_id:
                    break
        else:
            user_id = self._generate_user_id(users)
            fields['id'] = user_id
            self.db.add(fields)

    def get_users(self, ident=None):
        if ident:
            return self.db.get_by_id(ident)
        else:
            return self.db.get_all()

    def patch_user(self, user_id, updated_fields):
        users = self.db.get_all()
        for user in users:
            if user['id'] == user_id:
                user.update(updated_fields)
                self.db.update(user)

    def delete_user(self, ident):
        self.db.delete(ident)

    def _generate_user_id(self, users):
        if not users:
            return 1

        max_id = max(users, key=lambda user: user.get('id', 0)).get('id', 0)
        return max_id + 1

    def save_note(self, fields: dict):
        note_id = fields.get('id')
        notes = self.db.get_all()

        if note_id:
            for note in notes:
                if note['id'] == note_id:
                    break
        else:
            note_id = self._generate_note_id()
            fields['id'] = note_id
            self.db.add(fields)

    def get_notes(self, ident=None):
        if ident:
            return self.db.get_by_id(ident)
        else:
            return self.db.get_all()

    def patch_note(self, note_id, updated_fields):
        notes = self.db.get_all()
        for note in notes:
            if note['id'] == note_id:
                note.update(updated_fields)
                self.db.update(note)

    def delete_notes(self, ident):
        self.db.delete(ident)

    def _generate_note_id(self, notes):
        if not notes:
            return 1

        max_id = max(notes, key=lambda note: note.get('id', 0)).get('id', 0)
        return max_id + 1
