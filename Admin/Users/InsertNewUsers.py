from flask import Flask, request,jsonify
from flask_restful import Resource, Api, reqparse
import json
from QueryData.QueryData import *
import os
import random
from flask import Flask, request, redirect, url_for , send_file 
from werkzeug.utils import secure_filename
import pymysql as mysql
from flask_httpauth import HTTPBasicAuth
from CommonVariables.commonvariables import *

#UPLOAD_FOLDER = baseDirectory+"/Maps/mapimages"
UPLOAD_FOLDER = baseDirectory+"/profilePic/profPic"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowedExtension(fileName):
    return "." in fileName and fileName.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS

class InsertNewUsers(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['data']
    def post(self):
        userData=request.form
        '''password = random.randint(10000,99999)
        query="INSERT INTO users(access,user_email,user_contact_num, user_name, user_password) VALUES (%s,%s,%s,%s,%s)"
        values=(str(userData["access"]),str(userData["user_email"]),str(userData["user_contact_num"]),str(userData["user_name"]),str(password))
        cursor = self.db.cursor()  
        data=cursor.execute(query,values) 
        self.db.commit()
        return {"Inserted Row":data}'''
        
        if 'file' not in request.files:
            return {"data":[],"Error_msg":"Image is not available..Choose a image."}
        else:
            file = request.files["file"]
            try:
                if file and allowedExtension(file.filename):
                    fileName = secure_filename(file.filename) 
                    file.save(os.path.join(UPLOAD_FOLDER,fileName)) 
                    data = InsertIntoUsers(userData,fileName,self.db) 
                    return {
                        "data":[data] 
                    }
                else:
                    return {"data":[],
                        "Error_msg":"Session is not inserted due to incorrect fileformat"
                    }
            except:
                return { "data":[],
                        "Error_msg":"Wrong File Path"
                        }



def InsertIntoUsers(userData,name,db):
    password = random.randint(10000,99999)
    query="INSERT INTO users(user_email,user_contact_num, user_name, user_password,user_image) VALUES (%s,%s,%s,%s,%s)"
    values=(str(userData["email"]),str(userData["contact_number"]),str(userData["user_name"]),str(password),name) 
    print(values) 
    # return 0
    queryData = QueryData(db)
    data = queryData.insertAndUpdateQueryMethod(query,values)
    return data