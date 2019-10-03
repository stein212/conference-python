from flask import Flask , request , jsonify
from flask_restful import Api , Resource
import json
from QueryData.QueryData import *

class AllSession(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']
    
    def get(self,eventId):
        allSession = getAllSession(self.db,eventId)
        pollSession = getPollSessionCount(self.db,eventId)
        # return jsonify(pollSession)
        data = parseData(allSession,pollSession)
        return data

        

def getAllSession(db,eventId):
    query = "SELECT * FROM session WHERE event_id={0}".format(str(eventId))
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    response = []
    
    for x in data:
        x["start_time"] = x["start_time"].strftime('%Y-%m-%d %H:%M:%S')
        x["end_time"] = x["end_time"].strftime('%Y-%m-%d %H:%M:%S')
        response.append(x)
    return response
    

def getPollSessionCount(db,eventId):
    query = "SELECT session.session_id,COUNT(poll.session_id) FROM session INNER JOIN poll ON poll.session_id = session.session_id WHERE session.event_id = {0} group by poll.session_id".format(str(eventId))
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data
    
def parseData(session,pollCount):
    data = {}
    # return session
    for x in session:
        data[x["session_id"]]= x
    n = 0
    # return data
    for x in pollCount:
        if x["session_id"] in data:
            data[x["session_id"]]["count"] = x["COUNT(poll.session_id)"] 
            print("true")
        
    # return data
    response = []
    for x in data.values():
        if "count" in x:
            response.append(x)
        else:
            x["count"] = 0
            response.append(x)
    return response


# 15:37:15	SELECT poll_answer.poll_answer,COUNT(DISTINCT poll_answer.poll_answer) FROM poll INNER JOIN poll_answer ON poll.poll_id = poll_answer.poll_id WHERE poll.session_id =1 group by poll.session_id LIMIT 0, 50000	Error Code: 1055. Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'dbtest2809.poll_answer.poll_answer' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by	0.0032 sec

