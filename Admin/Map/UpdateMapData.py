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


class Mapdataupdate(Resource):
    def __init__(self,**kwargs):
        self.db=kwargs['data']
    
    def post(self):
        userData=request.get_json(force=True)  
        print(userData)
        # return userData
        if (len(checkMapdataidExists(userData,self.db))>0):
            updateData =  updateMapdata(userData,self.db)
            if(updateData["update"] > -1):
                return {"data":[{"update":updateData["update"]}]}
            else:
                return {"data":[],"Error_msg":"Error in updating data.Please try again."} 
        else:
            return {"data":[],"Error_msg":"Map Data credientials is not available."} 
        
def checkMapdataidExists(userData,db):
    query="SELECT map_data_id FROM map_data WHERE map_data_id={0}".format(userData["map_data_id"]) 
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)     
    return data   
            
def updateMapdata(userData,db):
    
    query1 = "UPDATE map_data SET title = '{0}',hall_number = '{1}',description = '{2}' WHERE map_data_id = {3}".format(str(userData["title"]),str(userData["point"]),str(userData["desc"]),str(userData["map_data_id"]))  
    print(query1)      
    value = ()
    # cursor = db.cursor()  
    # data1=cursor.execute(query1,value) 
    # db.commit()
    queryData = QueryData(db)
    data1=queryData.insertAndUpdateQueryMethod(query1,value)
    print (data1)
    return {"update":data1["Inserted Row"]} 