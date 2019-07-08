from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import json

class DeleteUsers(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs["data"]
    def post(self):
        parse = request.get_json(force=True)
        if(parse["password"]) == "3Edge@gmail.com":
            deleteUser(parse,self.db)
            return {"msg":"Success"}
        else:
            return {"Error_msg":"UnAuthorized user"}

def deleteUser(parse,db):
    query = "DELETE FROM attendee WHERE id = {0}".format(parse["id"])
    
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()