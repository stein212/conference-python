from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import json
import pymysql as mysql
import datetime

#mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")

class SpeakerDetails(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']
        #mysql_connection = self.data
        
    def get(self,speakerId):
        item = getData(speakerId,self.data)
        if len(item) == 0 :
            return {} , 202
        del item[0]["attendee_password"]
        return item[0]


def getData(speakerId,DB):
    query = "SELECT speaker.*,attendee.* FROM speaker INNER JOIN attendee ON speaker.speaker_id = attendee.id WHERE speaker.speaker_id={0}".format(str(speakerId))
    cursor = DB.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    item = [dict(zip([key[0] for key in cursor.description],row))for row in result] 
    return item 
