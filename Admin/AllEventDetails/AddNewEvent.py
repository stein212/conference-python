from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json
from QueryData.QueryData import *

class NewEventdetails(Resource):
    def __init__(self,**kwargs):
        self.db=kwargs['data']

    def post(self):
        userData=request.get_json(force=True)
        #item="event_name","event_desc","venue_name","venue_address","event_start_date","event_end_date","registration_fee","concepts"
        query="INSERT INTO event_details(event_name,event_desc,venue_name,venue_address,event_start_date,event_end_date,registration_fee,concepts,current_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
        val=(str(userData["event_name"]),str(userData["event_desc"]),str(userData["venue_name"]),str(userData["venue_address"]),str(userData["event_start_date"]),str(userData["event_end_date"]),str(userData["registration_fee"]),str(userData["concepts"]),str(userData["current_status"]))
        '''cursor=self.db.cursor()
        cursor.execute(query,val)
        self.db.commit()'''
        queryData=QueryData(self.db)
        data = queryData.insertAndUpdateQueryMethod(query,val)
        
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
                return {"data":[]}
    
        
        
