from flask import Flask,request
from flask_restful import Resource,Api,reqparse
import json
from QueryData.QueryData import *

class SessionDetails(Resource):
    def __init__(self,**kwargs): 
        self.db = kwargs['data'] 
    def get(self,event_id):
        event_id=event_id
        query="SELECT * FROM session WHERE event_id={0}".format(str(event_id))
        queryData = QueryData(self.db)
        data = queryData.selectQueryMethod(query)
        response = []
        try:
            for x in data:
                x["start_time"] = x["start_time"].strftime('%Y-%m-%d %H:%M:%S')
                x["end_time"] = x["end_time"].strftime('%Y-%m-%d %H:%M:%S')
                response.append(x)
        except:
            response = [] 

        return response
            