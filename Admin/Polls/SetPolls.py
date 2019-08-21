from flask import Flask , request , jsonify
from flask_restful import Api , Resource
import json
from QueryData.QueryData import *

class SetPolls(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']
    
    def post(self):
        requestData = request.get_json(force=True)
        checkPollExistResponse = checkPollExist(self.db,requestData)
        if len(checkPollExistResponse) == 0:
            insertPollDataResponse = insertPollData(self.db,requestData)
            if insertPollDataResponse > 0:
                data = checkPollExist(self.db,requestData)
                print(data)
                if(len(data)) == 0:
                    return {"Inserted Data": 0}
                if data[0]["poll_type"] == 0:
                    insertPollValuesResponse = insertPollValues(self.db,requestData,data[0]["poll_id"])
                    if insertPollValuesResponse == len(requestData["options"]):
                        return {"msg":"{0} Data successfully inserted".format(insertPollValuesResponse)}
                    else:
                        return {"msg":"Only {0} Data successfully inserted".format(insertPollValuesResponse)}

                else:
                    return {"msg":"Poll is added without options"}

        else:
            return jsonify(checkPollExistResponse)

def parseDict(data,poll_id):
    tupleData = []
    for item in data["options"]:
        for x,y in item.items():
            tupleData.append((str(poll_id),str(x),str(y))) 
    return tupleData

def checkPollExist(db,data):
    query = "SELECT * FROM poll WHERE poll_title = '{0}' AND session_id = '{1}' AND event_id = '{2}'".format(str(data["poll_title"]),str(data["session_id"]),str(data["event_id"]))
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query) 
    return data

def insertPollData(db,data):
    query = "INSERT INTO poll (event_id,poll_type,poll_title,poll_comments,poll_start_time,session_id,poll_status) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (str(data["event_id"]),str(data["poll_type"]),str(data["poll_title"]),str(data["poll_comments"]),str(data["poll_start_time"]),str(data["session_id"]),str(1))
    cursor = db.cursor()
    cursor.execute(query,values)
    rowsInserted = cursor.rowcount
    db.commit()
    cursor.close()
    return rowsInserted

def insertPollValues(db,data,poll_id):
    query = "INSERT INTO poll_values (poll_id,name,val) VALUES (%s,%s,%s)"
    value = parseDict(data,poll_id)
    print(value)
    cursor = db.cursor()
    cursor.executemany(query,value)
    inserted = cursor.rowcount
    db.commit()
    cursor.close()
    return inserted
    
