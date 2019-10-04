from flask import Flask, request
from flask_restful import Resource, Api
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAAbyL8xP4:APA91bGR-5gW5_yHzD8CuQYgiko11sJ_tzo9Oupp1XjAZBaxHpYLXaUz9M4vjOA49spcm296a3N3q5C98qeG0GDRa29S44Py3XBfXSbP1K1o7sX9L_jOBe0PV2oElanPVOAlPKaK-JTW")

#push_service = FCMNotification(api_key="<api-key>", proxy_dict={})

class SendingNotification(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']
    def post(self):
        userData = request.get_json(force=True)
        registration_id = "dLtl5QjoVIE:APA91bHvXmfh3TZTTVlKAMaxZDjeJuy8ynraEA3-7p6UqWon_5xAc-DWHjwe_6SZmdB_AZXKvat-YGA3ukhjzLLnVLHjcsrlmlU10nMw5rZMQ1DOJAQQx4Nd64HZPdsHCIi6qSJB8_LF"
        message_title = str(userData["title"])
        message_body = str(userData["message"])
        result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
        # result = push_service.notify_multiple_devices()
        return {"msg":result} 

