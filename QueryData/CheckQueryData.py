from flask import Flask , request
from flask_restful import Api , Resource , reqparse
from QueryData.QueryData import QueryData
class Sample(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']
    def get(self):
        qD = QueryData(self.db)
        data = qD.selectQueryMethod("SELECT * FROM map_data")
        return data
