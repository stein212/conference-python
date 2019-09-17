from flask import Flask, request,jsonify
from flask_restful import Resource, Api, reqparse
import json
from QueryData.QueryData import *

class Attendance(Resource):
    def __init__(self,**kwargs):
        self.db=kwargs['data']
    
    def post(self):
        userData=request.get_json(force=True)
        
        if  (len(checkEventidExists(self.db,userData))!=0):
            if  (len(checkAttendeeidExists(self.db,userData))!=0):
                if  (len(checkEventAndAttendeeidExists(self.db,userData))==0):
                    if InsertIntoAttendeeAttendance(self.db,userData)["Inserted Row"]== 1:
                        return {"data":[{"Inserted Row":1}],"msg":"Success , your attendance is registered."}
                    else:
                        return {"data":[],"msg":"Attendance is not registered."}  
                else:
                    return{"data":[],"msg":"You have already placed attendance to this event ."} 
            else:
                return{"data":[],"msg":"Credientials used is not available , Please contact the admin."} 
        else:
            return{"data":[],"msg":"Credientials ( Event Details )used is not available , Please contact the admin."} 

def checkAttendeeidExists(db,userData):
    query = "SELECT id FROM attendee WHERE id = {0}".format(userData["attendee_id"])
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data
def checkEventidExists(db,userData):
    query = "SELECT event_id FROM event_details WHERE event_id = {0}".format(userData["event_id"])
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data
def checkEventAndAttendeeidExists(db,userData):
    query = "SELECT attendee_id ,event_id FROM attendee_attendance WHERE attendee_id = '{0}' AND event_id='{1}' AND date = '{2}'".format(userData["attendee_id"],userData["event_id"],userData["date"])
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data


def InsertIntoAttendeeAttendance(db,userData):
    query = "INSERT INTO attendee_attendance(date,event_id,attendee_id) VALUES(%s,%s,%s)"
    values = (str(userData["date"]),str(userData["event_id"]),str(userData["attendee_id"]))
    queryData = QueryData(db)
    data=queryData.insertAndUpdateQueryMethod(query, values)
    return data


