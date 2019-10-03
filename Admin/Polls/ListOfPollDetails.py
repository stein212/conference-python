from flask import Flask , request , jsonify
from flask_restful import Api , Resource
import json
from QueryData.QueryData import QueryData

class GetListOfPollDetails(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']
    
    def get(self,sessionId):
        print(sessionId)
        getpollRes = getPoll(self.db,sessionId)
        # return getPollData(self.db,parsePolRes(getpollRes))
        return getPollData(self.db,parsePolRes(getpollRes))


def getPoll(db,sessionId):
    query = "SELECT poll.poll_title,poll.session_id,poll.event_id,poll.poll_id,poll_values.poll_values_id,poll_values.name,poll_values.val FROM (poll INNER JOIN poll_values ON poll.poll_id = poll_values.poll_id) WHERE poll.session_id={0}".format(str(sessionId))
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query) 
    return data

def parsePolRes(data):
    parseData = {}
    for x in data:
        if x["poll_id"] in parseData:
            parseData[x["poll_id"]]["data"].append({
                "val":x["val"],
                        "name":x["name"],
                        "count":0
            })
        else:
            parseData[x["poll_id"]] = {

                "poll_title":x["poll_title"],
                "session_id":x["session_id"],
                "event_id":x["event_id"],
                "poll_id":x["poll_id"],
                "data":[
                    {   "val":x["val"],
                        "name":x["name"],
                        "count":0
                        
                    }
                ]
            }
    return parseData

def listOfPollData(data):
    dataRes = []
    for x in data.values():
        dataRes.append(x)
    return dataRes

def getPollData(db,data):
    # return data
    response = []
    responseData = []
    
        
    nos = 0
    for a in data.values():
        value = getPollValueCount(db,a["poll_id"]) 
        # print(value)
        for x in value:
            indexData = 0
            for y in data[a["poll_id"]]["data"]:
                # print(y["val"],"-",x["poll_answer"])
                if y["val"] == x["poll_answer"]:
                    y["count"] = x["Count( poll_answer)"]
                    data[a["poll_id"]]["data"][indexData]["count"] = x["Count( poll_answer)"]
                indexData = indexData + 1 
                    # response[nos]["data"].append(
                    #     {
                    #         "value":y["val"],
                    #         "name":y["name"],
                    #         "count":x["Count( poll_answer)"] 
                    #     }
                    # )
        nos = nos + 1
    for x in data.values(): 
        responseData.append(x)

    return responseData 

def getPollValueCount(db,pollId):
    query = "SELECT poll_answer,Count( poll_answer) FROM poll_answer WHERE poll_id = {0} group by poll_answer".format(str(pollId))
    # print(query)
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    # print(data)
    return data 


