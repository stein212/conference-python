from flask import Flask , request
from flask_restful import Api,Resource
import json
from QueryData.QueryData import *

class PollAnswer(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def get(self):
        requestData = request.get_json(force=True)

        data = checkPollAvailability(self.db,requestData)
        if(len(data) == 0):
            return {"Error_msg":"Poll is not available in Database"}
        elif pollErrorResponse(data)["Error_msg"] == "You cannot give ratings ,because the poll is already over":
            return pollErrorResponse(data),205


        if requestData["from"] == "attendee":
            checkAttendeeIdInAttendeeTableResponse = checkAttendeeIdInAttendeeTable(self.db,requestData)
            if len(checkAttendeeIdInAttendeeTableResponse) >0:
                checkRatedResponse = checkRatedAlready(self.db,requestData)
                if len(checkRatedResponse) > 0:
                    return {"Error_msg":"You have already given ratings"},202
                return insertPollAnswer(self.db,requestData,'attendee') 
            return {"Error_msg":"Attendee is not available"},203


        elif requestData["from"] == "speaker":
            checkSpeakerIdInSpeakerTableResponse = checkSpeakerIdInSpeakerTable(self.db,requestData)
            if len(checkSpeakerIdInSpeakerTableResponse) > 0 :
                checkRatedResponse = checkRatedAlready(self.db,requestData)
                if len(checkRatedResponse) > 0:
                    return {"Error_msg":"You have already given ratings"},202
                return insertPollAnswer(self.db,requestData,'speaker')
            return {"Error_msg":"Attendee is not available"},203



        elif requestData["from"] == "user":
            checkUserIdInUserTableResponse = checkUserIdInUserTable(self.db,requestData)
            if len(checkUserIdInUserTableResponse) > 0:
                checkRatedResponse = checkRatedAlready(self.db,requestData)
                if len(checkRatedResponse) > 0:
                    return {"Error_msg":"You have already given ratings"},202
                return insertPollAnswer(self.db,requestData,'user') 
            return {"Error_msg":"Attendee is not available"},203
        
        else:
            return {"Error_msg":"Need data to insert"},205
            

        

def checkAttendeeIdInAttendeeTable(db,data):
    query = "SELECT * FROM attendee WHERE id = {0}".format(str(data["attendee_id"])) 
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data

def checkSpeakerIdInSpeakerTable(db,data):
    query = "SELECT * FROM speaker WHERE speaker_id = {0}".format(str(data["attendee_id"]))
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data

def checkUserIdInUserTable(db,data):
    query = "SELECT * FROM users WHERE user_id = {0}".format(str(data["user_id"]))
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data

def insertPollAnswer(db,data,role):
    query = "INSERT INTO poll_answer (poll_id,attendee_id,poll_answer,role) VALUES (%s,%s,%s,%s)"
    val = (str(data["poll_id"]),str(data["attendee_id"]),str(data["poll_answer"]),str(role))
    cursor = db.cursor()
    cursor.execute(query,val)
    db.commit()
    count = cursor.rowcount
    cursor.close()
    return {"Inserted Row":count}

def checkRatedAlready(db,data):
    query = "SELECT * FROM poll_answer WHERE poll_id = {0} AND attendee_id = {1}".format(str(data["poll_id"]),str(data["attendee_id"]))
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data

def checkPollAvailability(db,data):
    query = "SELECT * FROM poll WHERE poll_id = {0}".format(str(data["poll_id"])) 
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data

def pollErrorResponse(data):
    if data[0]["poll_status"] == 0:
        return {"Error_msg":"You cannot give ratings ,because the poll is already over"}
    else:
        return {"Error_msg":0}
