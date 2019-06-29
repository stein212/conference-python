from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import smtplib
import json
import pymysql as mysql
import time
import random
from time import sleep
from threading import Thread
#import threading


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("praveenkumar.u@3edge.in","Praveen@1996")
mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="mydb")
print(mysql)
cursor = mysql_connection.cursor()
temp_request = {}

class TempRegister(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']
        mysql_connection = self.data
        
    def post(self):
        parser = request.get_json(force=True)
        millis = int(round(time.time() * 1000))
        otp = random.randint(1000,9999)
        print(parser)
        email = parser['email']
        password = parser['password']
        name = parser['name']
        phoneNumber = parser['phoneNumber']
        self.sendEmail(parser['email'],otp)
        userData = {"email":email,"password":password,"name":name,"phoneNumber":phoneNumber,"otp":otp,"time":millis}
        temp_request[email] = userData
        print(temp_request)
        return {"msg":email}     
        
    def sendEmail(self,email,otp):
        return s.sendmail("praveenkumar@3edge.in",'"'+email+'"',''+str(otp)+'')

    def saveTempRegData(self,parser):
        millis = int(round(time.time() * 1000))
        otp = random.randint(1000,9999)
        sql = "INSERT INTO temp_user_register (email,password,name,phone_number,otp,time) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (parser["email"],parser["password"],parser["name"],parser["phone_number"],otp.str(),millis.str())
        cursor.execute(sql,val)
        mysql_connection.commit()
        sql = "SELECT * FROM temp_user_register WHERE email = %s"
        value = (parser['email'])
        cursor.execute(sql,value)
        mysql_connection.commit()
        myresult = cursor.fetchall()
        temp_id = 0
        for x in myresult:
            print(x)
        return "ok"

def deleteUnWanted():
    try:
        for x in temp_request:
            millis = int(round(time.time() * 1000))
            print(temp_request[x]["time"])
            print(millis - 500000)
            if temp_request[x]["time"] < (millis - 500000):
                del temp_request[x]
        print(temp_request)       
    except KeyError:
            print("Key value not found")                      
    
def onThread():
    while True:
        print("Running....")
        deleteUnWanted()
        sleep(60)
    
Thread(target=onThread).start()    

class CheckOtp(Resource):
    def post(self):
        try:
            parser = request.get_json(force=True)
            print(parser)
            millis = int(round(time.time() * 1000))
            if (temp_request[parser["email"]]["time"] > (millis - 500000)):
                if (temp_request[parser["email"]]["otp"] == parser["otp"]):
                    return {"msg":"Success on registration"}
                else:
                    return {"msg":"otp doesnt match"}
            else:
                return {"msg":millis - 500000,"sec":temp_request[parser["email"]]["time"]}
        except KeyError:
            return {"msg":"Error in server"}

class SetUserData:
    def __init__(self,email):
        self.email = email
        self.setData()

    def setData(self):
        print("ok")



                    

