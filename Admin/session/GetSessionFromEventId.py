from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json
from QueryData.QueryData import *

class GetSessionFromEventId(Resource):
    def __init__(self,**kwargs):
        self.db=kwargs['data']
    
    def get(self,eventId):
        
        query="SELECT session_id,session_topic,start_time From session WHERE event_id={0}".format(str(eventId)) 
        '''queryData = QueryData(self.db)
        data=queryData.selectQueryMethod(query)'''
        cursor = self.db.cursor()
        cursor.execute(query)
        item = cursor.fetchall() 
        response=[]
        for x in item:
            data1={"session_id":x[0],"session_topic":x[1],"start_time":x[2].strftime('%Y-%m-%d %H:%M:%S')}
            response.append(data1)
        return response
 
    