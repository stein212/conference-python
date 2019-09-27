from flask import Flask,request,jsonify
from flask_restful import Resource,Api,reqparse
import json
from QueryData.QueryData import *

class DeleteSpeaker(Resource):

    def __init__(self,**kwargs): 
        self.db = kwargs['data']
    
    def post(self):
        userData = request.get_json(force = True)
        query = "DELETE FROM speaker WHERE speaker_id = '{0}' AND session_id='{1}'".format(str(userData["speaker_id"]),str(userData["session_id"]))
        value=()
        queryData = QueryData(self.db)
        data = queryData.insertAndUpdateQueryMethod(query, value)
        
        if data["Inserted Row"] ==1:
            return  {"data":[{"Deleted Row":1}]} 
        else:
            return {"data":[],"Error_msg":"speaker with given id doesnot exist"}