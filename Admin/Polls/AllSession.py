from flask import Flask , request , jsonify
from flask_restful import Api , Resource
import json
from QueryData.QueryData import *

class AllSession(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']
    
    def get(self):
        query = "SELECT * FROM "
