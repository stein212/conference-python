from flask import Flask,request,jsonify
from flask_restful import Resource,Api,reqparse
import json
from QueryData.QueryData import *



class GetAllUserDetails(Resource):

    def __init__(self,**kwargs): 
        self.db = kwargs['data']

    def get(self):
        # pageNos = pageNos - 1
        # currentIndex = pageNos * 10
        query = "SELECT * FROM users"
        queryData = QueryData(self.db)
        return queryData.selectQueryMethod(query)