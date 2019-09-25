from flask import Flask,request,jsonify
from flask_restful import Resource,Api,reqparse
import json
from QueryData.QueryData import *

class GetMapDataByDate(Resource):

    def __init__(self,**kwargs): 
        self.db = kwargs['data'] 
    
    def get(self,mapid):
        mapid=mapid
        #query="SELECT session.*,speaker.role,speaker.speaker_id,attendee.id,attendee.attendee_name,attendee.attendee_email,attendee.attendee_contact_num,attendee.id,attendee.prof_img FROM session JOIN speaker ON session.session_id=speaker.session_id JOIN attendee on speaker.speaker_id=attendee.id WHERE session.session_id={0}".format(str(sessionid))
        #query="SELECT map_image.map_id,map_image.event_id,map_image.map_image,map_image.map_title,map_image.date,map_data.map_data_id,map_data.hall_number,map_data.description,map_data.title FROM map_image JOIN map_data ON map_image.map_id=map_data.map_id WHERE map_image.map_id={0}".format(str(mapid))
        query="SELECT map_image.*,map_data.map_data_id,map_data.hall_number,map_data.description,map_data.title FROM map_image JOIN map_data ON map_image.map_id=map_data.map_id WHERE map_image.map_id={0}".format(str(mapid))
        
        queryData=QueryData(self.db)
        data=queryData.selectQueryMethod(query)
        #return {data[0]["date"]:data}
        
        if len(data) != 0:
            return {data[0]["date"]:[parseData(data)]}
        else:
            return []

def parseData(data):
    parsedData = {}
    for x in data:        
        parsedData["map_id"]=x["map_id"]
        parsedData["event_id"]=x["event_id"]
        parsedData["map_image"]=x["map_image"]
        parsedData["map_title"]=x["map_title"]
        parsedData["date"]=x["date"]
        try:
            if(len(parsedData["MapData"]) == 0 ):
                temp_val = {
                    "map_data_id":x["map_data_id"],
                    "hall_number":x["hall_number"],
                    "description" :x["description"],
                    "title":x["title"]
                    
                }
                parsedData["MapData"].append(temp_val)
            else:
                temp_val = {
                    "map_data_id":x["map_data_id"],
                    "hall_number":x["hall_number"],
                    "description" :x["description"],
                    "title":x["title"]
                }
                parsedData["MapData"].append(temp_val) 
        except:
            parsedData["MapData"] = []
            if(len(parsedData["MapData"]) == 0):
                parsedData["MapData"] = []
                temp_val = {
                    "map_data_id":x["map_data_id"],
                    "hall_number":x["hall_number"],
                    "description" :x["description"],
                    "title":x["title"]
                    
                }
                parsedData["MapData"].append(temp_val)
    return parsedData