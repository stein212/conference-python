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
        print(parse)
        for x in parse["tags"]:
            print(x)
            searchTags(x,parse,self.db)
        return setTag(parse["tags"],id,self.db)             
        
def searchTags(tag,parse,db):
    query = "SELECT * FROM attendee_tag WHERE tag_name = %s AND event_id = %s"
    cursor = db.cursor()
    val = (str(tag),str(parse["eventId"]))
    cursor.execute(query,val)
    item = cursor.fetchall()
    #print(item)
    if len(item) == 0 :
        query2 = "INSERT INTO attendee_tag (tag_name,event_id,count) VALUES (%s,%s,%s)"
        val2 = (str(tag),"1","1")
        cursor = db.cursor()
        cursor.execute(query2,val2)
        db.commit()
    else:
        if(len(item) == 1):
            nos = item[0][3]
            nos = nos+1
            query = "UPDATE attendee_tag SET count = '{0}' WHERE tag_id = '{1}'".format(str(nos),str(item[0][0]))
            cursor = db.cursor()
            cursor.execute(query)
            db.commit()
        else:
            for y in item:
                nos = y[3]
                nos = nos+1
                query = "UPDATE attendee_tag SET count = '{0}' WHERE tag_id = '{1}'".format(str(nos),str(y[0]))
                cursor = db.cursor()
                cursor.execute(query)
                db.commit() 

def setTag(tags,id,db):
    query2 = "UPDATE attendee SET attendee_tags = %s WHERE id = %s"
    val2 = (json.dumps(tags),id)
    print(val2)
    cursor = db.cursor()
    cursor.execute(query2,val2)
    db.commit()
    return checkTagUpdate(tags,id,db) 

def checkTagUpdate(tags,id,db):
    query = "SELECT * FROM attendee WHERE id = {0}".format(str(id))
    cursor = db.cursor()
    cursor.execute(query)
    item = cursor.fetchall()
    items = [ dict(zip([key[0] for key in cursor.description],row))for row in item ] 
    if(items[0]["attendee_tags"] == json.dumps(tags)):
        return {"msg":"Success"}
    else:
        return {"Error_msg":"Not updated"}      

