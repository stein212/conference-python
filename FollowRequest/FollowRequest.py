from flask import Flask , request
from flask_restful import Resource, Api ,reqparse

class FollowRequest(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def post(self,id):
        parse = request.get_json(force=True)
        itemTO = checkToUserExist(parse,self.db)
        if len(itemTO) > 0:
            itemFrom = checkFromUserExist(parse,self.db)
            if len(itemFrom) > 0:
                check = checkAvailability(parse,self.db)
                if len(check) > 0:
                    return cancelRequest(parse,self.db)  # To call the cancel request .
                else:
                    return setRequest(parse,self.db)   # TO set request
            else:
                return {"Error_msg":"Attendee From Not Found"}
        else:
            return {"Error_msg":"Attendee Not Found"}

def checkToUserExist(parse,db):
    query = "SELECT * FROM attendee WHERE id = '{0}'".format(str(parse["to"]))
    cursor = db.cursor()
    cursor.execute(query)
    item = cursor.fetchall()
    return item

def checkFromUserExist(parse,db):
    query = "SELECT * FROM attendee WHERE id = '{0}'".format(str(parse["from"]))
    cursor = db.cursor()
    cursor.execute(query)
    item = cursor.fetchall()
    return item 

def checkAvailability(parse,db):
    query = "SELECT * FROM connection_request WHERE request_from_attendee = {0} AND request_to_attendee = {1}".format(str(parse["from"]),str(parse["to"]))
    cursor = db.cursor()
    cursor.execute(query)
    item = cursor.fetchall()
    return item

def setRequest(parse,db):
    query = "INSERT INTO connection_request (request_from_attendee,request_to_attendee,request_time,event_id,status) VALUES (%s,%s,%s,%s,%s)"
    val = (str(parse["from"]),str(parse["to"]),str(parse["time"]),str(parse["eventId"]),"0")
    cursor = db.cursor()
    cursor.execute(query,val)
    db.commit()
    return {"msg":"Success"}

def cancelRequest(parse,db):
    query = "DELETE FROM connection_request WHERE request_from_attendee = {0} AND request_to_attendee = {1}".format(str(parse["from"]),str(parse["to"]))
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    return {"msg":"Removed"}


