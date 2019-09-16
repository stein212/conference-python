from flask import Flask, request,jsonify
from flask_restful import Resource, Api, reqparse
import json
from QueryData.QueryData import *

class AddSession(Resource):
    def __init__(self,**kwargs):
        self.db=kwargs['data']
    
    def post(self):
        data=request.form
        userData = {
            "session_topic": data["schedule_topic"],
            "session_desc":data["schedule_description"],
            "start_time":data["schedule_start_time"],
            "end_time":data["schedule_end_time"],
            "location":data["location"],
            "event_id":data["event_id"],
            "speakers":json.loads(data["speakers"]),
            "users":json.loads(data["users"])
        }
        # return userData
        checkData = SelectSessionid(self.db,userData) 
        if(len(checkData) == 0):
            addSession = InsertIntoSession(self.db,userData)
            # return addPoll
            if(addSession["Inserted Row"] != 0):
            # keyValue = addKeyValue(self.db,userData)
                sessionData = SelectSessionid(self.db,userData) 
                print(len(sessionData))
                if(len(sessionData) != 0):
                    addData = InsertSpeaker(self.db,userData,sessionData[0]["session_id"]),

                    addData1=InsertUser(self.db,userData,sessionData[0]["session_id"])
                
                    return {
                        "data":{"session":addSession["Inserted Row"],"speakers":addData[0]["Inserted Row"],"users":addData1["Inserted Row"]} 
                        }

                else:
                    return {
                    "data":[],
                    "Error_msg":"speaker and user is not inserted"
                    }


            else:
                return {
                    "data":[],
                    "Error_msg":"session is not inserted"
                    }
        else:
            return {
                "data":[],
                "Error_msg":"session is already existed"
                }



def InsertIntoSession(db,userData):
    query = "INSERT INTO session(session_topic,session_desc,start_time,end_time,location,event_id,concepts) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    values = (str(userData["session_topic"]),str(userData["session_desc"]),str(userData["start_time"]),str(userData["end_time"]),str(userData["location"]),str(userData["event_id"]),str([]))
    queryData = QueryData(db)
    return queryData.insertAndUpdateQueryMethod(query, values)

def SelectSessionid(db,userData):
    query="SELECT session_id FROM session WHERE session_topic='{0}' AND start_time='{1}' AND location='{2}' ORDER BY session_id DESC LIMIT 1".format(str(userData["session_topic"]),str(userData["start_time"]),str(userData["location"]))
    queryData=QueryData(db)
    data=queryData.selectQueryMethod(query)
    return data
        
def addspeaker(userData,SESSIONID):
    value=[]
    for x in userData["speakers"]:
        value.append(
            (SESSIONID,x["id"],x["role"],userData["event_id"]) 
        ) 
    return value

def addUser(userData,SESSIONID):
    value1=[]
    for x in userData["users"]:
        value1.append(
            (SESSIONID,x)
        ) 
    return value1
    
def InsertSpeaker(db,userData,SESSIONID):
    '''query="SELECT id FROM attendee WHERE id={0}".format(str(userData["id"]))
    value = addspeaker(userData,SESSIONID)
    queryData = QueryData(db)
    data=queryData.selectQueryMethod(query)
    if(len(data))>0:'''
    
    query1 = "INSERT INTO speaker(session_id,speaker_id, role,event_id) VALUES(%s,%s, %s, %s )"
    value = addspeaker(userData,SESSIONID)
    queryData = QueryData(db)
    data=queryData.insertOrUpdateMany(query1, value)
    return data


def InsertUser(db,userData,SESSIONID):
    query2 = "INSERT INTO user_access(session_id,user_id) VALUES(%s, %s)"
    value1 = addUser(userData,SESSIONID)
    queryData = QueryData(db)
    data=queryData.insertOrUpdateMany(query2, value1)
    return data