from flask import Flask , request
from flask_restful import Resource, Api ,reqparse
import json
import pymysql as mysql

#mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")


class EventDetails(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']
        
    def get(self):
        # parser = request.get_json(force=True)
        # eventId = parser["eventId"]
        data = getDetails(self.data) 
        if(len(data) != 0):
            x = data[0]
            # vv = json.loads(x[4]) 
            # if 122 in vv:
            #     y = "Game of thrones"
            #     vv.append(125)
            #     query = "UPDATE event_details SET venue_address = '"+str(vv)+"'"
                
            #     c = mysql_connection.cursor()  
            #     c.execute(query)
            #     mysql_connection.commit()
            return {"event_id":x[0],"event_name":x[1],"event_desc":x[2],"venue_name":x[3],"venue_address":x[4],"event_start_date":x[5].strftime('%Y-%m-%d %H:%M:%S'),"event_end_date":x[6].strftime('%Y-%m-%d %H:%M:%S'),"registration_start_date":x[7].strftime('%Y-%m-%d %H:%M:%S'),"registration_end_date":x[8].strftime('%Y-%m-%d %H:%M:%S'),"registration_fee":int(x[9]),"venue_map1":x[10],"venue_map2":x[11],"current_status":x[12],"concept":json.loads(x[13]),"event_image":x[14]}
        else:
            return {"Error_msg":"Event is not found"}    
        
def getDetails(DB):
    query = "SELECT * FROM event_details WHERE current_status = 2" 
    c = DB.cursor()  
    c.execute(query)
    data  = c.fetchall()
    return list(data) 
    

