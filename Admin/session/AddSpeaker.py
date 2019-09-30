from flask import Flask, request , jsonify
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource, reqparse
import json
from QueryData.QueryData import *

class AddSpeakers(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']
    
    def post(self):
        userData = request.get_json(force=True)
        checkAttendee = checkattendeeFromData(self.db,userData)
        if(len(checkAttendee) > 0):
            insertSpeakersRes = insertSpeakers(self.db,userData) 
            return {
                "data":[insertSpeakersRes],
                "Error_msg":"The credientials are invalid"
            }        
        else:
            return {
                "data":[],
                "Error_msg":"The credientials are invalid"
            }

def checkattendeeFromData(db,userData):
    query = "SELECT * FROM attendee WHERE id = {0}".format(str(userData["id"])) 
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data

def insertSpeakers(db,userData):
    query = "INSERT INTO speaker(speaker_id,role,session_id,event_id) VALUES(%s,%s,%s,%s)"
    value = (str(userData["id"]),str(userData["role"]),str(userData["session_id"]),str(userData["event_id"])) 
    queryData = QueryData(db)
    data = queryData.insertAndUpdateQueryMethod(query,value)
    return data

