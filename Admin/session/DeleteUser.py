from flask import Flask,request,jsonify
from flask_restful import Resource,Api,reqparse
import json
from QueryData.QueryData import *

class DeleteUser(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']
    
    def post(self):
        userData = request.get_json(force=True)
        deleteUserAccessReq = deleteUserAccess(self.db,userData)
        return {
            "data":[deleteUserAccessReq]
        }

def deleteUserAccess(db,userData):
    query = "DELETE FROM user_access WHERE user_access_id = {0}".format(str(userData["user_access_id"]))
    queryData = QueryData(db)
    data = queryData.insertAndUpdateQueryMethod(query,())
    return data