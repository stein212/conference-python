from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import json
import smtplib
import time
import random
import pymysql as mysql
from time import sleep
from threading import Thread

temp_request = {}
# mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")
# print(mysql_connection)


class DataStorage:
    def __init__(self):
        print("Running..")

    def checkUserExist(self,email,eventId,db):
        query = "SELECT * FROM attendee WHERE attendee_email = %s AND event_id = %s"
        val = (email,eventId) 
        cursor = db.cursor() 
        x = cursor.execute(query,val) 
        n = 0
        myresult = cursor.fetchall()
        for x in myresult:
            print(x[1])
            n = 1                
        print(myresult)
        if(n != 0):
            return True
        else:
            return False 

datastoring = DataStorage()


class UserRegistration(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']

    def post(self):
        parser = request.get_json(force=True)
        millis = int(round(time.time() * 1000))
        otp = random.randint(1000,9999)
        print(parser)
        email = parser['email']
        password = parser['password']
        name = parser['name']
        phoneNumber = parser['phoneNumber']
        eventId = parser["eventId"]
        print(len(phoneNumber)) 
        print(".....")
        if ( (len(email) != 0 and len(password)!= 0 ) and (len(name) != 0 and len(phoneNumber)!= 0)  and len(eventId) != 0):

            if(datastoring.checkUserExist(email,eventId,self.data)):
                return {"Error_msg":"Email already registered to this Event."}
                
            else:
                millis = int(round(time.time() * 1000))
                otp = random.randint(1000,9999)
                send = SendMail(email)
                send.sendOtp (otp)
                userData = {"email":email,"password":password,"name":name,"phoneNumber":phoneNumber,"otp":otp,"time":millis,"event_id":eventId}
                temp_request[email] = userData
                print(temp_request)
                return {"msg":email}

        else:
            return {"Error_msg":"Need every details"}   



class SendMail:
    def __init__(self,email):
        self.email = email
        
    def sendOtp(self,otp):
        millis = int(round(time.time() * 1000))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        msg = "Your OTP is {0}".format(str(otp))
        s.login("praveenkumar.u@3edge.in","Praveen@1996")
        s.sendmail("praveenkumar@3edge.in",'"'+self.email+'"',''+str(msg)+'') 

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
    def __init__(self, **kwargs):
        self.data = kwargs['data']

    def post(self):
        try:
            parser = request.get_json(force=True) 
            print(parser)
            millis = int(round(time.time() * 1000))
            if (temp_request[parser["email"]]["time"] > (millis - 500000)):
                if (temp_request[parser["email"]]["otp"] == parser["otp"]):
                    reg = RegisterUser(parser["email"])
                    data = reg.insertUserData(self.data)
                    return {"userId":data[0][0],"email":data[0][3],"phoneNumber":data[0][4],"eventId":temp_request[parser["email"]]["event_id"]}
                else:
                    return {"msg":"Otp doesnt match"}
            else:
                return {"msg":millis - 500000,"sec":temp_request[parser["email"]]["time"]} 
        except KeyError:
            return {"msg":"Error in server"} , 500  

class RegisterUser:
    def __init__(self,email):
        self.email = email

    def insertUserData(self,db):
        query = "INSERT INTO attendee (attendee_email,attendee_password,attendee_name,attendee_contact_num,event_id) VALUE (%s,%s,%s,%s,%s)"
        val = (temp_request[self.email]["email"],temp_request[self.email]["password"],temp_request[self.email]["name"],temp_request[self.email]["phoneNumber"],str(temp_request[self.email]["event_id"])) 
        c = db.cursor()
        c.execute(query,val)
        db.commit()
        query = "SELECT * FROM attendee WHERE attendee_email = %s AND attendee_password = %s"
        val = (temp_request[self.email]["email"],temp_request[self.email]["password"]) 
        #c = mysql_connection.cursor()
        c.execute(query,val)
        data = c.fetchall()
        return data 

class OtpIdentifier(Resource):
    def get(self):
        return temp_request




