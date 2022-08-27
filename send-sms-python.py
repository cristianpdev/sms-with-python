import os
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Send SMS with Twilio API and Python -- cristianpdev",
                     from_=os.environ['SMS_SENDER'],
                     to=os.environ['SMS_RECEIVER']
                 )

print(message.sid)