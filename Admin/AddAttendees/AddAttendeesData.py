from flask import Flask,request,jsonify
from flask_restful import Resource,Api,reqparse
import json
from QueryData.QueryData import *
import random as rnd

class AddAttendeeData(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def post(self,eventId):
        userData = request.get_json(force=True)
        data = []
        dataJsonList = []
        for x in userData:
            password = rnd.randint(10000,100000)
            singleData = x
            splitEmail = str(singleData["email"]).split('@')
            singleData['password'] = splitEmail[0]+str(password)
            dataJsonList.append(singleData)
            if(len(checkAttendeeExist(self.db,singleData["email"],eventId)) == 0):
                data.append((str(singleData["name"]),str(singleData["email"]),str(singleData["phone_number"]),str(singleData["password"]),str(eventId)))
        insertDataResponse = insertData(self.db,data)

        if insertDataResponse["Inserted Row"] == len(data):
            return {"msg":"Successfully inserted {0}".format(str(len(data)))} 
            
        else:
            return {"msg":"Successfully inserted {0} of {1}".format(str(insertDataResponse["Inserted Row"]),str(len(data)))} 
        
        # isEmail = validate_email(email,check_mx=True)
        # return isEmail
def insertData(db,data):
    query = "INSERT INTO attendee (attendee_name,attendee_email,attendee_contact_num,attendee_password,event_id) VALUES (%s,%s,%s,%s,%s)"
    cursor = db.cursor()
    cursor.executemany(query,data)
    db.commit()
    cursor.close()
    return { "Inserted Row": cursor.rowcount } 

def checkAttendeeExist(db,data,eventId):
    query = "SELECT id FROM attendee WHERE attendee_email = '{0}' AND event_id={1}".format(str(data),str(eventId)) 
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data 


