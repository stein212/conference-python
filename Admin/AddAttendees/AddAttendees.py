from flask import Flask , request , jsonify
from flask_restful import Resource , Api
from validate_email import validate_email
from QueryData.QueryData import *
import csv
import io
import random as rnd

class AddAttendees(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def post(self,eventId):
        f = request.files['file1']
        stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)

        file_csv = csv.DictReader(stream)  #open("/Users/apple/Azure/Test1/Admin/AddAttendees/data.csv")

        data = []
        dataJsonList = []
        for x in file_csv:
            password = rnd.randint(10000,100000)
            singleData = dict(x)
            splitEmail = str(singleData["Email"]).split('@')
            singleData['password'] = splitEmail[0]+str(password)
            dataJsonList.append(singleData)
            data.append((str(singleData["Name"]),str(singleData["Email"]),str(singleData["PhoneNumber"]),str(singleData["password"]),str(eventId)))
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
