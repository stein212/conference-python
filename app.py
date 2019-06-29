from flask import Flask
from flask_restful import Resource, Api
#import MySQLdb as mysql
import pymysql as mysql
from Registration.registration import *
from EventDetails.EventDetails import *
from LogingIn.LoginIn import *
from Session.SessionData import *
from Session.SingleSessionData import *
from Speaker.SpeakerDetails import *
from Speaker.AllSpeakers import *
from Speaker.SpeakerImage import *
from AttendeeDetails.Attendee import *
from UploadFiles.UploadFiles import *
from FCM.FcmSender import *
from UserTags.UserTags import *
from UserTags.AddTags import *
from UserTags.SearchSimilar import *
from Registration.UpDateUserProfile import *
from Registration.UploadPicAndTags import *
from profilePic.GetProfilePic import *
from AttendeeDetails.EditDetails import *
from FollowRequest.FollowRequest import *
from FollowRequest.CheckRequest import *

app = Flask(__name__)

api = Api(app,prefix='/v0')

mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1",connect_timeout=1)  
#mysql_connection = mysql.connect(host='',user='test2', password='Test@123', database="dbtest")  


api.add_resource(UserRegistration, '/user/register',resource_class_kwargs={'data':mysql_connection})  

api.add_resource(UpDateInfo, '/update/attendee/<int:id>/details',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(UploadPicTags, '/update/attendee/<int:id>/profile',resource_class_kwargs={'data':mysql_connection})  

api.add_resource(CheckOtp, '/user/otp',resource_class_kwargs={'data':mysql_connection})

api.add_resource(EventDetails, '/event/details',resource_class_kwargs={'data':mysql_connection})

api.add_resource(Login, '/user/login',resource_class_kwargs={'data':mysql_connection})

api.add_resource(SessionData, '/user/get/event<string:eventId>-data',resource_class_kwargs={'data':mysql_connection})

api.add_resource(SingleSessionData, '/user/get/event/<string:eventId>/session/<int:sessionId>/data',resource_class_kwargs={'data':mysql_connection})

api.add_resource(SpeakerDetails, '/speaker/details-by/id/<int:speakerId>/data',resource_class_kwargs={'data':mysql_connection})

api.add_resource(AttendeeDetails, '/attendee/details-by/id/<int:attendeeId>/data',resource_class_kwargs={'data':mysql_connection})

api.add_resource(UploadProfPic, '/upload',resource_class_kwargs={'data':mysql_connection})

api.add_resource(UploadMap, '/upload/map',resource_class_kwargs={'data':mysql_connection})

api.add_resource(GetImage, '/get/map',resource_class_kwargs={'data':mysql_connection})

api.add_resource(SendingNotification, '/notification',resource_class_kwargs={'data':mysql_connection})

api.add_resource(UserTags, '/get/<int:id>/taglist',resource_class_kwargs={'data':mysql_connection})

api.add_resource(SearchForAttendees, '/get/<string:tag>/tagmembers',resource_class_kwargs={'data':mysql_connection})

api.add_resource(SimilarAttendees, '/get/similar/<int:id>/attendees',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(GetProfilePicture, '/get/profile/image',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(AddTags, '/for/attendee/<int:id>/set/tags',resource_class_kwargs={'data':mysql_connection})

api.add_resource(GetAllSpeakers, '/get/event/<int:id>/all/speakers',resource_class_kwargs={'data':mysql_connection})

api.add_resource(GetSpeakerPicture, '/get/speaker/image/<int:id>/<string:name>',resource_class_kwargs={'data':mysql_connection})

# api.add_resource(EventDetails,'update/attendee/1/details')#,resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(EditAttendeeInfo, '/update/attendee/details',resource_class_kwargs={'data':mysql_connection})

api.add_resource(FollowRequest, '/send/request/now/event-<string:id>',resource_class_kwargs={'data':mysql_connection})

api.add_resource(CheckRequest,'/check/follow/request',resource_class_kwargs={'data':mysql_connection})


if __name__ == '__main__':
    app.run(host="192.168.70.15",debug=False)   


    