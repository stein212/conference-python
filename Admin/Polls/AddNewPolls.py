from flask import Flask, request , jsonify
from flask_restful import Api, Resource, reqparse
import json
from QueryData.QueryData import *

class Insertpollquestion(Resource):

    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def post(self):
        userData = request.get_json(force = True)
        checkPollData = checkpollquestionwithsessionid(self.db , userData) 
        if(len(checkPollData) == 0):
            addPoll = addpollDetails(self.db,userData)
            # return addPoll
            if(addPoll["Inserted Row"] != 0):
                # keyValue = addKeyValue(self.db,userData)
                polData = checkpollquestionwithsessionid(self.db,userData) 
                print(">>>>>")
                print(len(polData))
                if(len(polData) != 0):
                    addData = addOptions(self.db,userData,polData[0]["poll_id"])
                    return {
                        "data":{"options":addData,"poll":addPoll} 
                        } 
                else:
                    return {
                        "data":[],
                        "Error_msg":"Poll is not inserted"
                        }
            else:
                return {
                    "data":[],
                    "Error_msg":"Poll is not inserted"
                    }
        else:
            return {
                "data":[],
                "Error_msg":"Poll for this session with the same question already exists"
            }


def checkpollquestionwithsessionid(db,userData):
    query1= "SELECT poll_id FROM poll WHERE poll_title='{0}' AND session_id = {1}".format(str(userData["poll_title"]),str(userData["session_id"]))
    print(query1)
    queryData = QueryData(db)
    data1 = queryData.selectQueryMethod(query1)
    print (data1)
    return data1

def addpollDetails(db,userData):
    query = "INSERT INTO poll(poll_title,session_id,event_id,poll_start_time,poll_status) VALUES(%s, %s, %s, %s,'1')"
    values = (str(userData["poll_title"]),str(userData["session_id"]),str(userData["event_id"]),userData["start_time"])
    queryData = QueryData(db)
    return queryData.insertAndUpdateQueryMethod(query, values)  

# def getInsertedPoll(db,userData):
#     query = " SELECT poll_id FROM poll WHERE poll_title = {0} AND session_id = {1}".format(str(userData["poll_title"]),str(userData["session_id"]))
#     queryData = QueryData(db)
#     data = queryData.selectQueryMethod(query)
#     return data


def addKeyValue(userData,pollId):
    value = []
    for x in userData["values"]:
        value.append(
            (pollId,x["key"],x["value"]) 
        )
    return value

def addOptions(db,userData,pollId):
    query = "INSERT INTO poll_values(poll_id,name,val) VALUES(%s,%s,%s)"
    value = addKeyValue(userData,pollId)
    queryData = QueryData(db)
    data = queryData.insertOrUpdateMany(query,value)
    return data


