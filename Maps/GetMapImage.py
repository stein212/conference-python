from flask import Flask , request , send_file , jsonify , redirect, url_for
from flask_restful import Resource, Api ,reqparse 
from CommonVariables.commonvariables import baseDirectory
from werkzeug.utils import secure_filename

class GetMapImages(Resource):

    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def get(self,imageName):
        imageName = secure_filename(imageName)
        
        print(imageName)
        try:
            return send_file(baseDirectory+"/Maps/mapimages/"+str(imageName)) 
        except:
            return send_file(baseDirectory+"/Maps/mapimages/error_map.jpeg") 
        