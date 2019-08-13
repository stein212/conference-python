from flask import Flask, request , jsonify
from flask_restful import Api, Resource, reqparse
import json
from QueryData.QueryData import *


class CurrentStatus(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['data']

    def post(self):
        requestedData = request.get_json(force=True)
        if(requestedData["force"] == 1):
            if requestedData["current_status"] == 0:
                setCurrentStatusAsZero(self.db)
                return responseOfService([]) 
            count = setCurrentStatusAsZero(self.db)["Inserted Row"]
            updateEventCurrentStatus(self.db,requestedData["event_id"],requestedData["current_status"])
            return responseOfService([])
        else:
            if len(checkCurrentStatus(self.db)) == 0:
                return "ok"


            
def setCurrentStatusAsZero(db):
    query = "UPDATE event_details SET current_status = 0"
    print(query)
    queryData = QueryData(db)
    data = queryData.insertAndUpdateQueryMethod(query,())
    print(data)
    return data

def updateEventCurrentStatus(db,event_id,currentState):
    query = "UPDATE event_details SET current_status = {0} WHERE event_id={1}".format(str(currentState),str(event_id))
    print(query)
    queryData = QueryData(db)
    data = queryData.insertAndUpdateQueryMethod(query,())
    return data

def checkCurrentStatus(db):
    query = "SELECT event_id,event_name,event_start_date,event_end_date,current_status FROM event_details WHERE current_status = 1"
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    print(".....")
    print(data)
    return parse(data)

def parse(data):
    print(data[0]["event_end_date"].strftime('%Y-%m-%d %H:%M:%S'))
    return [{
    "current_status": data[0]["current_status"],
    "event_end_date": data[0]["event_end_date"].strftime('%Y-%m-%d %H:%M:%S'),
    "event_id": data[0]["event_id"],
    "event_name": data[0]["event_name"],
    "event_start_date": data[0]["event_start_date"].strftime('%Y-%m-%d %H:%M:%S')
  }]
    # data["event_start_date"] = data[0]["event_start_date"].strftime('%Y-%m-%d %H:%M:%S')
    # data["event_end_date"] = data[0]["event_end_date"].strftime('%Y-%m-%d %H:%M:%S')
    
def responseOfService(data):
    if len(data) > 0:
        return {"data":data}
    else:
        return {"data":[]}