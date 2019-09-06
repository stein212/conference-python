from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json
from QueryData.QueryData import *
from datetime import datetime
from CommonVariables.commonvariables import *

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = baseDirectory+"profilePic/profPic"


def allowedExtension(fileName):
    return "." in fileName and fileName.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS

class NewEventdetails(Resource):
    def __init__(self,**kwargs):
        self.db=kwargs['data']

    def post(self):
        userData=request.form
        if 'file' not in request.files:
            return {"data":[{}]},203
            
        if len(checkEvent(self.db,userData)) != 0:
            return {"data":[],"Error_msg":"Event Already in the database"}
        
        

        # return userData
        #item="event_name","event_desc","venue_name","venue_address","event_start_date","event_end_date","registration_fee","concepts"
        query="INSERT INTO event_details(event_name,event_desc,venue_name,venue_address,event_start_date,event_end_date,registration_fee,concepts,current_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
        val=(str(userData["event_name"]),str(userData["event_description"]),str(userData["venue_name"]),str(userData["venue_address"]),str(userData["event_start_time"]),str(userData["event_end_time"]),str(0),str([]),str(1))
        '''cursor=self.db.cursor()
        cursor.execute(query,val)
        self.db.commit()'''
        print(val)
        queryData=QueryData(self.db)
        data = queryData.insertAndUpdateQueryMethod(query,val)
        if data["Inserted Row"] == 1:
            queryselect="SELECT event_id,event_name,event_start_date,event_end_date,current_status FROM event_details ORDER BY event_id DESC LIMIT 1 "
            cursor = self.db.cursor()
            cursor.execute(queryselect)
            item = cursor.fetchall()
            response=[]
            for x in item:
                data1={"event_id":x[0],"event_name":x[1],"event_start_date":x[2].strftime('%Y-%m-%d %H:%M:%S'),"event_end_date":x[3].strftime('%Y-%m-%d %H:%M:%S'),"current_status":x[4]}
                response.append(data1)
            if response!=0:
                return {"data":response}
            else:
                return {"data":[]},201
        else:
            return {"data":[]},202

def uploadImage(file):
    pass

def checkEvent(db,request):
    query = "SELECT event_id FROM event_details WHERE event_name= '{0}' AND venue_name='{1}' AND event_start_date='{2}' AND event_END_date='{3}'".format(
        str(request["event_name"]),
        str(request["venue_name"]),
        str(request["event_start_time"]),
        str(request["event_end_time"])
    )
    #AND venue_name={1} AND event_start_date = {2} AND event_end_data = {3}
    print(query)
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)

    return data



    
        
        
