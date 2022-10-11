import requests
from django.conf import settings

# Sms app functions

'''
This file contains sms class and methods w.r.t sms service providers
'''
# Provider - Msg91.com
class SMSMsg91:
    authKey = ''
    sandbox_mode=False

    def __init__(self, mobile, sms_logs=False):
        if mobile:
            self.mobile = mobile
            self.sms_logs = sms_logs

            if settings.SMS_SETTINGS["MSG91_AUTH_KEY"]:
                self.authKey = settings.SMS_SETTINGS["MSG91_AUTH_KEY"]

            if settings.SMS_SETTINGS["SMS_SANDBOX_MODE"]:
                self.sandbox_mode = settings.SMS_SETTINGS["SMS_SANDBOX_MODE"]
        else:
            return '{"message":"Mobile number missing", "type":"error"}'

    def SendOTP(self, payload="", template_id="", unicode="0", otp_length="4", otp_expiry_in_mins = "1440", email=""):
        
        sandbox_response = '{"request_id":"000000000000000000000000","type":"success"}'

        if self.sandbox_mode == True:
            return sandbox_response
        else:            
            url = "https://api.msg91.com/api/v5/otp?authkey=" + self.authKey  + "&mobile=" + self.mobile + "&template_id=" + template_id + "&unicode=" + unicode + "&otp_length=" + otp_length + "&otp_expiry=" + otp_expiry_in_mins + "&email=" + email

            response = requests.request("POST", url, data=payload)
            return response.text

    def ResendOTP(self):
        sandbox_response = '{"message":"retry send successfully","type":"success"}'
        
        if self.sandbox_mode == True:
            return sandbox_response
        else:
            url = "https://api.msg91.com/api/v5/otp/retry?authkey=" + self.authKey  + "&mobile=" + self.mobile + "&retrytype=text"

            response = requests.request("POST", url)
            return response.text

    def VerifyOTP(self, otp="", otp_expiry_in_mins = "1440"):
        sandbox_response = '{"message":"OTP verified success","type":"success"}'

        if self.sandbox_mode == True:
            return sandbox_response
        else:
            url = "https://api.msg91.com/api/v5/otp/verify?otp=" + otp + "&authkey=" +  self.authKey  + "&mobile=" + self.mobile + "&otp_expiry=" + otp_expiry_in_mins

            response = requests.request("POST", url)
            return response.text

    def SendTransactionSMS(self, message="", sender_id="", country="0", unicode="1", DLT_TE_ID=""):
        sandbox_response = '{"request_id":"000000000000000000000000","type":"success"}'

        if self.sandbox_mode == True:
            return sandbox_response
        else:
            url = "https://api.msg91.com/api/v2/sendsms"

            headers = { 'authkey': self.authKey, 'content-type': "application/json" }

            payload = '{"sender":"'+ sender_id +'","route":"4","country":"'+ country +'","unicode":"'+ unicode +'","DLT_TE_ID": "'+ DLT_TE_ID +'","sms":[{"message":"' + message + '","to": ['+ str(self.mobile) +']}]}'
            response = requests.request("POST", url, headers=headers, data=payload)
            return response.text
