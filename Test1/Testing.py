from flask import Flask , request
from flask_restful import Resource , Api , reqparse

class GetName(Resource):
    def get(self):
        return {"mag":"Praveen Kumar"}