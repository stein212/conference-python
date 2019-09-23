from flask import Flask, request,jsonify
from flask_restful import Resource, Api, reqparse
import json
from QueryData.QueryData import *
import os
from flask import Flask, request, redirect, url_for , send_file 
from werkzeug.utils import secure_filename
import pymysql as mysql
from flask_httpauth import HTTPBasicAuth
from CommonVariables.commonvariables import *


UPLOAD_FOLDER = baseDirectory+"Maps/mapimages"

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowedExtension(fileName):
    return "." in fileName and fileName.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS


class AddSession2(Resource):
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
            "speakers":data["speakers"],
            "users":data["users"]
        }
    
        
        if(len(SelectSessionid(self.db,userData)) == 0):
            if 'file' not in request.files:
                return {"Error_msg":"Image is not available..Choose a image."}
            else:
                file = request.files["file"]
                if 1==1:
                    if file and allowedExtension(file.filename):
                        fileName = secure_filename(file.filename) 
                        file.save(os.path.join(UPLOAD_FOLDER,fileName))
                        data = InsertIntoSession(userData,fileName,self.db) 
                        print(data)
                        sessionData = SelectSessionid(self.db,userData) 
                        print(len(sessionData))
                        if(len(sessionData) != 0):
                            addSpeaker = InsertSpeaker(self.db,userData,sessionData[0]["session_id"],sessionData[0]["event_id"])
                            addUser=InsertUser(self.db,userData,sessionData[0]["session_id"]) 
                            return {
                                "data": {"session":data["Inserted Row"],"speakers":addSpeaker["Inserted Row"],"users":addUser["Inserted Row"]}
                                }
                        else:
                            return {
                            "data":[],
                            "Error_msg":"speaker and user is not inserted"
                            }
                        
                    else:
                        return "image is not uploaded"
                else:
                        return "image is not uploaded 1"



               
            
        else:
            return {
                "data":[],
                "Error_msg":"session is already existed"
                }



def InsertIntoSession(userData,name,db):
    query = "INSERT INTO session(session_topic,session_desc,start_time,end_time,location,event_id,session_image) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    values = (str(userData["session_topic"]),str(userData["session_desc"]),str(userData["start_time"]),str(userData["end_time"]),str(userData["location"]),str(userData["event_id"]),name)
    print(values)
    cursor = db.cursor()  
    data=cursor.execute(query,values) 
    db.commit()
    
    return {"Inserted Row":data}

def SelectSessionid(db,userData):
    query="SELECT session_id,event_id FROM session WHERE session_topic='{0}' AND start_time='{1}' AND location='{2}' ORDER BY session_id DESC LIMIT 1".format(str(userData["session_topic"]),str(userData["start_time"]),str(userData["location"]))
    queryData=QueryData(db)
    data=queryData.selectQueryMethod(query)
    return data

def addspeaker(userData,SESSIONID,EVENTID):
    value=[]
    for x in json.loads(userData["speakers"]):
        value.append(
            (SESSIONID,EVENTID,x["id"],x["role"]) 
        ) 
    print (value)
    return value

def addUser(userData,SESSIONID):
    value1=[]
    for x in json.loads(userData["users"]):
        value1.append(
            (SESSIONID,x)
        ) 
    print (value1)
    return (value1)
    
def InsertSpeaker(db,userData,SESSIONID,EVENTID):
    '''query="SELECT id FROM attendee WHERE id={0}".format(str(userData["id"]))
    value = addspeaker(userData,SESSIONID)
    queryData = QueryData(db)
    data=queryData.selectQueryMethod(query)
    if(len(data))>0:'''
    
    query1 = "INSERT INTO speaker(session_id,event_id,speaker_id,role) VALUES(%s,%s, %s, %s )"
    value = addspeaker(userData,SESSIONID,EVENTID)
    queryData = QueryData(db)
    data=queryData.insertOrUpdateMany(query1, value)
    print(data)
    return data


def InsertUser(db,userData,SESSIONID):
    
    query2 = "INSERT INTO user_access(session_id,user_id) VALUES(%s, %s)"
    value1 = addUser(userData,SESSIONID)
    queryData = QueryData(db)
    data=queryData.insertOrUpdateMany(query2, value1)
    print (data)
    return data