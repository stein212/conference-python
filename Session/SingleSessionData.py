from flask import Flask , request , jsonify
from flask_restful import Resource, Api ,reqparse
import json
import pymysql as mysql
import datetime
from flask_httpauth import HTTPBasicAuth

#mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")

auth = HTTPBasicAuth() 

USER_LOGIN = {"admin":"password"}


@auth.verify_password
def verify(username,password):
    if not(username,password):
        return False
    return USER_LOGIN.get(username) == password   
    # return True

@auth.error_handler
def error():
    return jsonify({"Error_msg":"UnAuthorized user"}),403


class SingleSessionData(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']

    @auth.login_required
    def get(self,eventId,sessionId):
        item = getSessionData(sessionId,self.data) 
        if len(dataPhraser(item)) == 0:
            return dataPhraser(item) , 202 
        return dataPhraser(item) , 200



def getSessionData(sessionId,db):
    query = "SELECT session.*,speaker.*,attendee.* FROM ((session INNER JOIN speaker ON session.session_id = {0}  AND session.session_id = speaker.session_id) INNER JOIN attendee ON  speaker.speaker_id = attendee.id)".format(str(sessionId))
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    item = [dict(zip([key[0] for key in cursor.description] , row)) for row in data] 
    return item  


def dataPhraser(item):
    setData = {}
    for x in item:
        concept = []
        if x["concepts"] == None:
            print("Not available")
        else:
            print(x["concepts"])
            concept = json.loads(x["concepts"])
        links = []
        if x["attendee_links_to_research"] != None: 
            links = json.loads(x["attendee_links_to_research"])
        tags = []
        if x["attendee_tags"] != None: 
            tags = json.loads(x["attendee_tags"])    
        if "session_id" in setData:
            speaker = {"speaker_id":x["speaker_id"],"role":x["role"],"id":x["id_number"],"about":x["attendee_synopsis"],"attendee_name":x["attendee_name"],"speaker_image":x["prof_img"],"linked_in":x["attendee_linkedin_profile"],"facebook":x["attendee_facebook"],"twitter":x["attendee_twitter"],"tags":tags,"interest":x["attendee_areas_of_interest"],"links":links,"website":x["attendee_research_websites"]}
            setData["speakers"].append(speaker)
        else:
            setData["session_id"] = x["session_id"]
            setData["session_topic"] = x["session_topic"]
            setData["session_desc"] = x["session_desc"]
            setData["start_time"] = x["start_time"].strftime('%Y-%m-%d %H:%M:%S')
            setData["end_time"] = x["end_time"].strftime('%Y-%m-%d %H:%M:%S') 
            setData["session_type"] = x["session_type"]
            setData["location"] = x["location"]                                 
            setData["event_id"] = x["event_id"]
            setData["concept"] = concept
            setData["speakers"] = [{"speaker_id":x["speaker_id"],"role":x["role"],"id":x["id_number"],"about":x["attendee_synopsis"],"attendee_name":x["attendee_name"],"speaker_image":x["prof_img"],"linked_in":x["attendee_linkedin_profile"],"facebook":x["attendee_facebook"],"twitter":x["attendee_twitter"],"tags":tags,"interest":x["attendee_areas_of_interest"],"links":links,"website":x["attendee_research_websites"]}]        
    return setData      




