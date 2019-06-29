from flask import Flask, request
from flask_restful import Resource, Api
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAAgS5PhGM:APA91bEwD_2_vVOhlNFifaQkLpHSFrD9faFuIUv5RN6WHKcTyoB3xFzqswnKha8vYTQu87mwEGhNGYaSqxxsbcgUgMMVw4j3Gns8JRX4EkSpzL9VSqEu974FzIoenl8KrIj1_qsjjZ_Q")

#push_service = FCMNotification(api_key="<api-key>", proxy_dict={})

class SendingNotification(Resource):
    def post(self):
        registration_id = "fmEWhwrcVsE:APA91bE65_mHNcBMPjG8uZto_pWiAoexEOk3pFFbua837BStw_Y2mF_IFvESFTft4GRWDMhBpP801ToPreVGAMfM1kba2U-jI48_xtaw8bc_3Jm9XRpRH2LlB6FMwPt-lsBF8RRuTIvU"
        message_title = "Uber update"
        message_body = "Hi john, your customized news for today is ready"
        result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
        return {"msg":"Sent"}

