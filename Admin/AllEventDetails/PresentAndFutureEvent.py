from flask import Flask , request ,jsonify
from flask_restful import Api , Resource , reqparse
import json
from QueryData.QueryData import *

class PresentFutureDetailsOfEvent(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def get(self):
        

        query1="SELECT event_id,event_name,event_end_date,event_start_date,current_status FROM event_details WHERE current_status=2"
        query2="SELECT event_id,event_name,event_end_date,event_start_date,current_status FROM event_details WHERE current_status=1"
        #queryData=QueryData(self.db)
        #data=queryData.selectQueryMethod(query1)
        #data1=queryData.selectQueryMethod(query2)
        cursor = self.db.cursor()
        cursor.execute(query1)
        item = cursor.fetchall()
        response=[]
        for x in item:
            data1={"event_id":x[0],"event_name":x[1],"event_end_date":x[2].strftime('%Y-%m-%d %H:%M:%S'),"event_start_date":x[3].strftime('%Y-%m-%d %H:%M:%S'),"current_status":x[4]}
            response.append(data1)
        
        cursor = self.db.cursor()
        cursor.execute(query2)
        item1 = cursor.fetchall()
        response1=[]
        for x in item1:
            data2={"event_id":x[0],"event_name":x[1],"event_end_date":x[2].strftime('%Y-%m-%d %H:%M:%S'),"event_start_date":x[3].strftime('%Y-%m-%d %H:%M:%S'),"current_status":x[4]}
            response1.append(data2)
        return {"present":response,"Future":response1}



