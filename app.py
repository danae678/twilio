import os
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="heyyy.",
                     from_='+12057547814',
                     to=os.environ['MY_NUMBER']
                 )

print(message.sid)