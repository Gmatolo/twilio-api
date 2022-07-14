import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']

auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+15055914607',
         to='+254719749633'
     )