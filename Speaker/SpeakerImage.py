import os
from flask import Flask, request, redirect, url_for , send_file , jsonify
from werkzeug.utils import secure_filename
from flask_restful import Resource, Api
from CommonVariables.commonvariables import baseDirectory


class GetSpeakerPicture(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs["data"]
        
    def get(self,id,name):    
        try:
            directory = baseDirectory+"/profilePic/profPic/{0}".format(name) 
            return send_file(directory,"image/jpeg")
        except:
            if id == 1:
                return send_file(baseDirectory+"/profilePic/profPic/blank.jpg","image/jpeg")     
            return send_file(baseDirectory+"/profilePic/profPic/person.png","image/jpeg")






