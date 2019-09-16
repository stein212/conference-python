from flask import Flask, request,jsonify
from flask_restful import Resource, Api, reqparse
import json
from QueryData.QueryData import *

class GetAttendeeDetails(Resource):
    def __init__(self,**kwargs):
        self.db=kwargs['data']
    
    def get(self,eventId):
        user = getUser(self.db)
        attendee = getAttendee(self.db,eventId)
        return {"users":user,"attendee":attendee}

        
def getUser(db):
    query = "SELECT user_id,user_name,user_email,user_image FROM users ORDER BY user_email ASC"
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data

def getAttendee(db,eventId):
    query="SELECT id,attendee_name,attendee_email,prof_img FROM attendee WHERE event_id='{0}' ORDER BY attendee_email ASC ".format(str(eventId))
    queryData=QueryData(db)
    data=queryData.selectQueryMethod(query) 
    return data

