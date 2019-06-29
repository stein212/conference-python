from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import json
import pymysql as mysql

# mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")
# print(mysql_connection)

class Login(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs["data"]

    def post(self):
        try:
            parser = request.get_json(force = True) 
            email = parser["email"]
            password = parser["password"]
            eventId = parser["eventId"]
            check = DataStorage(email,password,eventId)
            data = check.checkUserExist(self.db) 
            if (len(email) != 0) & (len(password) != 0) & (len(eventId) != 0):
                print(data)
                if data != None:
                    return {"userId":data[0],"email":data[3],"phoneNumber":data[4],"eventId":eventId} 
                else:
                    if check.checkEmail(self.db) != None:
                        return {"Error_msg":"Password is incorrect"},202    
                    return {"Error_msg":"Unable to find the user"},202
            else:
                return {"Error_msg":"Need every details"},202       
            

        except KeyError:
            return {"Error_msg":"Need every details"},500    




class DataStorage:
    def __init__(self,email,password,eventId):
        self.email = email
        self.eventId = eventId
        self.password = password

    def checkUserExist(self,db):
        query = "SELECT * FROM attendee WHERE attendee_email = %s AND attendee_password = %s AND event_id = %s"
        val = (self.email,self.password,self.eventId)  
        cursor = db.cursor() 
        cursor.execute(query,val)
        myresult = cursor.fetchone()                 
        #..........................
        print(json.dumps(myresult)) 
        return myresult

    def checkEmail(self,db):
        query = "SELECT * FROM attendee WHERE attendee_email = %s AND event_id = %s"
        val = (self.email,self.eventId)  
        cursor = db.cursor()  
        cursor.execute(query,val)
        myresult = cursor.fetchone()                 
        #..........................
        print(json.dumps(myresult)) 
        return myresult


