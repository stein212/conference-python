from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import json
import pymysql as mysql
import datetime


#mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")

class UserTags(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']
        #mysql_connection = self.data
    
    def get(self,id):
        try:
            data = getTagList(id,self.data)
            list_of_tags = {"tag":[]}
            for x in data:
                list_of_tags["tag"].append({"tagName":x[1],"count":x[3],"tagId":x[0]}) 
            return {"msg":list_of_tags},200 
        except:
            return {"Error_msg":"Exception error"},500   


def getTagList(id,DB):
    query = "SELECT * FROM attendee_tag WHERE event_id = {0}".format(str(id))   
    cursor = DB.cursor()
    cursor.execute(query)
    result = cursor.fetchall()  
    return result



class SearchForAttendees(Resource):
    def get(self,tag):
        #parser = request.get_json(force = True)
        data = getTagMembers(tag)  
         
        #index = 0
        responseData = []
        if len(data) == 0:
            return {},202
        for x in data:
            # tagData = x["attendee_tags"]
            # jsonData = json.loads(tagData)
            # data[index]["attendee_tags"] = jsonData
            # del data[index]["attendee_password"]  
            responseData.append({"attendee_id":x["id"],"attendee_name":x["attendee_name"],"prof_pic":x["prof_img"]}) 
            # index = index + 1
        return responseData      
          



def getTagMembers(tag):
    query = "SELECT * FROM dbtest1.attendee WHERE attendee_tags LIKE '%{0}%';".format(tag)
    mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")
    cursor = mysql_connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    items = [dict(zip((key[0] for key in cursor.description),row))for row in result]
    return items 
