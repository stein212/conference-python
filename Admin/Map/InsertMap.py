from flask import Flask, request,jsonify
from flask_restful import Resource, Api, reqparse
import json
from QueryData.QueryData import *
import os
from flask import Flask, request, redirect, url_for , send_file 
from werkzeug.utils import secure_filename
import pymysql as mysql
from flask_httpauth import HTTPBasicAuth
from CommonVariables.commonvariables import *

UPLOAD_FOLDER= baseDirectory+"Maps/mapimages" 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowedExtension(fileName):
    return "." in fileName and fileName.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS

class InsertMapData(Resource):
    def __init__(self,**kwargs):
        self.db=kwargs['data']
    
    def post(self):
        userData=request.form

        if(len(Selectmapid(self.db,userData)) == 0):
            if 'file' not in request.files:
                return {"Error_msg":"Image is not available..Choose a image."}
            else:
                file = request.files["file"]
                if file and allowedExtension(file.filename):
                    fileName = secure_filename(file.filename) 
                    file.save(os.path.join(UPLOAD_FOLDER,fileName))
                    addmap = insertmap(userData,fileName,self.db) 
                    print(len(addmap))
                    
                    mapdata= Selectmapid(self.db,userData) 
                    print(len(mapdata))
                    if(len(mapdata) != 0):
                        addmapdata = insertmapdata(self.db,userData,mapdata[0]["map_id"])
                        return{"mapimage":addmap["Inserted Row"],"mapdata":addmapdata["Inserted Row"]}
                    else:
                        return {
                            "data":[],
                            "Error_msg":"map_data is not inserted"
                            }

                else:
                    return "image is not uploaded"
        else:
            return {
                "data":[],
                "Error_msg":" Map_Image is already existed"
                }
       
def insertmap(userData,name,db):
        query = "INSERT INTO map_image(event_id,map_title,map_image,date) VALUES(%s,%s,%s,%s)"
        values = (str(userData["event_id"]),str(userData["map_title"]),name,str(userData["date"]))
        print(values)
        cursor = db.cursor()  
        data=cursor.execute(query,values) 
        db.commit()
    
        return {"Inserted Row":data}
def Selectmapid(db,userData):
    query="SELECT map_id FROM map_image WHERE map_title='{0}' AND date='{1}' ORDER BY map_id DESC LIMIT 1".format(str(userData["map_title"]),str(userData["date"]))
    queryData=QueryData(db)
    data=queryData.selectQueryMethod(query) 
    return data


def mapdata(userData,MAPID):
    value=[]
    for x in json.loads(userData["data"]):
        value.append(
            (MAPID,x["hall_number"],x["description"],x["title"])
        ) 
    print (value)
    return value

def insertmapdata(db,userData,MAPID):
    
    query2 = "INSERT INTO map_data(map_id,hall_number,description,title) VALUES(%s,%s,%s, %s)"
    value1 = mapdata(userData,MAPID)
    queryData = QueryData(db)
    data=queryData.insertOrUpdateMany(query2, value1)
    return data