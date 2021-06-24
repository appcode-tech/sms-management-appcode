from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from sms_app.utils import SMSMsg91

# Create your views here.

class SmsMsg91Test(View):
    '''
    View for integration tests of sms methods
    '''

    def get(self, request):
        
        # Create obj of class
        obj = SMSMsg91(mobile="", sandbox_mode=False)
        
        # SendOTP
        # payload = '{ "VAR1": "<#>", "VAR2": "60RvwNCEDSU" }'
        # result = obj.SendOTP(template_id="605acffded8a7f04c36a4715", payload=payload)

        ''' ResendOTP '''
        # result = obj.ResendOTP()
        
        ''' VerifyOTP '''
        # result = obj.VerifyOTP(otp="3186")

        ''' Send transaction sms '''
        
        # msg = "Dear Test,%0a%0aShagun of INR 27 is successfully sent to Test1. You can request acknowledgement from Test1 in Envites app -- Profile -- Wallet -- Sent eShagun -- Request for acknowledgement.%0a%0a- Team Envites (Addnum Infotech)"
        # result = obj.SendTransactionSMS(message=msg, sender_id="ADDNUM", DLT_TE_ID="1007161795518439782")

        return HttpResponse(result)