from flask import Flask
from flask_restful import Resource, Api
#import MySQLdb as mysql
import pymysql as mysql
from threading import Thread
from time import sleep 
import datetime
from DataBase import *
from flask_cors import CORS


#----------------------------------------#
from Registration.registration import *
from EventDetails.EventDetails import *
from LogingIn.LoginIn import *
from Session.SessionData import *
from Session.SingleSessionData import *
from Speaker.SpeakerDetails import *
from Speaker.AllSpeakers import *
from Speaker.SpeakerImage import *
from AttendeeDetails.Attendee import *
from AttendeeDetails.attendance import *
from UploadFiles.UploadFiles import *
from FCM.FcmSender import *
from UserTags.UserTags import *
from UserTags.AddTags import *
from UserTags.SearchSimilar import *
from UserTags.AllAttendees import *
from Registration.UpDateUserProfile import *
from Registration.UploadPicAndTags import *
from LogingIn.DeleteUsers import *
from profilePic.GetProfilePic import *
from AttendeeDetails.EditDetails import *
from AttendeeDetails.FilterAttendeeDetails import *
from FollowRequest.FollowRequest import *
from FollowRequest.CheckRequest import *
from CommonVariables.commonvariables import *
#from Questions.AskQuestions import *
from Maps.GetMapData import *
from Maps.GetMapImage import *
from Test1.Testing import *
from QueryData.CheckQueryData import *
from Session.SessionFiles import *

# ........................................... Admin 
from Admin.AllEventDetails.AllEventDetails import *
from Admin.AllEventDetails.PresentAndFutureEvent import *
from Admin.AllEventDetails.AddNewEvent import *
from Admin.Speaker.SingleSpeakerDetails import *
from Admin.Speaker.AddNewSpeaker import *
# from Admin.Speaker.AllSpeakers import *
from Admin.Map.MapDetails import *
from Admin.Map.InsertMap import *
from Admin.AddAttendees.AddAttendees import *
from Admin.Polls.SetPolls import *
from Admin.Polls.ListOfPolls import *
from Admin.Polls.PollAnswer import *
from Admin.Polls.GetPollsBySession import *
from Admin.session.Getsessiondetails import *
from Admin.session.ListOfSession import *
from Admin.session.GetSessionFromEventId import *
from Admin.Polls.AddNewPolls import *
from Admin.Polls.AddpollAnswer import *
from Admin.session.GetAttendeeAndUser import *
from Admin.session.AddSession import *
from Admin.session.AddSession2 import *
from Admin.session.UploadFilesToSession import *
from AttendeeDetails.ShareDetails import *
from Admin.SplashScreen.SplashScreen import *
from Admin.Polls.AllSession import AllSession
from Admin.Map.GetMapData2 import *
from Admin.Map.UpdateMapImageData import *
from Admin.Map.UpdateMapData import *
from Admin.Map.InsertMapData import *
from Admin.Map.DeleteMapData import *
from Admin.Speaker.DeleteSpeaker import *
from Admin.session.GetSessionDetail import *
from Admin.session.UpdateTime import *
from Admin.session.UpdateSession import *
from Admin.session.AddSpeaker import *
from Admin.session.AddUsers import *
from Admin.session.DeleteUser import *
from Admin.Users.AllUsers import *
from Admin.Users.InsertNewUsers import *
from Admin.Map.GetAllMap import *
from Admin.AddAttendees.AddAttendeesData import *



app = Flask(__name__)
CORS(app)
api = Api(app,prefix='/v0')

# mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")
# mysql_connection.autocommit(True)
connection = DataBase()
mysql_connection = connection.cursor()

#mysql_connection.begin()
# def refreshConnection():
#     while True:
        
#         global mysql_connection
#         # mysql_connection.close() 
#         sleep(10)   
#         #print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" - - New Connection to mysql extablished") 
#         mysql_connection = None
#         #mysql_connection = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")
        
#         print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" - - New Connection to mysql extablished") 
        
        
# Thread(target=refreshConnection).start()

#mysql_connection = mysql.connect(host='',user='test2', password='Test@123', database="dbtest")  


