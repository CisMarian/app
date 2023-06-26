import json


class Services:
    def save_user(self, fields: dict):
        users = self._load_users()
        user_id = fields.get('id')

        if user_id:
            for user in users:
                if user['id'] == user_id:
                    break

        else:
            user_id = self._generate_user_id(users)
            fields['id'] = user_id
            users.append(fields)

        self._save_users(users)

    def get_users(self, ident=None):
        users = self._load_users()

        if ident:
            return list(filter(lambda user: user['id'] == ident, users))

        return users

    def patch_user(self, user_id, updated_fields):
        users = self._load_users()
        for user in users:
            if user['id'] == user_id:
                user.update(updated_fields)
                break
        self._save_users(users)

    def delete_user(self, ident):
        users = self._load_users()
        updated_users = list(filter(lambda user: user['id'] != ident, users))
        self._save_users(updated_users)

    def _load_users(self):
        try:
            with open('users.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def _save_users(self, users):
        try:
            with open('users.json', 'w') as f:
                json.dump(users, f)
        except FileNotFoundError:
            return []

    def _generate_user_id(self, users):
        if not users:
            return 1

        max_id = max(users, key=lambda user: user.get('id', 0)).get('id', 0)
        return max_id + 1

    def save_note(self, fields: dict):
        notes = self._load_notes()
        note_id = fields.get('id')

        if note_id:
            for note in notes:
                if note['id'] == note_id:
                    break

        else:
            note_id = self._generate_note_id()
            fields['id'] = note_id
            notes.append(fields)

        self._save_notes(notes)

    def get_notes(self, ident=None):
        notes = self._load_notes()

        if ident:
            return list(filter(lambda note: note['id'] == ident, notes))

        return notes

    def patch_note(self, note_id, updated_fields):
        notes = self._load_notes()
        for note in notes:
            if note['id'] == note_id:
                note.update(updated_fields)
                break
        self._save_notes(notes)

    def delete_notes(self, ident):
        notes = self._load_notes()
        updated_notes = list(filter(lambda note: note['id'] != ident, notes))
        self._save_notes(updated_notes)

    def _load_notes(self):
        try:
            with open('notes.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def _save_notes(self, notes):
        with open('notes.json', 'w') as f:
            json.dump(notes, f)

    def _generate_note_id(self, notes):
        if not notes:
            return 1

        max_id = max(notes, key=lambda note: note.get('id', 0)).get('id', 0)
        return max_id + 1
