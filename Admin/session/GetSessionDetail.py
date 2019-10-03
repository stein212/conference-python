from flask import Flask,request,jsonify
from flask_restful import Resource, Api, reqparse
import json
from QueryData.QueryData import *

class GetSessionDetailsById(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']
    
    def get(self,sessionid):
        sessionData = getSessionData(self.db,sessionid)
        
        if len(sessionData) > 0:
            speakerData = getSpeakerData(self.db,sessionid)
            response = addSpeakerData(sessionData[0],speakerData)
            userData = getUser(self.db,sessionid)
            # return userData
            response = addUsers(userData,response) 
            response = addFilesData(response,getFiles(self.db,sessionid)) 
            response["start_time"] = response["start_time"].strftime("%Y-%m-%d %H:%M:%S")
            response["end_time"] = response["end_time"].strftime("%Y-%m-%d %H:%M:%S")
            return [response] 
        
        else:
            return {
                "data":[],
                "Error_msg":"Session is not found."
            }    

def addSpeakerData(sessionData,speakerData):
    sessionData["speaker_data"] = []
    for x in speakerData:
        sessionData["speaker_data"].append({
                    "speaker_id":x["speaker_id"],
                    "role":x["role"],
                    "attendee_contact_num" :x["attendee_contact_num"],
                    "attendee_email":x["attendee_email"],
                    "attendee_name" :x["attendee_name"],
                    "id": x["id"],
                    "prof_img" :x["prof_img"]                  
                })
    return sessionData 




def getSessionData(db,sessionId):
    query = "SELECT * FROM session WHERE session_id = {0}".format(str(sessionId)) 
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query) 
    return data

def getSpeakerData(db,sessionId):
    query = "SELECT speaker.speaker_id,speaker.role,attendee.id,attendee.attendee_name,attendee.attendee_email,attendee_contact_num,attendee.prof_img FROM session JOIN speaker ON session.session_id=speaker.session_id JOIN attendee ON speaker.speaker_id=attendee.id WHERE session.session_id={}".format (str(sessionId))
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

def getFiles(db,sessionId):
    query = "SELECT * FROM session_files WHERE session_id = {0}".format(sessionId)
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data

def addFilesData(parsedData,fileData):
    parsedData["file_data"] = []
    for x in fileData:
        parsedData["file_data"].append(
            x
        )  
    return parsedData 