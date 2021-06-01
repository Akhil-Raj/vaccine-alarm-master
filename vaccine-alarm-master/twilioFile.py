
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC4f20b5df995843f5b73d443a4bc321db"
# Your Auth Token from twilio.com/console
auth_token  = "6c6f842638b2fbaa94769c48c294ab9b"
to_number = "+919045907963"
from_number = "+13392934573"
body_msg = "Hello! You got a message from the vaccine-checker!"

client = Client(account_sid, auth_token)

message = client.messages.create(
            to=to_number, 
                from_=from_number,
                    body=body_msg)

print(message.sid)

