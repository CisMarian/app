# from flask import request
from flask_restful import Resource

# from services import NotesServices

notes = []


class NotesList(Resource):
    def get(self):
        return {
            "message": "Lista notatek",
        }

    def post(self):
        return {
            "message": "Dodaj notatk�"
        }


class Notes(Resource):
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
            "message": f"Usu� notatk� {note_id}"
        }
