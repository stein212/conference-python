from flask import Flask
from flask_restful import Resource, Api
from TempRegister.temp_register import *

# Init the Flask service .
app = Flask(__name__)

api = Api(app,prefix='/v0')

# Route to register detail by sending OTP to the email we give.
api.add_resource(TempRegister, '/user/register')

api.add_resource(CheckOtp, '/user/otp')

if __name__ == '__main__':
    app.run(host="192.168.70.15",debug=True) 