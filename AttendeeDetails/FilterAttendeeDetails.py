from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import json
import pymysql as mysql
import datetime
from flask_httpauth import HTTPBasicAuth

class FilteredAttendeeDetails(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']
    
    def get(self,id):
        item = getData(id,self.db)
        if(len(item) > 0):
            return item[0] , 200 
        else:
            return {} , 202    

def getData(attendeeId,DB):
    query = "SELECT * FROM attendee WHERE id = {0}".format(str(attendeeId))  
    cursor = DB.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    item = [dict(zip([key[0] for key in cursor.description],row))for row in results] 

    if(len(item) > 0):
        del item[0]["attendee_password"]
        tagData = item[0]["attendee_tags"]
        if tagData == None:
            jsonData = []
        else:
            jsonData = json.loads(tagData) 
        item[0]["attendee_tags"] = jsonData
        return item

    else:
        return [] 
