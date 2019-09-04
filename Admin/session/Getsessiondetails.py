from flask import Flask,request,jsonify
from flask_restful import Resource, Api, reqparse
import json
from QueryData.QueryData import *

class Getsessiondetails(Resource):
    def __init__(self,**kwargs):
        self.db=kwargs['data']
    def get(self,sessionid):

        sessionid=sessionid
        query="SELECT session.*,speaker.speaker_id,speaker.role,attendee.id,attendee.attendee_name,attendee.attendee_email,attendee_contact_num,attendee.prof_img FROM session JOIN speaker ON session.session_id=speaker.session_id JOIN attendee ON speaker.speaker_id=attendee.id WHERE session.session_id={}".format (str(sessionid))
        queryData=QueryData(self.db)
        data=queryData.selectQueryMethod(query)
        #return jsonify(data)
        if len(data) != 0:
            return parseData(data)
            #return data
        else:
            return{},202

def parseData(data):
    parsedData = {}
    for x in data:        
        parsedData["session_desc"]=x["session_desc"]
        parsedData["session_id"]=x["session_id"]
        parsedData["session_topic"]=x["session_topic"]
        parsedData["session_type"]=x["session_type"]
        parsedData["start_time"]=x["start_time"].strftime("%Y-%m-%d %H:%M:%S")
        parsedData["end_time"]=x["end_time"].strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            if(len(parsedData["sessionData"]) == 0 ):
                temp_val = {
                    "speaker_id":x["speaker_id"],
                    "role":x["role"],
                    "attendee_contact_num" :x["attendee_contact_num"],
                    "attendee_email":x["attendee_email"],
                    "attendee_name" :x["attendee_name"],
                    "id": x["id"],
                    "prof_img" :x["prof_img"]
                    
                    
                    
                }
                parsedData["sessionData"].append(temp_val) 
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
                parsedData["sessionData"].append(temp_val)
        except:
            parsedData["sessionData"] = []
            if(len(parsedData["sessionData"]) == 0):
                parsedData["sessionData"] = []
                temp_val = {
                    "speaker_id":x["speaker_id"],
                    "role":x["role"],
                    "attendee_contact_num" :x["attendee_contact_num"],
                    "attendee_email":x["attendee_email"],
                    "attendee_name": x["attendee_name"],
                    "id": x["id"],
                    "prof_img" :x["prof_img"]
                }
                parsedData["sessionData"].append(temp_val)
    return parsedData