from flask import Flask,request,jsonify
from flask_restful import Resource,Api,reqparse
import json
from QueryData.QueryData import *

class GetMapDataDetail(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def get(self,eventId):
        allMapData = getAllMapData(self.db,eventId)
        mapData = getMapData(self.db,eventId)
        # return jsonify(allMapData)
        parsedData = parseData(allMapData) 
        response = addMapData(parsedData,mapData)
        responseDataResponse = responseData(response)
        return responseDataResponse



def getAllMapData(db,eventId):
    query = "SELECT * FROM map_image WHERE event_id = {0}".format(str(eventId))
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data

def getMapData(db,eventId):
    query = "SELECT map_image.*,map_data.* FROM map_image JOIN map_data ON map_image.map_id=map_data.map_id WHERE map_image.event_id = {0}".format(str(eventId))
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data

def parseData(data):
    response = {}
    for x in data:
        date = x["date"].strftime("%Y-%m-%d")+"#"+str(x["map_id"] )
        if date not in response:
            x["date"] = x["date"].strftime("%Y-%m-%d")
            x["map_data"] = []
            response[date] = x
    return response

def addMapData(parsedData,mapData):
    for x in mapData:
        date = x["date"].strftime("%Y-%m-%d")+"#"+str(x["map_id"])
        if date in parsedData:
            
            parsedData[date]["map_data"].append(
                {
                    "map_data_id":x["map_data_id"],
                    "hall_number":x["hall_number"],
                    "description" :x["description"],
                    "title":x["title"]
                    
                }
            )
    return parsedData

def responseData(data):
    responseData = {}
    for x,y in data.items():
        date = x.split("#")[0]
        if date in responseData:
            responseData[date].append(y)
        else:
            responseData[date] = []
            responseData[date].append(y)
    return responseData




