from flask import Flask, request,jsonify
from flask_restful import Resource, Api
import json
from QueryData.QueryData import *


class GetSessionNameImage(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs["data"]
        
    def get(self,session_id):  
       
        query="SELECT * FROM session_files WHERE session_id ='{0}'".format(str(session_id))
        queryData=QueryData(self.db)
        data=queryData.selectQueryMethod(query)
        response = []
        for x in data:
            x["image"] = getImageName(x["session_file_name"])
            response.append(x)
        return response

#['pdf', 'zip', 'rar','png', 'jpg', 'jpeg'])
def getImageName(name):
    x = name.split('.')
    y = x[len(x)-1]
    if(y == 'pdf'):
        return "pdf.png"
    if(y == 'zip'):
        return 'zip.png'
    if( y == 'rar'):
        return 'rar.png'
    if(y == 'png'):
        return 'png.png'
    if(y == 'jpg'):
        return 'jpg.jpg'
    if(y == 'jpeg'):
        return 'jpeg.png'