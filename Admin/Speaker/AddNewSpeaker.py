from flask import Flask, request , jsonify
from flask_restful import Api, Resource, reqparse
import json
from QueryData.QueryData import *
import random
        

class AddNewSpeaker(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def post(self):
        requestedData = request.get_json(force=True)
        
        if(1 != 1):
            return response([]) 
        else:
            if "attendeeId" in requestedData:
                attendee = checkAttendeeCountById(self.db,requestedData["attendeeId"])
                
                if (len(attendee) > 0):
                    checkSpeaker = checkSpeakerByIdAndSession(self.db,requestedData["attendeeId"],requestedData["sessionId"])
                    print(checkSpeaker)
                    if(len(checkSpeaker)):
                        return {"data":[]},203
                    insert = insertSpeakers(self.db,attendee[0]["id"],requestedData["role"],requestedData["sessionId"],requestedData["event_id"])
                    if(insert["Inserted Row"] > 0):
                        return response([])
                else:
                    return {"data":[]},202
            else:
                # check = checkAttendees(self.db,requestedData["email"])
                # print(check)
                if(1 > 0):
                    data = insertAttendee(self.db,requestedData["event_id"],requestedData["name"],requestedData["email"])
                    if(data["Inserted Row"] > 0):
                        id = checkAttendeeCountByEmail(self.db,requestedData["email"],requestedData["name"])[0]["id"]
                        insert = insertSpeakers(self.db,id,requestedData["role"],requestedData["sessionId"],requestedData["event_id"])
                        if(insert["Inserted Row"] > 0):
                            return response([])
                        else:
                            return response([]),203
                    else:
                        return response([]),403                               
        

def checkAttendees(db,email):
    query = "SELECT id,attendee_name,attendee_email,attendee_contact_num FROM attendee WHERE attendee_email = {0}".format(str(email))
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data

def checkAttendeeCountById(db,attendee_id):
    query = "SELECT id FROM attendee WHERE id = {0}".format(str(attendee_id))
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data

def checkAttendeeCountByEmail(db,email,name):
    query = "SELECT * FROM attendee WHERE attendee_email = '{0}' AND attendee_name = '{1}'".format(str(email),str(name))
    print(query)
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    print("Attendee count")
    print(data)
    return data

def insertSpeakers(db,attendeeId,role,sessionId,eventId):
    query = "INSERT INTO speaker (speaker_id,role,session_id,event_id) VALUES (%s,%s,%s,%s)"
    val = (attendeeId,role,sessionId,eventId)
    queryData = QueryData(db)
    data = queryData.insertAndUpdateQueryMethod(query,val)
    return data

def insertAttendee(db,eventId,name,email):
    password = random.randint(10000,99999)
    query = "INSERT INTO attendee (attendee_name,attendee_email,attendee_password,event_id) VALUES (%s,%s,%s,%s)"
    val = (name,email,password,eventId)
    queryData = QueryData(db)
    data = queryData.insertAndUpdateQueryMethod(query,val)
    return data

def checkSpeakerByIdAndSession(db,attendeeId,sessionId):
    query = "SELECT role FROM speaker WHERE speaker_id = {0} AND session_id = {1}".format(str(attendeeId),str(sessionId))
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data


def response(data):
    if(len(data) > 0):
        return {"data":data}
    else:
        return {"data":[]} 

