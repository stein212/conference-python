from flask import Flask, request , jsonify
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource, reqparse
import json
from QueryData.QueryData import *

class AddUsers(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data'] 

    def post(self):
        userData = request.get_json(force=True)
        userExistRes = userExist(self.db,userData)
        if len(userExistRes) > 0 :
            checkUserAccessReq = checkUserAccess(self.db,userData)
            if(len(checkUserAccessReq) == 0 ):
                insertUsersReq = insertUsers(self.db,userData)
                return {
                "data":[insertUsersReq]
                }
            else:
                return {
                "data":[],
                "Error_msg":"The Moderator already exist ."
            }
        else:
            return {
                "data":[],
                "Error_msg":"The Credientials are not correct."
            }


def userExist(db,userData):
    query = "SELECT user_id FROM users WHERE user_id = {0}".format(str(userData["user_id"])) 
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data

def insertUsers(db,userData):
    query = "INSERT INTO user_access(user_id,session_id) VALUES(%s,%s)"
    value = (str(userData["user_id"]),str(userData["session_id"]))
    queryData = QueryData(db)
    data = queryData.insertAndUpdateQueryMethod(query,value)
    return data  

def checkUserAccess(db,userData):
    query = "SELECT user_id FROM user_access WHERE user_id={0} AND session_id={1}".format(str(userData["user_id"]),str(userData["session_id"]))
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query) 
    return data