from flask import Flask , request , jsonify
from flask_restful import Resource, Api ,reqparse
import json
import pymysql as mysql
import datetime
from flask_httpauth import HTTPBasicAuth

class GetMapData2(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']
    def get(self,eventId):
        data = getMapData(eventId,self.data)
        resp = DataResponse(data)
        response = resp.phrase()
        if len(response) > 0:
            return response , 200
        else:
            return response , 201    
        
def getMapData(eventId,db):
    query = "SELECT map_image.*,map_data.* FROM map_image INNER JOIN map_data ON map_image.map_id = map_data.map_id WHERE map_image.event_id = {0}".format(str(eventId))
    cursor = db.cursor() 
    cursor.execute(query)
    result = cursor.fetchall() 
    items = [dict(zip([key[0] for key in cursor.description], row)) for row in result] 
    return items   


class DataResponse:
    def __init__(self,data):
        self.data = data

    def phrase(self):
        response = {}
        for x in self.data:
            key = x['date'].strftime("%Y-%m-%d") 
            response[key] = {}    
            
            if (x['date'] in response[key]):
                MapData = {"map_data_id":x["map_data_id"],"hall_number":x["hall_number"],"description":x["description"],"title":x["title"]}
                response[key][x['date']]["MapData"].append(MapData) 

            else:
                setData = {}
                setData["map_id"] = x["map_id"]
                setData["event_id"] = x["event_id"]
                setData["map_image"] = x["map_image"]
                setData["map_title"] = x["map_title"] 
                setData["date"] = x["date"].strftime("%Y-%m-%d") 
                setData["MapData"] = [{"map_data_id":x["map_data_id"],"hall_number":x["hall_number"],"description":x["description"],"title":x["title"]}]
                response[key] = [setData]
        return response