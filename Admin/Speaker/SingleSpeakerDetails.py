
from flask import Flask, request, redirect , jsonify

from flask_restful import Resource, Api 
from flask_httpauth import HTTPBasicAuth
import json
from QueryData.QueryData import *

auth = HTTPBasicAuth()

@auth.verify_password
def auth(username,password):
    print(username,password)
    return True


def wrongAuth():
    return {"Error_msg":"Unauthorized User"}

class SingleSpeakerDetails(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']

    #@auth.login_required
    def get(self,speakerId):
        query = "select speaker.*,attendee.*,session.* from (( speaker inner join attendee on speaker.speaker_id = id) inner join session on session.session_id = speaker.session_id ) where speaker_id = {0}".format(str(speakerId))
        queryData = QueryData(self.db)
        data = queryData.selectQueryMethod(query)
        #return jsonify(data)
        if len(data) != 0:
            return parseData(data)
            #return data

def parseData(data):
    parsedData = {}
    for x in data:        
        parsedData["attendee_affiliation"] = x["attendee_affiliation"]
        parsedData["attendee_areas_of_interest"] = x["attendee_areas_of_interest"]
        parsedData["attendee_contact_num"] = x["attendee_contact_num"]
        parsedData["attendee_email"] = x["attendee_email"]
        parsedData["attendee_facebook"] = x["attendee_facebook"]
        parsedData["attendee_first_login"] = x["attendee_first_login"]
        parsedData["attendee_linkedin_profile"] = x["attendee_linkedin_profile"]
        parsedData["attendee_links_to_research"] = x["attendee_links_to_research"]
        parsedData["attendee_name"] = x["attendee_name"]
        parsedData["attendee_password"] = x["attendee_password"]
        parsedData["attendee_research_websites"] = x["attendee_research_websites"]
        parsedData["attendee_synopsis"] = x["attendee_synopsis"]
        parsedData["attendee_tags"] = json.loads(x["attendee_tags"])
        parsedData["attendee_twitter"] = x["attendee_twitter"]
        if(x["concepts"] != None):
            parsedData["concepts"] = json.loads(x["concepts"])
        else:
            parsedData["concepts"] = []
        parsedData["event_id"] = x["event_id"]
        parsedData["id"] = x["id"]
        parsedData["prof_img"] = x["prof_img"]
        try:
            if(len(parsedData["sessionData"]) == 0 ):
                temp_val = {
                    "role":x["role"],
                    "session_desc":x["session_desc"],
                    "session_id":x["session_id"],
                    "session_topic":x["session_topic"],
                    "session_type":x["session_type"],
                    "start_time":x["start_time"].strftime("%Y-%MM-%DD %HH:%mm:%SS"),
                    "end_time":x["end_time"].strftime("%Y-%MM-%DD %HH:%mm:%SS")
                }
                parsedData["sessionData"].append(temp_val)
            else:
                temp_val = {
                    "role":x["role"],
                    "session_desc":x["session_desc"],
                    "session_id":x["session_id"],
                    "session_topic":x["session_topic"],
                    "session_type":x["session_type"],
                    "start_time":x["start_time"].strftime("%Y-%MM-%DD %HH:%mm:%SS"),
                    "end_time":x["end_time"].strftime("%Y-%MM-%DD %HH:%mm:%SS")
                }
                parsedData["sessionData"].append(temp_val)
        except:
            parsedData["sessionData"] = []
            if(len(parsedData["sessionData"]) == 0):
                parsedData["sessionData"] = []
                temp_val = {
                    "role":x["role"],
                    "session_desc":x["session_desc"],
                    "session_id":x["session_id"],
                    "session_topic":x["session_topic"],
                    "session_type":x["session_type"],
                    "start_time":x["start_time"].strftime("%Y-%MM-%DD %HH:%mm:%SS"),
                    "end_time":x["end_time"].strftime("%Y-%MM-%DD %HH:%mm:%SS")
                }
                parsedData["sessionData"].append(temp_val)
    return parsedData
