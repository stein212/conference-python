from flask import Flask , request , jsonify
from flask_restful import Resource, Api ,reqparse
import json
import pymysql as mysql
import datetime
from flask_httpauth import HTTPBasicAuth

#mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")

auth = HTTPBasicAuth()

USER_DATA = {"admin":"password"}

@auth.verify_password
def verify(userName,password):
    if not (userName and password):
        return False
    return USER_DATA.get(userName) == password

@auth.error_handler
def errorMsg():
    return jsonify({"Error_msg":"Unauthorized Connection"})  

class SimilarAttendees(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']
        #mysql_connection = self.data

    @auth.login_required
    def get(self,attendeeId):
        data = request.args.get("tags")
        eventId = request.args.get("eventId")
        # tags = getData(attendeeId,self.data) 
        # print(">>>>>>>>>>")
        # print(tags)
        # tags = ["flutter","python"]

        tags = json.loads(data) 

        if tags == None:
            tags = []
        attendees = []
        for tag in tags:
            result = lookForAttendees(tag,eventId,self.data)
            attendees.append(result)

        return attendeeListGenerator(filterAttendees(attendees,id))     
        #print(request.headers.get("tags")) 

class SimilarSpeakers(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']
        #mysql_connection = self.data

    @auth.login_required
    def get(self,id):
        # tags = request.args.get("tags")
        eventId = request.args.get("eventId")
        attendees = []
        # if tags == None:
        #     tags = []
        # 
        # for tag in tags:
        result = lookForMutualSpeakers(eventId,self.data)
        attendees.append(result)  
        return attendeeListGenerator(filterAttendees(attendees,id))  
        #print(request.headers.get("tags")) 

class SimilarPeople(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']
        #mysql_connection = self.data

    @auth.login_required
    def get(self,attendeeId):
        
        eventId = request.args.get("eventId")
        # tags = getData(attendeeId,self.data) 
        # print(">>>>>>>>>>")
        # print(tags)
        tags = ["flutter","python"] 

        #tags = json.loads(data) 
         
        if tags == None:
            tags = []
        attendees = []
        for tag in tags:
            result = lookForAttendees(tag,eventId,self.data)
            attendees.append(result)

        return attendeeListGenerator(filterAttendees(attendees,id))     
        #print(request.headers.get("tags")) 

# class SimilarAttendeesShortDetails(Resource):
#     def __init__(self, **kwargs):
#         self.data = kwargs['data']
#         #mysql_connection = self.data

#     @auth.login_required
#     def get(self,id):
#         data = request.args.get("tags")
#         eventId = request.args.get("eventId")
#         print("........")
#         print(data)
        
#         tags = json.loads(data)
#         if tags == None:
#             tags = []
#         attendees = []
#         for tag in tags:
#             result = lookForAttendees(tag,eventId,self.data)
#             attendees.append(result)
#         return attendeeListGenerator(filterAttendees(attendees,id)) 

def lookForAttendees(tag,eventId,db):
    print(tag)
    query = "SELECT * FROM dbtest1.attendee WHERE attendee_tags LIKE '%{0}%' AND event_id = '{1}';".format(tag,str(eventId))  
    cursor = db.cursor()
    cursor.execute(query)
    result1 = cursor.fetchall()
    items = [dict(zip((key[0] for key in cursor.description),row))for row in result1] 
    result = []
    for x in items:
        links = []
        if x["attendee_links_to_research"] != None: 
            links = json.loads(x["attendee_links_to_research"])
        tags = []
        if x["attendee_tags"] != None: 
            links = json.loads(x["attendee_tags"]) 
        data = {"speaker_id":x["id"],"id":x["id"],"about":x["attendee_synopsis"],"attendee_name":x["attendee_name"],"profile_image":x["prof_img"],"linked_in":x["attendee_linkedin_profile"],"facebook":x["attendee_facebook"],"twitter":x["attendee_twitter"],"tags":tags,"interest":x["attendee_areas_of_interest"],"links":links,"website":x["attendee_research_websites"]}
        if(len(data["links"]) == 0):
            print(data)
        else:
            result.append(data)
    return result

def filterAttendees(attendeesDetail,id):
    data = {}
    for detailList in attendeesDetail:
        for x in detailList:
            data[x["speaker_id"]] = x 
    try:
        del data[id]
    except:
        #print(data)
        print("Not available")            
    return data   

def attendeeListGenerator(data):
    attendeeList = []
    for x in data.values():
        attendeeList.append(x) 
    return attendeeList

def lookForMutualSpeakers(eventId,db):
    # query = "SELECT attendee.* , speaker.* FROM attendee INNER JOIN speaker ON attendee.id = speaker.speaker_id WHERE attendee.attendee_tags LIKE '%{0}%' AND event_id = '{1}'".format(tag,str(eventId))
    query = "SELECT attendee.* , speaker.* FROM attendee INNER JOIN speaker ON attendee.id = speaker.speaker_id WHERE attendee.event_id = '{0}'".format(str(eventId))
    cursor = db.cursor()
    cursor.execute(query)
    result1 = cursor.fetchall()
    print(result1)
    items = [dict(zip((key[0] for key in cursor.description),row))for row in result1]  
    result = []
    for x in items:
        links = []
        if x["attendee_links_to_research"] != None: 
            links = json.loads(x["attendee_links_to_research"])
        tags = []
        if x["attendee_tags"] != None: 
            tags = json.loads(x["attendee_tags"]) 
        data = {"speaker_id":x["speaker_id"],"role":x["role"],"id":x["id_number"],"about":x["attendee_synopsis"],"attendee_name":x["attendee_name"],"profile_image":x["prof_img"],"linked_in":x["attendee_linkedin_profile"],"facebook":x["attendee_facebook"],"twitter":x["attendee_twitter"],"tags":tags,"interest":x["attendee_areas_of_interest"],"links":links,"website":x["attendee_research_websites"]}
        result.append(data)   
    return result 

def getData(attendeeId,DB):
    query = "SELECT * FROM attendee WHERE id = {0}".format(str(attendeeId))  
    cursor = DB.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    item = [dict(zip([key[0] for key in cursor.description],row))for row in results] 
    print(item)
    if(len(item) > 0):
        tagData = item[0]["attendee_tags"]
        print(">>>>>>>> Tag data")
        print(tagData)
        if tagData == None:
            jsonData = []
            item[0]["attendee_tags"] = jsonData
        else:
            jsonData = json.loads(tagData) 
            item[0]["attendee_tags"] = jsonData
        
        return item[0]["attendee_tags"]

    else:
        return []

