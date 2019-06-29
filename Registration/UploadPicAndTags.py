import os
from flask import Flask, request, redirect, url_for , send_file 
from werkzeug.utils import secure_filename
from flask_restful import Resource, Api 
import json
import pymysql as mysql
from flask_httpauth import HTTPBasicAuth

#mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = "/users/apple/python/isls/profilePic/profPic"


def allowedExtension(fileName):
    return "." in fileName and fileName.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS

auth = HTTPBasicAuth()
USER_DATA = {
    "admin": "password"
}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password 

class UploadPicTags(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']
        #mysql_connection = self.data


    #@auth.login_required
    def post(self,id):
        print(request.headers)
        if 'file' not in request.files:
            try:
                tags = request.form["tags"]
                jso = json.loads(tags) 
                return setTag(id,jso,self.data)
            except:
                return {"msg":6}    
        else:
            file = request.files["file"]
            tags = request.form["tags"]
            if file.filename == " ":
                jso = json.loads(tags) 
                return setTag(id,jso,self.data) 
            try:
                if file and allowedExtension(file.filename):
                    fileName = str(id)+"_"+secure_filename(file.filename) 
                    file.save(os.path.join(UPLOAD_FOLDER,fileName))
                    jso = json.loads(tags) 
                    data = setTagAndImageName(id,jso,fileName,self.data) 
                    print(data) 
                    return {"msg":1},200
                else:
                    jso = json.loads(tags) 
                    data = setTag(id,jso,self.data)
                    return {"msg":2}
            except:
                jso = json.loads(tags) 
                data = setTag(id,jso,self.data) 
                return {"msg":3} 

def setTag(id,tags,DB):
    print(tags)
    query = "UPDATE attendee SET attendee_tags = %s WHERE id = %s" 
    val = (json.dumps(tags),str(id))  
    print(val)
    cursor = DB.cursor()  
    cursor.execute(query,val) 
    DB.commit()
    return {"msg":5}

def setTagAndImageName(id,tags,name,db):
    print(tags)
    query = "UPDATE attendee SET attendee_tags = %s , prof_img = %s WHERE id = %s" 
    val = (json.dumps(tags),name,str(id))  
    print(val)
    cursor = db.cursor()  
    cursor.execute(query,val) 
    db.commit()
    return {"msg":5}    
