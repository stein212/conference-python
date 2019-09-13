from flask import Flask, request,jsonify
from flask_restful import Resource, Api, reqparse
import json
from QueryData.QueryData import *

class AddPollAnswers(Resource):
    def __init__(self,**kwargs):
        self.db=kwargs['data']
    
    def post(self):
        userData=request.get_json(force=True)
        
        
        if  (len(checkPollidExists(self.db,userData))!=0):
            
            if (len(checkAttendeeidExists(self.db,userData))==0):
                if(len(checkpollidandattendeeid(self.db,userData))==0):
                    #return {"Error_msg":"User with the given email does not exist."} 
                    if checkpollstatus(self.db,userData)["Inserted Row"]== 1:
                        return {"data":[{"Inserted Row":1}]}
                    else:
                        return {"data":[],"Error_msg":"The data is not inserted."}  

                            
                else:
                    return {"data":[],"Error_msg":"Given details already existed"}               
            else:
                return{"data":[],"Error_msg":"Given attendee_id is available"}
                
        else:
            return{"data":[],"Error_msg":"Given poll_id is not existed"} 

                                       
        
                

def checkPollidExists(db,userData):
    query = "SELECT poll_id FROM poll WHERE poll_id = {0}".format(userData["poll_id"])
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data
def checkAttendeeidExists(db,userData):
    query = "SELECT attendee_id FROM attendee WHERE attendee_id = '{0}'".format(userData["attendee_id"])
    print(query)
    queryData = QueryData(db)
    data1 = queryData.selectQueryMethod(query)
    return data1

def checkpollidandattendeeid(db,userData):
    query = "SELECT attendee_id FROM poll_answer WHERE poll_id = '{0}' AND attendee_id = '{1}'".format(userData["poll_id"],userData["attendee_id"])
    print(query)
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    return data

def checkpollstatus(db,userData):
    query="SELECT poll_status FROM poll WHERE poll_id={0}".format(userData["poll_id"])
    queryData = QueryData(db)
    data = queryData.selectQueryMethod(query)
    if data[0]["poll_status"]==1:
        query1 = "INSERT INTO poll_answer(poll_id,attendee_id,poll_answer,role) VALUES(%s, %s, %s, %s)"
        values = (str(userData["poll_id"]),str(userData["attendee_id"]),str(userData["poll_answer"]),str(userData["role"]))
        queryData = QueryData(db)
        return queryData.insertAndUpdateQueryMethod(query1, values)
    else:
        return {"Inserted Row":0}