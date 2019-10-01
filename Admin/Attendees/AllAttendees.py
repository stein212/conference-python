from flask import Flask,request,jsonify
from flask_restful import Resource,Api,reqparse
import json
from QueryData.QueryData import *

class AllAttendeesDetails(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def get(self,eventId):
        query = "SELECT id,attendee_name,attendee_email,status FROM attendee WHERE event_id = {0}".format(eventId)
        queryData = QueryData(self.db)
        data = queryData.selectQueryMethod(query)
        return data