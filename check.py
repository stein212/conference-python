# from flask import Flask , jsonify
# from flask_restplus import Resource, Api , fields
# # from flask_pymongo import PyMongo
# import MySQLdb as mariadb
# import random
# import smtplib
# from Email.send_email import * 

# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.starttls()
# s.login("praveenkumar.u@3edge.in","Praveen@1996")
# mariadb_connection = mariadb.connect(host='127.0.0.1',user='root', password='password', database="isls")
# print(mariadb)
# cursor = mariadb_connection.cursor()

# # class DataBase:
# #     def __init__(self,mongo):
# #         self.mongo = mongo

# #     def userSignIn(self,payload):
# #         self.email = payload["email"]
# #         self.password = payload["password"]
# #         print(self.email) 
# #         x = database.mongo.db.users.find({})
# #         response = []
# #         for y in x:
# #             response.append(y["email"])
# #         return response    
# #     def saveUserData(self):
# #         x = self.mongo.db.users.insert_one({"email":self.email,"password":self.password}) 
# #         print(x)
# #         return True   

# app = Flask(__name__)
# api = Api(app)
# # app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/test2"
# # # mongo = PyMongo(app)
# # # database = DataBase(mongo)

# # class Register(Resource):
# #     def post(self):
# #         print(api.payload)
# #         email = api.payload["email"]
# #         password = api.payload["password"]
# #         x = database.mongo.db.users.find({})
        
# #         response = []
# #         for y in x:
# #             response.append(y["email"])
# #         if len(response) == 0 :
# #             database.saveUserData
# #             return database.userSignIn(api.payload)
# #         else :
# #             return response       
# # server = smtplib.SMTP('smtp.gmail.com', 587)
# # server.login("praveenkumar@3edge.in", "Praveen@1996")
# # msg = "Hello!" # The /n separates the message from the headers
# # server.sendmail("praveenkumar@3edge.in", "dacts@2019", msg)

# @api.route('/register')
# class SqlDb(Resource):
#     def post(self):
#         return api.payload



# @api.route('/sendmail')
# class SendMail(Resource):
#     def post(self):
#         intVal = random.randint(1000,9999)
#         msg = "Your OTP is :"+ str(intVal)
#         # print(msg)
#         # sql = "INSERT INTO user_basic_details (email_id,password) VALUES ('email','password')"
#         # cursor.execute(sql)
#         # mariadb_connection.commit()
#         send = sendMail(api.payload["email"],intVal)
#         return send


# if __name__ == '__main__':
#     app.run(debug=True)

   
def computeHCF(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf

num1 = 54 
num2 = 24

# take input from the user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1,"and", num2,"is", computeHCF(num1, num2))

def lcm(x, y):  
   if x > y:  
       greater = x  
   else:  
       greater = y  
  while(True):  
       if((greater % x == 0) and (greater % y == 0)):  
           lcm = greater  
           break  
       greater += 1  
   return lcm

Data = 
{ 
'student':
    { 
    'Ajith':{ 
        'class':'12th-A',
        'marks':[80,90,80],
        'respective_subject_name':["chemistry","maths","physics"]
        }, 
    'Bhanu':{ 
        'class':'12th-A',
        'marks':[60,89,95],
        'respective_subject_name':["chemistry","maths","physics"]
        },
    'Cris':{ 
        'class':'12th-B',
        'marks':[65,85,90],
        'respective_subject_name':["chemistry","maths","physics"] 
        },
    'Fathima':{ 
        'class':'12th-B',
        'marks':[80,90,80],
        'respective_subject_name':["chemistry","maths","physics"] 
        },
    'Karthick':{ 
        'class':'12th-C',
        'marks':[70,95,65],
        'respective_subject_name':["chemistry","maths","physics"] 
        },
    'Praveen':{ 
        'class':'12th-C',
        'marks':[80,90,85],
        'respective_subject_name':["chemistry","maths","physics"] 
        },
    },
'teachers-average':{},
'others':{} 
} 