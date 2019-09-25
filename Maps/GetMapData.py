from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import json

class DetailsOfMap(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def get(self,eventId):
        values = getMapData(eventId,self.db)
        return parse(dataAssigning(values))


def getMapData(eventId,db):
    query = "SELECT map_image.*,map_data.* FROM map_image INNER JOIN map_data ON map_image.map_id = map_data.map_id WHERE map_image.event_id = {0}".format(str(eventId))
    cursor = db.cursor()
    cursor.execute(query)
    items = cursor.fetchall()
    data = [dict(zip((key[0] for key in cursor.description),row)) for row in items]
    return data



def dataAssigning(data):
    item = {}
    if len(data) > 0:
        for x in data:
            if x["map_id"] in item:
                item[x["map_id"]]["data"].append({"map_data_id":x["map_data_id"],"hall_number":x["hall_number"],"description":x["description"],"title":x["title"]})
            else:
                item[x["map_id"]] = {"map_id": x["map_id"],"event_id": x["event_id"],"map_image": x["map_image"],"map_title":x["map_title"],"date":x["date"].strftime("%Y-%m-%d"),"data":[{"map_data_id":x["map_data_id"],"hall_number":x["hall_number"],"description":x["description"],"title":x["title"]}]}
    return item

def parse(data):
    item = []
    for x,y in data.items():   
        item.append(y)
    return item


        