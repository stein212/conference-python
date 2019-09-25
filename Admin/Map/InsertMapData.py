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


class InsertPointData(Resource):
    def __init__(self,**kwargs):
        self.db=kwargs['data']
    
    def post(self):
        userData=request.get_json(force=True) 
        # return userData
        if (len(checkMapidExists(userData,self.db))>0):
            if (len(checkMapidExistsinmapdata(userData,self.db))==0):
                insertedRow = insertMapdata(userData,self.db)
                if(insertedRow["Inserted Row"] > 0):
                    return {"data":[
                        {
                            "inserted":insertedRow["Inserted Row"]
                        
                        }
                        ]}
                else:
                    return {"data":[],"Error_msg":"Data is not successfully added"} 
            else:
                return {"data":[],"Error_msg":"Data already exist"}
        else:
            return {"data":[],"Error_msg":"map_id is not existed"}
        
def checkMapidExists(userData,db):
    query="SELECT map_id FROM map_image WHERE map_id={0}".format(userData["map_id"])
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)     
    return data   

def checkMapidExistsinmapdata(userData,db):
    query="SELECT map_id FROM map_data WHERE map_id='{0}' AND hall_number='{1}' AND description='{2}' AND title='{3}'".format(userData["map_id"],userData["hall_number"],userData["description"],userData["title"])
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)     
    return data   

            
def insertMapdata(userData,db):
    
    query = "INSERT INTO map_data(map_id,hall_number,description,title) VALUES(%s,%s,%s,%s)"
    values = (str(userData["map_id"]),str(userData["hall_number"]),str(userData["description"]),str(userData["title"]))
    cursor = db.cursor()  
    data1=cursor.execute(query,values) 
    db.commit()
        # queryData = QueryData(db)
        # data1=queryData.insertAndUpdateQueryMethod(query1,value)
    print (data1)
    return {"Inserted Row":data1}
        