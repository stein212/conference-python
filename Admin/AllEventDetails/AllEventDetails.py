from flask import Flask , request ,jsonify
from flask_restful import Api , Resource , reqparse
import json
class AllEventDetails(Resource):

    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def get(self,pageNos):
        pageNos = pageNos - 1
        currentIndex = pageNos * 10
        query = "SELECT * FROM event_details LIMIT {0},10".format(str(currentIndex))
        cursor = self.db.cursor()
        cursor.execute(query)
        item = cursor.fetchall()
       #    data = [dict(zip((key[0] for key in cursor.description),row)) for row in item]
        #item = [dict(zip([key[0] for key in cursor.description],row))for row in result]
        response = [] 
        for x in item:
            data2 = {"event_id":x[0],"event_name":x[1],"event_desc":x[2],"venue_name":x[3],"venue_address":x[4],"event_start_date":x[5].strftime('%Y-%m-%d %H:%M:%S'),"event_end_date":x[6].strftime('%Y-%m-%d %H:%M:%S'),"registration_start_date":x[7].strftime('%Y-%m-%d %H:%M:%S'),"registration_end_date":x[8].strftime('%Y-%m-%d %H:%M:%S'),"registration_fee":int(x[9]),"venue_map1":x[10],"venue_map2":x[11],"current_status":x[12],"concept":json.loads(x[13])}
            response.append(data2)
        return response
            
        
        


        
