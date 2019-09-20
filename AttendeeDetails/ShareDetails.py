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



class ShareDetails(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['data']

    def post(self):
        userData = request.get_json(force = True)
        # return "ok"
        if 1==1 :
            query1="SELECT * FROM attendee WHERE id={0}".format(str(userData["to"]))
            queryData = QueryData(self.db)
            data1 = queryData.selectQueryMethod(query1)
            query2="SELECT * FROM attendee WHERE id={0}".format(str(userData["from"]))
            queryData = QueryData(self.db)
            data2 = queryData.selectQueryMethod(query2)
        
        #return data1[0]["attendee_name"]
        #return {"from":data1,"to":data2}
        
            toTemp = template("http://155.254.17.159:5000/v0/get/speaker/image/0/"+str(data1[0]["prof_img"]),str(data1[0]["attendee_name"]),str(data1[0]["attendee_areas_of_interest"]),str(data1[0]["attendee_synopsis"]),str(data1[0]["attendee_email"]),str(data1[0]["attendee_contact_num"]),str(data1[0]["attendee_facebook"]),str(data1[0]["attendee_twitter"]),str(data1[0]["attendee_linkedin_profile"]),str(data1[0]["attendee_research_websites"]))
            fromTemp = template("http://155.254.17.159:5000/v0/get/speaker/image/0/"+str(data2[0]["prof_img"]),str(data2[0]["attendee_name"]),str(data2[0]["attendee_areas_of_interest"]),str(data2[0]["attendee_synopsis"]),str(data2[0]["attendee_email"]),str(data2[0]["attendee_contact_num"]),str(data2[0]["attendee_facebook"]),str(data2[0]["attendee_twitter"]),str(data2[0]["attendee_linkedin_profile"]),str(data2[0]["attendee_research_websites"]))
        

            toshare=SendMail(str(data1[0]["attendee_email"]))
            fromshare=SendMail(str(data2[0]["attendee_email"]))
            toshare.send(fromTemp)
            fromshare.send(toTemp)
        #totemplate=template(data1[0]x,data1[1].name,data1[2].botttomTitle,data1[3].synopsis,data1[4].email,data1[5].phoneNumber,data1[6].facebook,data1[7].twitter,data1[8].linkedin,data1[9].website)
        #fromtemplate=template(data2[0]x,data2[1].name,data2[2].botttomTitle,data2[3].synopsis,data2[4].email,data2[5].phoneNumber,data2[6].facebook,data2[7].twitter,data2[8].linkedin,data2[9].website)
            return {"data":[{"Mail-status":"Sent"}]}
        # except:
        #     return {"data":[],"Error_msg":"The email is not sent"}

def template(image,name,botttomTitle,synopsis,email,phoneNumber,facebook,twitter,linkedin,website):
    return '''
    <div style="background-color: rgba(121,121,121,0.3);height:600px;width:450px;white-space: initial;word-wrap: break-word;">
  <div style="padding: 16px;">
    <div style="width: 420px;height:220px;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    max-width: 400px;
    margin: auto;
    text-align: center;background-color: white;">
      <div style=" align-content: center;
      float: left;
      justify-content: center;
      display: grid;width:35%;background: linear-gradient(#dE685E, #EE786E);height: 100%;float: left;">
        <div style="">
          <!-- border-right: 1px solid grey; -->
          <img style="border-radius: 50%;" src="'''+image+'''" alt="" height="100px;width:100px;">
          <p style="font-size: 14px;font-weight: 800;color:whitesmoke;">'''+name+''' <br><span style="font-weight: 500;">('''+botttomTitle+''')</span></p> 
        </div>
      </div>
      <div style="width: 65%; float:right;">
        <div style="font-weight: 600;font-size:12px;text-align: left;padding-left: 8px;padding-top:8px;">
          SYNOPSIS:
        </div>
        <div style="font-weight: 300;font-size:10px;text-align: left;padding-left: 8px;padding-right: 8px;">
          '''+synopsis+'''
        </div>
        <div style="font-weight: 600;font-size:12px;text-align: left;padding-left: 8px;padding-top:8px;">
          EMAIL :
        </div>
        <div style="white-space: initial;font-weight: 300;font-size:10px;text-align: left;padding-left: 8px;padding-right: 8px;width: 80%;">
          '''+email+'''
        </div>
        <div style="font-weight: 600;font-size:12px;text-align: left;padding-left: 8px;padding-top:4px;">
          PHONE NUMBER :
        </div>
        <div style="font-weight: 300;font-size:10px;text-align: left;padding-left: 8px;padding-right: 8px;width: 80%;">
          '''+phoneNumber+'''
        </div>
      </div>
    </div>
  </div>
  <div style="height: 10px;">
  
  </div>
  <div style="padding: 16px;">
    <div style="width: 420px;height:220px;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    max-width: 400px;
    margin: auto;
    text-align: center;background-color: white;">
      <div style=" width:100%;background: linear-gradient(#dE685E, #EE786E);height: 100%;float: left;color: whitesmoke;">
        <div style="">
          <!-- border-right: 1px solid grey; -->
          <div style="font-weight: 900;font-size:12px;text-align: left;padding-left: 8px;padding-top:8px;">
            FACEBOOK :
          </div>
          <div style="font-weight: 300;font-size:10px;text-align: left;padding-left: 8px;padding-right: 8px;">
            '''+facebook+'''
          </div>
          <div style="font-weight: 900;font-size:12px;text-align: left;padding-left: 8px;padding-top:8px;">
            TWITTER :
          </div>
          <div style="font-weight: 300;font-size:10px;text-align: left;padding-left: 8px;padding-right: 8px;width: 80%;">
            '''+twitter+'''
          </div>
          <div style="font-weight: 900;font-size:12px;text-align: left;padding-left: 8px;padding-top:4px;">
            LINKEDIN :
          </div>
          <div style="font-weight: 300;font-size:10px;text-align: left;padding-left: 8px;padding-right: 8px;width: 80%;">
            '''+linkedin+'''
          </div>
          <div style="font-weight: 900;font-size:12px;text-align: left;padding-left: 8px;padding-top:4px;">
            WEBSITE :
          </div>
          <div style="font-weight: 300;font-size:10px;text-align: left;padding-left: 8px;padding-right: 8px;width: 80%;">
            '''+website+'''
          </div>
        </div>
      </div>
      
    </div>
  </div>
</div>
'''