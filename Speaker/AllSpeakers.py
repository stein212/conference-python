from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import json
import pymysql as mysql
import datetime


class GetAllSpeakers(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs["data"]

    def get(self,id):
        data = getSpeakers(id,self.db)
        if len(filterResponse(data)) == 0 :
            return [],202
        return filterResponse(data),200


def getSpeakers(eventId,db):
    query = "SELECT speaker.* , attendee.* FROM speaker INNER JOIN attendee ON attendee.id = speaker.speaker_id WHERE speaker.event_id = {0}".format(str(eventId))
    cursor = db.cursor()
    cursor.execute(query)
    items = cursor.fetchall()
    #print(items)
    return items

def filterResponse(data):
    response = {}
    for x in data:
        item = {"speaker_name":x[8],"image":x[23]}
        response[x[0]] = item
    return sortResponse(response)

def sortResponse(data):
    response = []
    for x in data.values():
        response.append(x)
    return response    



