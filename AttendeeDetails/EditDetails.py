from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import json

class EditAttendeeInfo(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def post(self):

        try:
            parse = request.get_json(force=True)
            header = request.authorization
            nameOfColumn = parse["colName"]
            dataOfColumn = parse["data"]
            
            return getAccess(header,parse,self.db)

        except:
            parse = request.get_json(force=True)
            header = request.authorization
            print(parse)
            print(header)
            return {"Error_msg":"Error need every details"}   

def getAccess(header,parse,db):
    # return {"header":header,"body":parse} .
    query = "SELECT * FROM attendee WHERE id = '{0}' AND attendee_contact_num = '{1}'".format(str(header.username),str(header.password))
    cursor = db.cursor()
    cursor.execute(query)
    item = cursor.fetchall()
    if len(item) > 0 :
        #return updateData(header,parse,db)
        return updateData(header,parse,db)
    else:
        return {"Error_msg":"Unable to find the user"}    
     

def updateData(header,parse,db):
    #return {"h":header,"parse":parse}
    query = "UPDATE attendee SET "+parse["colName"]+" = '{0}' WHERE id = {1}".format(parse["data"],header["username"])
    val = (str(parse["data"]),header.username)
    cursor = db.cursor()
    cursor.execute(query) 
    db.commit()
    item = checkUpdate(header,parse,db)
    if len(item) == 0:
        return {"Error_msg":"Value set but not Updated"}
    else:
        if item[0][parse["colName"]] == parse["data"]:
            return {"msg":"Successfully Updated"}
        else:
            return {"Error_msg":"Error in updating Information"}   

def checkUpdate(header,parse,db):
    # return {"header":header,"body":parse} .
    query = "SELECT * FROM attendee WHERE id = '{0}' AND attendee_contact_num = '{1}'".format(header["username"],header["password"])
    cursor = db.cursor()
    cursor.execute(query)
    item = cursor.fetchall()
    print(item)
    mapItem = [dict(zip([key[0] for key in cursor.description],row))for row in item]
    print(mapItem)
    if len(mapItem) > 0:
        return mapItem
    else:
        return []




        