from flask import Flask , request
from flask_restful import Resource, Api ,reqparse

class CheckRequest(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def post(self):
        parse = request.get_json(force=True)
        item = checkRequest(parse,self.db)
        return item
        

def checkRequest(parse,db):
    query = "SELECT * FROM connection_request WHERE request_from_attendee = {0} AND (request_to_attendee = {1})".format(parse["from"],parse["to"])
    print(query)
    cursor = db.cursor()
    cursor.execute(query)
    item = cursor.fetchall()
    result = [dict(zip([key[0] for key in cursor.description],row))for row in item]
    print(result)
    if len(result) > 0:
        return parseData(result,db)
    else:
        return []    

def parseData(result,db):
    try:
        del result[0]["accept_time"]
        #del result[0]["request_time"]
        result[0]["request_time"] = result[0]["request_time"].strftime("%Y-%m-%d %H:%M:%S")
        return result
    except:
        return []



    