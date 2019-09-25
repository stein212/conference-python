from flask import Flask, request,jsonify
from flask_restful import Resource, Api, reqparse
import json
import pymysql as mysql
from flask_httpauth import HTTPBasicAuth
from CommonVariables.commonvariables import *
from QueryData.QueryData import *
import os
from flask import Flask, request, redirect, url_for , send_file 
from werkzeug.utils import secure_filename


class UpdateMapTitle(Resource):
    def __init__(self,**kwargs):
        self.db=kwargs['data']
    
    def post(self):
        userData=request.get_json(force=True) 
        
        if (len(checkMapidExists(userData,self.db))>0):
            updateData =  updateMaptitle(userData,self.db)
            if(updateData["update"] > 0):
                return {"data":[{"update":1}]}
            else:
                return {"data":[],"Error_msg":"Error in updating data.Please try again."}
        else:
            return {"data":[],"Error_msg":"Map cannot be found,Please try again."}
        
def checkMapidExists(userData,db):
    query="SELECT map_id FROM map_image WHERE map_id={0}".format(userData["map_id"])
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)     
    return data   
            
def updateMaptitle(userData,db):
    
    query1 = "UPDATE map_image SET map_title = '{0}',date = '{1}' WHERE map_id = {2}".format(str(userData["title"]),str(userData["date"]), str(userData["map_id"]))        
    value = ()
    cursor = db.cursor()  
    data1=cursor.execute(query1,value) 
    db.commit()
        # queryData = QueryData(db)
        # data1=queryData.insertAndUpdateQueryMethod(query1,value)
    print (data1)
    return {"update":data1}