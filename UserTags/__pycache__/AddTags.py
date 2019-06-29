from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import json
import pymysql as mysql
import datetime


class AddTags(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs["data"]

    def post(self,id):
        parse = request.get_json(force = True)
        for x in parse["tags"]:
            searchTags(x,self.db)
        
def searchTags(tag,db):
    query = "SELECT * FROM attendee_tag WHERE tag_name = %s"
    cursor = db.cursor()
    val = (str(tag))
    cursor.execute(query,val)
    item = cursor.fetchall()
    if len(item) == 0 :
        query2 = "INSERT INTO attendee_tag (tag_name,event_id,count) VALUES (%s,%s,%s)"
        val2 = (str(tag),"1","1")
        cursor = db.cursor()
        cursor.execute(query2,val2)
        db.commit()

def setTag(tags,id,db):
    query2 = "UPDATE attendee SET attendee_tags = %s WHERE id = %s"
    val2 = (str(tags),id)
    cursor = db.cursor()
    cursor.execute(query2,val2)
    db.commit()


