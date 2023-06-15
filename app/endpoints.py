from flask import request
from flask_restful import Resource

from services import NotesServices


class Notes(Resource):
    def get(self):
        return {
            "status": "ok",
            "data": "jakies dane"
        }

    def post(self):
        data = request.get.json()
        return {
            "status": "ok",
            "data": "tutaj powinny si� znale�� wys�ane dane"
        }
   

class Notes2(Resource):
    def get(self):
        return {
            "status": "git",
            "data": "jakies dane si� tutaj znajduj�"
        }

    def post(self):
        data = request.get.json()
        return {
            "status": "git",
            "data": "mo�e kiedy� znajd� si� tutaj jakie� dane"
        }


class Notes3(Resource):
    def get(self):
        return {
            "status": "spk",
            "data": "jakies dane"
        }

    def post(self):
        data = request.get.json()
        return {
            "status": "forever young, i wanna be, forever youuung",
            "data": "Do you really want to live forever?"
        }
