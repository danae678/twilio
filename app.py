import os
from twilio.rest import Client
from dotenv import load_dotenv

#Simple program to send a test message from a Twilio number

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="heyyy.",
                     from_='+12057547814',
                     to=os.getenv('MY_NUMBER')
                 )

print(message.sid)
displaymessage = str(message.body)
print(displaymessage[38:])