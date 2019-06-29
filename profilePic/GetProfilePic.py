import os
from flask import Flask, request, redirect, url_for , send_file , jsonify
from werkzeug.utils import secure_filename
from flask_restful import Resource, Api
import pymysql as mysql
from flask_httpauth import HTTPBasicAuth
from CommonVariables.commonvariables import baseDirectory

USER_PASSWORD = {
    "admin":"password"
}
auth = HTTPBasicAuth()

#mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")

@auth.verify_password
def verify(username,password):
    USER_PASSWORD[username] = password
    print(USER_PASSWORD)
    if not (username,password):
        return False
    return True

@auth.error_handler
def unAuthorize():
    return send_file(baseDirectory+"/profilePic/unauthorize.jpg","image/jpeg")

class GetProfilePicture(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs["data"]
        
    @auth.login_required
    def get(self):
        try:
            name = request.authorization
            print(name)
            imageName = getImageName(name.username,self.db)
            if imageName == None:
                return send_file(baseDirectory+"/profilePic/profPic/person.png","image/jpeg") 
            directory = baseDirectory+"/profilePic/profPic/{0}".format(imageName) 
            return send_file(directory,"image/jpeg")
        except:
            #print("Running")
            return send_file(baseDirectory+"/profilePic/profPic/person.png","image/jpeg")      

def getImageName(userId,db):
    query = "SELECT * FROM attendee WHERE id = {0}".format(str(userId)) 
    cursor = db.cursor()
    cursor.execute(query)       
    item = cursor.fetchall()
    if len(item) == 0:
        return "error.png"
    return item[0][16]  

def getAccess(userId,db):
    if len(userId) == 0 :
        return False
    query = "SELECT * FROM attendee WHERE id = {0}".format(str(userId)) 
    cursor = db.cursor()
    cursor.execute(query)       
    item = cursor.fetchall()
    if len(item) == 0:
        return False
    return True


