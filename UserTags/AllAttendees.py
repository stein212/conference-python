from flask import Flask,request,jsonify
from flask_restful import Resource , Api , reqparse
import json
import pymysql as mysql
import datetime
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
def check(username,password):
    return True
        

class AllAttendees(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs["data"]
    @auth.login_required
    def get(self,id):
        try:
            query = "SELECT * FROM attendee WHERE event_id = {0}".format(str(id))
            cursor = self.db.cursor()
            cursor.execute(query)
            item = cursor.fetchall()
            description = cursor.description
            data = parseDataAttendees(item,description)
            return data,200

        except:
            return {"Error_msg":"Exception error"},202

class AllSpeakers(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs["data"]
    @auth.login_required
    def get(self,id):
        try:
            query = "SELECT attendee.* , speaker.* FROM attendee INNER JOIN speaker ON attendee.id = speaker.speaker_id WHERE attendee.event_id = '{0}'".format(str(id))
            cursor = self.db.cursor()
            cursor.execute(query)
            item = cursor.fetchall()
            description = cursor.description
            data = parseDataSpeakers(item,description)
            return removeRepeated(data),200
        except:
            return {"Error_msg":"Exception error"},202

def parseDataSpeakers(item,description):
    values = [dict(zip((key[0] for key in description),row)) for row in item]
    return removePassword(values)

def parseDataAttendees(item,description):
    values = [dict(zip((key[0] for key in description),row)) for row in item]
    return removeUnwantedData(values)

def removePassword(values):
    data = []
    for x in values:
        links = []
        if x["attendee_links_to_research"] != None: 
            links = json.loads(x["attendee_links_to_research"])
        tags = []
        if x["attendee_tags"] != None: 
            tags = json.loads(x["attendee_tags"])
        item = {"speaker_id":x["speaker_id"],"role":x["role"],"id":x["id_number"],"about":x["attendee_synopsis"],"attendee_name":x["attendee_name"],"speaker_image":x["prof_img"],"linked_in":x["attendee_linkedin_profile"],"facebook":x["attendee_facebook"],"twitter":x["attendee_twitter"],"tags":tags,"interest":x["attendee_areas_of_interest"],"links":links,"website":x["attendee_research_websites"]}
        data.append(item)
    return data

def removeUnwantedData(values):
    data = []
    for x in values:
        item = {"id":x["id"],"attendee_name":x["attendee_name"],"profile_image":x["prof_img"],"website":x["attendee_research_websites"],"interest":x["attendee_areas_of_interest"],"attendee_email":x["attendee_email"]}
        data.append(item)
    return data

def removeRepeated(data):
    filterData = {}
    results = []
    for x in data:
        filterData[x["id"]] = x
    
    for x in filterData.values():
        results.append(x)
    return results





        

        