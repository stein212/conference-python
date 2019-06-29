import os
from flask import Flask, request, redirect, url_for , send_file 
from werkzeug.utils import secure_filename
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

UPLOAD_FOLDER = "/users/apple/python/isls/UploadFiles/profPic"
UPLOAD_FOLDER2 = "/users/apple/python/isls/UploadFiles/map"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
ALLOWED_EXTENSIONS2 = set(['pdf', 'zip', 'rar','png', 'jpg', 'jpeg'])





# @auth.error_handler
# def unAuthorize():
#     return send_file("/Users/apple/python/isls/UploadFiles/map/error.png","image/jpeg")


def allowedExtension(fileName):
    return "." in fileName and fileName.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS

class UploadProfPic(Resource):
    def post(self):
        if "file" not in request.files:
            return {"Error_msg":"File is not available"},202

        file = request.files["file"]

        if file.filename == " ":
            return {"Error_msg":"FileName is not available"},202    
        
        if file and allowedExtension(file.filename):
            fileName = "1_"+secure_filename(file.filename) 
            file.save(os.path.join(UPLOAD_FOLDER,fileName)) 
            return {"msg":fileName},200

        return {"Error_msg":"Error in extension"},202 


def allowedExtension2(fileName):
    return "." in fileName and fileName.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS2

class UploadMap(Resource):
    def post(self):
        if "file" not in request.files:
            return {"Error_msg":"File is not available"},202

        file = request.files["file"]

        if file.filename == " ":
            return {"Error_msg":"FileName is not available"},202    
        
        if file and allowedExtension2(file.filename):
            fileName = "1_"+secure_filename(file.filename) 
            file.save(os.path.join(UPLOAD_FOLDER2,fileName))
            return {"msg":fileName},200

        return {"Error_msg":"Error in extension"},202


USER_AUTH = {
    "admin":"password"
}

auth = HTTPBasicAuth()

@auth.verify_password
def auth(username,password):
    if not (username,password):
        return False
    return USER_AUTH.get(username) == password  

class GetImage(Resource):
    #@auth.login_required 
    def get(self):
        name = request.headers.get("name") 
        try:
            if((id == "Praveen") and (password == "praveen00")):
                sendImage = "/Users/apple/python/isls/UploadFiles/map/{0}".format(str(name)) 
                return send_file(sendImage,"image/jpeg")
            return send_file("/Users/apple/python/isls/UploadFiles/map/error.png","image/jpeg")    
        except:
            return send_file("/Users/apple/python/isls/UploadFiles/map/error.png","image/jpeg")     

        return send_file("/Users/apple/python/isls/UploadFiles/map/error.png","image/jpeg")         
              





