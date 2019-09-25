from flask import Flask,request,jsonify
from flask_restful import Resource,Api,reqparse
import json
from QueryData.QueryData import *

class DeleteMapData(Resource):

    def __init__(self,**kwargs): 
        self.db = kwargs['data']
    
    def post(self):
        userData = request.get_json(force = True)
        query = "DELETE FROM map_data WHERE map_data_id = {0}".format(str(userData["map_data_id"]))
        value=()
        queryData = QueryData(self.db)
        data = queryData.insertAndUpdateQueryMethod(query, value)
        
        if data["Inserted Row"] ==1:
            return  {"data":[{"Deleted Row":1}]} 
        else:
            return {"data":[],"Error_msg":"map_data with given id doesnot exist"}