from flask import Flask,request,jsonify
from flask_restful import Resource, Api, reqparse
import json
from QueryData.QueryData import *

class Getsessiondetails(Resource):
    def __init__(self,**kwargs):
        self.db=kwargs['data']
    def get(self,sessionid):

        sessionid=sessionid
        query="SELECT speaker.speaker_id,speaker.role,attendee.id,attendee.attendee_name,attendee.attendee_email,attendee_contact_num,attendee.prof_img FROM session JOIN speaker ON session.session_id=speaker.session_id JOIN attendee ON speaker.speaker_id=attendee.id WHERE session.session_id={}".format (str(sessionid))
        queryData=QueryData(self.db)
        data=queryData.selectQueryMethod(query)
        
        if len(data) != 0:
            return [ addUsers(getUser(self.db,sessionid),parseData(data)) ]
            #return data
        else:
            return[],202

def parseData(data):
    parsedData = {}
    for x in data:        
        parsedData["session_desc"]=x["session_desc"]
        parsedData["session_id"]=x["session_id"]
        parsedData["session_topic"]=x["session_topic"]
        parsedData["session_type"]=x["session_type"]
        parsedData["session_image"] = x["session_image"]
        parsedData["start_time"]=x["start_time"].strftime("%Y-%m-%d %H:%M:%S")
        parsedData["end_time"]=x["end_time"].strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            if(len(parsedData["speaker_data"]) == 0 ):
                temp_val = {
                    "speaker_id":x["speaker_id"],
                    "role":x["role"],
                    "attendee_contact_num" :x["attendee_contact_num"],
                    "attendee_email":x["attendee_email"],
                    "attendee_name" :x["attendee_name"],
                    "id": x["id"],
                    "prof_img" :x["prof_img"]                  
                }
                parsedData["speaker_data"].append(temp_val) 
            else:
                temp_val = {
                    "speaker_id":x["speaker_id"],
                    "role":x["role"],
                    "attendee_contact_num" : x["attendee_contact_num"],
                    "attendee_email": x["attendee_email"],
                    "attendee_name" : x["attendee_name"],
                    "id": x["id"],
                    "prof_img" : x["prof_img"]
                }
                parsedData["speaker_data"].append(temp_val)
        except:
            parsedData["speaker_data"] = []
            if(len(parsedData["speaker_data"]) == 0):
                parsedData["speaker_data"] = []
                temp_val = {
                    "speaker_id":x["speaker_id"],
                    "role":x["role"],
                    "attendee_contact_num" :x["attendee_contact_num"],
                    "attendee_email":x["attendee_email"],
                    "attendee_name": x["attendee_name"],
                    "id": x["id"],
                    "prof_img" :x["prof_img"]
                }
                parsedData["speaker_data"].append(temp_val)
    return parsedData

def getSessionData(db,sessionId):
    query = "SELECT * FROM session WHERE session_id = {0}".format(str(sessionId)) 
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query) 
    return data



def addUsers(users,parsedData):
    parsedData["userData"] = []
    for x in users:
        parsedData["userData"].append(
            {
                "user_name":x["user_name"],
                "user_image":x["user_image"],
                "user_id":x["user_id"],
                "user_access_id":x["user_access_id"] 
            }
        )
    return parsedData

def getUser(db,sessionId):
    query = "SELECT user_access.*,users.* FROM users INNER JOIN user_access ON user_access.user_id = users.user_id WHERE user_access.session_id = {0}".format(str(sessionId))
    queryData=QueryData(db)
    data=queryData.selectQueryMethod(query)
    return data
