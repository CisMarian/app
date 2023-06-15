from flask import request
from flask_restful import Resource

# from services import NotesServices


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
            "data": data
        }


class Notes2(Resource):
    def get(self):
        return {
            "status": "git",
            "data": "jakies dane siê tutaj znajduj¹"
        }

    def post(self):
        data = request.get.json()
        return {
            "status": "git",
            "data": data
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
            "data": data
        }
