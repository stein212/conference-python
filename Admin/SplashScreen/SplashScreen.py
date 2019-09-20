from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import json
import pymysql as mysql
import datetime
from flask_httpauth import HTTPBasicAuth
from QueryData.QueryData import QueryData


class SplashScreen(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs["data"]
    
    def get(self):
        # userData = request.get_json(force=true)
        query = "SELECT * FROM splash_screen_adds WHERE status = {0}".format(str(1))
        queryData = QueryData(self.db)
        data = queryData.selectQueryMethod(query)
        if(len(data) > 0):
            return {"duration":data[0]["duration"],"url":data[0]["splash_image_name"]}
        return {"duration":0,"url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoxAXjt1ZiieqEzISwbW9d7aqg0vSXyfpDrE9zylHxEFs2XyVg"}