
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""
to_number = ""
from_number = ""
body_msg = "Hello! You got a message from the vaccine-checker!"

client = Client(account_sid, auth_token)

message = client.messages.create(
            to=to_number, 
                from_=from_number,
                    body=body_msg)

print(message.sid)

