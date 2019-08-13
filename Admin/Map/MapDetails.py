from flask import Flask, request , jsonify, redirect, url_for , send_file 
from flask_restful import Api, Resource, reqparse
import os
import json
from werkzeug.utils import secure_filename
from QueryData.QueryData import *
from CommonVariables.commonvariables import baseDirectory

UPLOAD_FOLDER = baseDirectory+"Maps/mapimages"

class MapDetails(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def post(self):
        if 'files' not in request.files:
            return {"msg":"Need Image File"},202

        else:
            file = request.files['files']         
            mapTittle = request.form["map_tittle"]   
            eventId = request.form["event_id"]   
            mapData = json.loads(request.form['map_data']) 
            # listOfValuesOfMapData = []
            
            fileName = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER,fileName))
            insertMapImageResponse = insertMapImage(self.db,fileName,mapTittle,eventId)
             
            if(insertMapImageResponse["Inserted Row"] > 0):
                selectMapImageDataResponse = selectMapImageData(self.db,eventId,fileName)
                print(selectMapImageDataResponse)
                if 'map_id' in selectMapImageDataResponse[0]:
                    # insertMapDataResponse = insertMapData(self.db)
                    values = generateListOfMapData(mapData,selectMapImageDataResponse[0]["map_id"])
                    print(values)
                    insertMapDataResponse = insertMapData(self.db,selectMapImageDataResponse[0]["map_id"],values)
                    # return insertMapDataResponse
                    if(insertMapDataResponse["Inserted Row"] == len(values)):
                        return {"msg":"success"}
                    else:
                        return {"msg":"Not inserted map data"},203
                else:
                    return {},202
            

def generateListOfMapData(data,mapId):
    listOfValuesOfMapData = []
    for x in data["data"]:
        listOfValuesOfMapData.append(tuple((str(mapId),str(x["hall_no"]),str(x["description"]),str(x["tittle"]))))
    # print(listOfValuesOfMapData)
    return listOfValuesOfMapData

def insertMapImage(db,mapName,mapTittle,eventId):
    query = "INSERT INTO map_image (event_id,map_image,map_title) VALUES (%s,%s,%s)"
    val=(eventId,mapName,mapTittle)
    queryData = QueryData(db)
    data = queryData.insertAndUpdateQueryMethod(query,val)
    return data

def insertMapData(db,mapId,mapdata):
    query = "INSERT INTO map_data (map_id,hall_number,description,title) VALUES (%s,%s,%s,%s)"
    # # listOfValue = mapdata
    # queryData = QueryData(db)
    # data = queryData.insertOrUpdateMany(query,mapdata)
    # return data
    cursor = db.cursor()
    cursor.executemany(query,mapdata)
    db.commit()
    return {"Inserted Row" : cursor.rowcount}

def selectMapImageData(db,eventId,mapImageName):
    query = "SELECT map_id FROM map_image WHERE map_image = '{0}' AND event_id = {1}".format(str(mapImageName),str(eventId))
    print(query)
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data



            

