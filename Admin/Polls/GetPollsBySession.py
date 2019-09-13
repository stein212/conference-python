from flask import Flask,request
from flask_restful import Resource,Api,reqparse
import json
from QueryData.QueryData import *

class GetPollsBySession(Resource):
    def __init__(self,**kwargs): 
        self.db = kwargs['data'] 

    def get(self,session_id):
        
        query="SELECT poll.event_id,poll.poll_id,poll.poll_title,poll.poll_start_time,poll.poll_end_time,poll_values.name,poll_values.val FROM poll INNER JOIN poll_values ON poll.poll_id=poll_values.poll_id  WHERE session_id={0}".format(str(session_id))
        queryData=QueryData(self.db)
        data = queryData.selectQueryMethod(query)
        if len(data) != 0:
            return parseData(data)
        else:
            return []

def parseData(data):
    response = []
    parsedData = {}
    for x in data:      
        if x["poll_id"] not in parsedData:
            parsedData[x["poll_id"]] = {}  
            parsedData[x["poll_id"]]["event_id"]=x["event_id"]
            parsedData[x["poll_id"]]["poll_id"]=x["poll_id"]
            parsedData[x["poll_id"]]["poll_title"]=x["poll_title"]
            parsedData[x["poll_id"]]["poll_start_time"]=x["poll_start_time"].strftime("%Y-%m-%d %H:%M:%S")
            parsedData[x["poll_id"]]["poll_end_time"]="xx-xx-xx hh:mm:ss" if x["poll_end_time"] == None else x["poll_end_time"].strftime("%Y-%m-%d %H:%M:%S")
            parsedData[x["poll_id"]]["values"] = []
            parsedData[x["poll_id"]]["values"].append({
                x["name"]:x["val"]
            })
        else:
            parsedData[x["poll_id"]]["values"].append({
                x["name"]:x["val"]
            })

        
    for val in parsedData.values():
        response.append(val)
    return response
                    