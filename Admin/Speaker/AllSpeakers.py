from flask import Flask, request, redirect , jsonify

from flask_restful import Resource, Api 
from flask_httpauth import HTTPBasicAuth
import json
from QueryData.QueryData import *


class AllSpeakers(Resource):

    def __init__(self,**kwargs):
        self.db = kwargs["data"]
    
    def get(self):
        queryData = QueryData(self.db)
        query = "SELECT speaker.*,attendee.attendee_name,attendee.attendee_email,attendee.attendee_contact_num FROM speaker INNER JOIN attendee ON speaker.speaker_id=attendee.id"
        data = queryData.selectQueryMethod(query)
        return data