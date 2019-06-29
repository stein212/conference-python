from flask import Flask , jsonify
from flask_restplus import Resource, Api , fields
# from flask_pymongo import PyMongo
import MySQLdb as mariadb
import random
import smtplib
from Email.send_email import * 

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("praveenkumar.u@3edge.in","Praveen@1996")
mariadb_connection = mariadb.connect(host='127.0.0.1',user='root', password='password', database="isls")
print(mariadb)
cursor = mariadb_connection.cursor()

# class DataBase:
#     def __init__(self,mongo):
#         self.mongo = mongo

#     def userSignIn(self,payload):
#         self.email = payload["email"]
#         self.password = payload["password"]
#         print(self.email) 
#         x = database.mongo.db.users.find({})
#         response = []
#         for y in x:
#             response.append(y["email"])
#         return response    
#     def saveUserData(self):
#         x = self.mongo.db.users.insert_one({"email":self.email,"password":self.password}) 
#         print(x)
#         return True   

app = Flask(__name__)
api = Api(app)
# app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/test2"
# # mongo = PyMongo(app)
# # database = DataBase(mongo)

# class Register(Resource):
#     def post(self):
#         print(api.payload)
#         email = api.payload["email"]
#         password = api.payload["password"]
#         x = database.mongo.db.users.find({})
        
#         response = []
#         for y in x:
#             response.append(y["email"])
#         if len(response) == 0 :
#             database.saveUserData
#             return database.userSignIn(api.payload)
#         else :
#             return response       
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.login("praveenkumar@3edge.in", "Praveen@1996")
# msg = "Hello!" # The /n separates the message from the headers
# server.sendmail("praveenkumar@3edge.in", "dacts@2019", msg)

@api.route('/register')
class SqlDb(Resource):
    def post(self):
        return api.payload



@api.route('/sendmail')
class SendMail(Resource):
    def post(self):
        intVal = random.randint(1000,9999)
        msg = "Your OTP is :"+ str(intVal)
        # print(msg)
        # sql = "INSERT INTO user_basic_details (email_id,password) VALUES ('email','password')"
        # cursor.execute(sql)
        # mariadb_connection.commit()
        send = sendMail(api.payload["email"],intVal)
        return send


if __name__ == '__main__':
    app.run(debug=True)

   