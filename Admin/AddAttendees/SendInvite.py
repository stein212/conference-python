from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import json
import smtplib
import time
import random
import pymysql as mysql
from time import sleep
from threading import Thread
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from QueryData.QueryData import *

class SendMail:
    def __init__(self,email):
        self.email = email
        
    def send(self,template):
        #millis = int(round(time.time() * 1000)) 
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Link"
        msg['From'] = ""
        msg['To'] = ""
        html = template

        part = MIMEText(html, 'html')
        msg.attach(part)
        # msg = "Your OTP is {0}".format(str(otp)) 
        s.login("praveenkumar.u@3edge.in","Praveen@1996") 
        # s.sendmail("praveenkumar@3edge.in",'"'+self.email+'"',''+str(msg)+'') 
        s.sendmail("praveenkumar@3edge.in",'"'+self.email+'"',str(msg)) 



class SendInvite(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['data']

    def post(self):
        userData = request.get_json(force = True)
        # return "ok"
        try:
            email = userData["email"]
            eventId = userData["event_id"]
            checkAttendeeResp = checkAttendee(self.db,email,eventId)
            if(len(checkAttendeeResp) > 0):
                

                attendee = SendMail(str(email))
                attendee.send(template(checkAttendeeResp[0]["attendee_email"],checkAttendeeResp[0]["attendee_password"]))
                update = updateAttendee(self.db,checkAttendeeResp[0]["id"])
                return {"data":[ {"Mail-status":"Sent"} ] } 
            else:
                return {"data":[],"Error_msg":"Attendee not found in the database."}
        
        
        
            

            
            
        #totemplate=template(data1[0]x,data1[1].name,data1[2].botttomTitle,data1[3].synopsis,data1[4].email,data1[5].phoneNumber,data1[6].facebook,data1[7].twitter,data1[8].linkedin,data1[9].website)
        #fromtemplate=template(data2[0]x,data2[1].name,data2[2].botttomTitle,data2[3].synopsis,data2[4].email,data2[5].phoneNumber,data2[6].facebook,data2[7].twitter,data2[8].linkedin,data2[9].website)
            
        except:
            return {"data":[],"Error_msg":"The email is not sent , due to internal email sending server."}

def template(email,password):
    return '''
    <div style="padding: 16px;background-color:rgba(127,127,127,0.2);">
  <div style="background-color:white;padding:8px;">
    <p style="color:rgb(81,156,199);font-weight:800;font-size:18px;">Thank you for registering in International Singapour Lipid Symposium.</p>
    <p style="color:rgb(27,27,27);font-weight:800;font-size:16px;">Please find the credientials below to login to your account:</p>
    <p><strong>Email :</strong>'''+email+'''</p>
    <p><strong>Password :</strong>'''+password+'''</p>
    <a href="https:www.playstore.com">Click here to download the Mobile application</a>
  </div>
</div>
    '''

def checkAttendee(db,email,eventId):
    query = " SELECT * FROM attendee WHERE attendee_email = '{0}' AND event_id = '{1}'".format(str(email),str(eventId))
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data 

def updateAttendee(db,id):
    query = "UPDATE attendee SET status = 1 WHERE id= {0}".format(str(id)) 
    queryData = QueryData(db)
    data = queryData.insertAndUpdateQueryMethod(query,())
    print(data)
    return data