from flask import Flask,request,jsonify
from flask_restful import Resource,Api,reqparse
import json
from QueryData.QueryData import *

class DeleteSessionFiles(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']
    
    def post(self):
        userData = request.get_json(force=True)
        query = "UPDATE session_files SET session_id = 0 WHERE session_file_id = {0}".format(str(userData["session_file_id"]))
        queryData =  QueryData(self.db)
        data = queryData.insertAndUpdateQueryMethod(query,()) 
        if(data["Inserted Row"] == 1):
            return {
                "data":[data] 
            }
        else:
            return {
                "data":[],
                "Error_msg":"The session file is not available." 
            }
