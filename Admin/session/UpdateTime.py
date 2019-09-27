from flask import Flask, request , jsonify
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource, reqparse
import json
from QueryData.QueryData import *

class UpdateSessionTime(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['data']

    def post(self):
        userData = request.get_json(force=True)
        # return userData
        if (len(checkSessionidExists(userData,self.db))>0):
            return {
                "data":[UpdateSession(userData,self.db)],
                "Error_msg":"Please try again after sometime."
            }
        else:
            return {
                "data":[],
                "Error_msg":"Please try again after sometime."
            } 
        
      
def checkSessionidExists(userData,db):
    query="SELECT session_id FROM session WHERE session_id={0}".format(userData["session_id"])
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)     
    return data  
def UpdateSession(userData,db):
    query1 = "UPDATE session SET {0} = '{1}' WHERE session_id = {2}".format(
        str(userData["col_name"]),
        str(userData["value"]),
        str(userData["session_id"])         
    )        
    value = ()
    cursor = db.cursor()  
    data1=cursor.execute(query1,value) 
    db.commit()
    print (data1)
    return {"UpdatedRow":data1}