api.add_resource(UserRegistration, '/user/register',resource_class_kwargs={'data':mysql_connection})  

api.add_resource(UpDateInfo, '/update/attendee/<int:id>/details',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(UploadPicTags, '/update/attendee/<int:id>/profile',resource_class_kwargs={'data':mysql_connection})  

api.add_resource(CheckOtp, '/user/otp',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(EventDetails, '/event/details',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(Login, '/user/login',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(SessionData, '/user/get/all/session/event<string:eventId>-data',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(SingleSessionData, '/user/get/event/<string:eventId>/session/<int:sessionId>/data',resource_class_kwargs={'data':mysql_connection})

api.add_resource(SpeakerDetails, '/speaker/details-by/id/<int:speakerId>/data',resource_class_kwargs={'data':mysql_connection})

api.add_resource(AttendeeDetails, '/attendee/details-by/id/<int:attendeeId>/data',resource_class_kwargs={'data':mysql_connection})

api.add_resource(Attendance, '/attendee/attendance',resource_class_kwargs={'data':mysql_connection})

api.add_resource(UploadProfPic, '/upload',resource_class_kwargs={'data':mysql_connection})

api.add_resource(UploadMap, '/upload/map',resource_class_kwargs={'data':mysql_connection})

api.add_resource(GetImage, '/get/map',resource_class_kwargs={'data':mysql_connection})

api.add_resource(SendingNotification, '/notification',resource_class_kwargs={'data':mysql_connection})

api.add_resource(UserTags, '/get/<int:id>/taglist',resource_class_kwargs={'data':mysql_connection})

api.add_resource(SearchForAttendees, '/get/<string:tag>/tagmembers',resource_class_kwargs={'data':mysql_connection})

api.add_resource(SimilarAttendees, '/get/similar/<int:attendeeId>/attendees',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(SimilarPeople, '/get/similar/<int:attendeeId>/people',resource_class_kwargs={'data':mysql_connection})

api.add_resource(SimilarSpeakers, '/get/similar/<int:id>/speakers',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(GetProfilePicture, '/get/profile/image',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(AddTags, '/for/attendee/<int:id>/set/tags',resource_class_kwargs={'data':mysql_connection})

api.add_resource(GetAllSpeakers, '/get/event/<int:id>/all/speakers',resource_class_kwargs={'data':mysql_connection})

api.add_resource(GetSpeakerPicture, '/get/speaker/image/<int:id>/<string:name>',resource_class_kwargs={'data':mysql_connection})

# api.add_resource(EventDetails,'update/attendee/1/details')#,resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(EditAttendeeInfo, '/update/attendee/details',resource_class_kwargs={'data':mysql_connection})

api.add_resource(FollowRequest, '/send/request/now/event-<string:id>',resource_class_kwargs={'data':mysql_connection})

api.add_resource(CheckRequest,'/check/follow/request',resource_class_kwargs={'data':mysql_connection})  

api.add_resource(AllAttendees,'/get/all/attendees/<int:id>/event',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(AllSpeakers,'/get/all/speakers/<int:id>/event',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(FilteredAttendeeDetails,'/attendee/details/<int:id>/short',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(DeleteUsers,'/delete/users',resource_class_kwargs={'data':mysql_connection})  

api.add_resource(OtpIdentifier,'/all/otp') 

api.add_resource(DetailsOfMap,'/event/<int:eventId>/map/details',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(GetMapImages,'/event/map/images/<string:imageName>',resource_class_kwargs={'data':mysql_connection})

api.add_resource(GetSessionNameImage,'/session/name/image/<string:session_id>',resource_class_kwargs={'data':mysql_connection})

# .............................. Admin ..............................

api.add_resource(AllEventDetails , '/all/event/details/page/<int:pageNos>',resource_class_kwargs={'data':mysql_connection})

api.add_resource (PresentFutureDetailsOfEvent,'/event/details/presentandfuture',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource (NewEventdetails,'/add/new/event',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(Sample, '/query/data',resource_class_kwargs={'data':mysql_connection})  

api.add_resource (SingleSpeakerDetails ,'/get/speaker/<int:speakerId>/data',resource_class_kwargs={'data':mysql_connection})

# api.add_resource(AllSpeakers , '/all/speaker',resource_class_kwargs={'data':mysql_connection})

api.add_resource (AddNewSpeaker,'/add/new/speaker',resource_class_kwargs={'data':mysql_connection})

api.add_resource (MapDetails,'/add/new/map',resource_class_kwargs={'data':mysql_connection})

api.add_resource(InsertMapData,'/add/map',resource_class_kwargs={'data':mysql_connection})

api.add_resource (AddAttendees,'/add/<string:eventId>',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource (SetPolls,'/add/polls',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource (ListOfPolls,'/list/polls/by/<int:pageNos>',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource (PollAnswer,'/pol/answer',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(GetSessionFromEventId,'/get/all/session/by/event/<int:eventId>',resource_class_kwargs={'data':mysql_connection})

api.add_resource(SessionDetails,'/all/session/for/event/<int:event_id>',resource_class_kwargs={'data':mysql_connection})

api.add_resource(GetPollsBySession,'/get/poll/<string:session_id>',resource_class_kwargs={'data':mysql_connection})

api.add_resource(Insertpollquestion,'/insert/poll/question',resource_class_kwargs={'data':mysql_connection})

api.add_resource(AddPollAnswers,'/add/new/poll',resource_class_kwargs={'data':mysql_connection})

api.add_resource(GetAttendeeDetails,'/get/attendee/users/<string:eventId>',resource_class_kwargs={'data':mysql_connection})

api.add_resource(AddSession,'/add/session',resource_class_kwargs={'data':mysql_connection})

api.add_resource(AddSession2,'/add/session2',resource_class_kwargs={'data':mysql_connection})

api.add_resource(UploadFilesToSession,'/add/files/to/session/<string:session_id>',resource_class_kwargs={'data':mysql_connection})

api.add_resource(ShareDetails,'/share/details',resource_class_kwargs={'data':mysql_connection})

api.add_resource(SplashScreen,'/get/splash',resource_class_kwargs={'data':mysql_connection})

api.add_resource(AllSession,'/get/poll/session/<string:eventId>',resource_class_kwargs={'data':mysql_connection})

api.add_resource(GetMapData2,'/get/all/map/data/<string:eventId>',resource_class_kwargs={'data':mysql_connection})

api.add_resource(UpdateMapTitle,'/update/map/details/data',resource_class_kwargs={'data':mysql_connection})

api.add_resource(Mapdataupdate,'/update/map/data',resource_class_kwargs={'data':mysql_connection})

api.add_resource(InsertPointData,'/add/map/data',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(DeleteMapData,'/delete/map/data',resource_class_kwargs={'data':mysql_connection}) 

# ..................... Admin Session ......................ZipFile The class for reading and writing ZIP files.  See section 
# api.add_resource(DeleteMapData,'/session/details/',resource_class_kwargs={'data':mysql_connection}) 
api.add_resource(GetSessionDetailsById,'/get/session/<string:sessionid>/data',resource_class_kwargs={'data':mysql_connection})

api.add_resource(DeleteSpeaker,'/delete/speaker',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(DeleteUser,'/delete/user',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(UpdateSessionTime,'/edit/session/time',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(UpdateSessionDetails,'/edit/session/data',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(AddSpeakers,'/add/speakers',resource_class_kwargs={'data':mysql_connection})

api.add_resource(AddUsers , '/add/users',resource_class_kwargs={'data':mysql_connection})

# api.add_resource(DeleteUser,'/delete/user',resource_class_kwargs={'data':mysql_connection}) 

#.................------- USERS -----------.............#
api.add_resource(GetAllUserDetails,'/all/users',resource_class_kwargs={'data':mysql_connection})

api.add_resource(InsertNewUsers,'/add/new/users',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(GetMapDataDetail,'/get/event/<string:eventId>/map/data',resource_class_kwargs={'data':mysql_connection}) 

api.add_resource(AddAttendeeData,'/add/many/attendee/<string:eventId>',resource_class_kwargs={'data':mysql_connection}) 



if __name__ == '__main__':
    app.run(host=ipAddress,debug=True,threaded=True,processes=1)      




    