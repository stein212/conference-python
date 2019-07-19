from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import json

class AksQuestion(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']
    
    def past(self):
        return {"msg":"ok"}