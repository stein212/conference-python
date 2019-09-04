from flask import Flask , request , jsonify
from flask_restful import Resource, Api ,reqparse
import json
import pymysql as mysql
import datetime

from flask_httpauth import HTTPBasicAuth

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



class SessionData(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']

    @auth.login_required
    def get(self,eventId):
        # parser = request.get_json(force = True)
        # eventId = parser["eventId"]
        
        data = getSessionData(eventId,self.data)
        resp = DataResponse(data)
        response = resp.phrase()
        
        if len(response) > 0:
            return response , 200
        else:
            return response , 201    
        #return response



def getSessionData(eventId,db):
    #mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")
    query = "SELECT session.*,speaker.*,attendee.* FROM ((session INNER JOIN speaker ON session.session_id=speaker.session_id AND session.event_id = {0}) INNER JOIN attendee ON speaker.speaker_id = attendee.id) ORDER BY session.start_time ASC".format(str(eventId))
    cursor = db.cursor() 
    cursor.execute(query)
    result = cursor.fetchall() 
    #print(eventId)
    items = [dict(zip([key[0] for key in cursor.description], row)) for row in result] 
    return items   


class DataResponse:
    
    response2 = []
    def __init__(self,data):
        self.data = data
        #print(self.data)

    def phrase(self):
        response = {}
        for x in self.data:
            key = x['start_time'].strftime('%Y-%m-%d') 
            response[key] = {}
        # print(response)    
        
        for x in self.data:
            
            key = x['start_time'].strftime('%Y-%m-%d')
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

            if (x['start_time'].strftime('%Y-%m-%d %H:%M:%S')+ '.'+ str(x["session_id"]) in response[key]):
                speaker = {"speaker_id":x["speaker_id"],"role":x["role"],"id":x["id_number"],"about":x["attendee_synopsis"],"attendee_name":x["attendee_name"],"speaker_image":x["prof_img"],"linked_in":x["attendee_linkedin_profile"],"facebook":x["attendee_facebook"],"twitter":x["attendee_twitter"],"tags":tags,"interest":x["attendee_areas_of_interest"],"links":links,"website":x["attendee_research_websites"]}
                response[key][x['start_time'].strftime('%Y-%m-%d %H:%M:%S')+ '.'+ str(x["session_id"])]["speakers"].append(speaker) 

            else:
                setData = {}
                setData["session_id"] = x["session_id"]
                setData["session_topic"] = x["session_topic"]
                setData["session_desc"] = x["session_desc"]
                setData["start_time"] = x["start_time"].strftime('%Y-%m-%d %H:%M:%S') 
                setData["end_time"] = x["end_time"].strftime('%Y-%m-%d %H:%M:%S') 
                setData["session_type"] = x["session_type"]
                setData["location"] = x["location"]                                 
                setData["event_id"] = x["event_id"]
                setData["session_image"]=x["session_image"] 
                print(setData)
                setData["speakers"] = [{"speaker_id":x["speaker_id"],"role":x["role"],"id":x["id_number"],"about":x["attendee_synopsis"],"attendee_name":x["attendee_name"],"speaker_image":x["prof_img"],"linked_in":x["attendee_linkedin_profile"],"facebook":x["attendee_facebook"],"twitter":x["attendee_twitter"],"tags":tags,"interest":x["attendee_areas_of_interest"],"links":links,"website":x["attendee_research_websites"]}]
                response[key][x['start_time'].strftime('%Y-%m-%d %H:%M:%S')+ '.'+ str(x["session_id"])] = setData
        return response
        # for x in self.data:
        #     x['start_time'] = x['start_time'].strftime('%Y-%m-%d %H:%M:%S')
        #     x['end_time'] = x['end_time'].strftime('%Y-%m-%d %H:%M:%S')
        #     self.response2.append(x)

            

        