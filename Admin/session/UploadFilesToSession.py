import os
from flask import Flask, request, redirect, url_for , send_file 
from werkzeug.utils import secure_filename
from flask_restful import Resource, Api 
import json
import pymysql as mysql
from flask_httpauth import HTTPBasicAuth
from CommonVariables.commonvariables import *

UPLOAD_FOLDER = baseDirectory+"Admin/session/sessionfiles"
ALLOWED_EXTENSIONS = set(['pdf', 'zip', 'rar','png', 'jpg', 'jpeg'])


def allowedExtension(fileName):
    return "." in fileName and fileName.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS


class UploadFilesToSession(Resource):
    def __init__(self,**kwargs):
        self.data=kwargs['data']
    
    def post(self,session_id):
        if 'file' not in request.files:
            return {
                "data":[],
                "Error_msg":"File is not found."
                }
        file = request.files["file"]
        if len(checkSessionInSession(self.data,session_id)) > 0:
            fileNameCheck = str(session_id)+"-"+secure_filename(file.filename) 
            if len(checkSessionInSessionFiles(self.data,session_id,fileNameCheck)) == 0:
                if 'file' not in request.files:
                    return {"Error_msg":"Image cannot be uploaded { 2 }."},400
                else:
                    file = request.files["file"]
                    if file and allowedExtension(file.filename):
                        fileName = str(session_id)+"-"+secure_filename(file.filename) 
                        file.save(os.path.join(UPLOAD_FOLDER,fileName))
                        data = InsertIntoSession(session_id,fileName,self.data) 
                        print(data) 
                        return data,200 
                    
                    else:
                        return {"Error_msg":"File extension cannot be uploaded."},400
            else:
                return {
                "data":[],
                "Error_msg":"The same file is already uploaded to the session."
                }

        else:
            return {
                "data":[],
                "Error_msg":"Please select the correct session."
                }

def checkSessionInSession(db,session_id):
    query="SELECT session_id FROM session WHERE session_id ={0}".format(str(session_id))
    cursor = db.cursor()
    cursor.execute(query)
    item = cursor.fetchall()
    return item  

def checkSessionInSessionFiles(db,session_id,fileName):
    query="SELECT session_id FROM session_files WHERE session_id ={0} AND session_file_name = '{1}'".format(str(session_id),str(fileName))
    cursor = db.cursor()
    cursor.execute(query)
    item = cursor.fetchall()
    return item        

def InsertIntoSession(session_id,name,db):
    #query = "UPDATE session_files SET session_file_name = '{0}' WHERE session_id = %s" 
    query="INSERT INTO session_files(session_file_name,session_id) VALUES(%s,%s)"
    val = (name,str(session_id))  
    print(val)
    cursor = db.cursor()  
    cursor.execute(query,val) 
    db.commit()
    return {
                "data":[{"inserted":"ok"}]
                
                } 