from flask import Flask, request 
from flask_restful import Resource, Api
import json
import time
import random
import pymysql as mysql

#mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")

class UpDateInfo(Resource):
    def __init__(self, **kwargs):
        self.data = kwargs['data']
        #mysql_connection = self.data

    def post(self,id):
        parse = request.get_json(force = True)
        interest = parse["interest"]
        researchLinks = parse["researchLinks"]
        researchWebsites = parse["websites"]
        facebook = parse["facebook"]
        twitter = parse["twitter"]
        linkedIn = parse["linkedIn"]
        if (len(interest) != 0):
            if((len(facebook) == 0) and (len(twitter) == 0) and (len(linkedIn) == 0)):  
                return {"Error_msg":"Need any one of the social media account"}  
            else:
                return responseFunction(interest,researchLinks,researchWebsites,facebook,twitter,linkedIn,self.data)  
        else:
            return {"Error_msg":"Need area of interest details"} 



def responseFunction(interest,researchLinks,researchWebsites,facebook,twitter,linkedIn,DB):
    query = 'UPDATE attendee SET attendee_areas_of_interest = %s,attendee_links_to_research = %s,attendee_research_websites = %s,attendee_facebook = %s , attendee_twitter = %s , attendee_linkedin_profile = %s WHERE id = 22'
    val = (str(interest),json.dumps(researchLinks),json.dumps(researchWebsites),facebook,twitter,linkedIn)     
    try:          
        cursor = DB.cursor()
        cursor.execute(query,val)
        DB.commit()
        return {"msg":"Success fully inserted"}     
    except:
        return {"msg":"Not inserted"}      
    

        


