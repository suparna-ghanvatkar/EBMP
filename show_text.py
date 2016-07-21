from datetime import date
from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "AC937af250fc201a2c44aad667cf309fa4"
AUTH_TOKEN = "6a8accce5860c8f18391bf4ec809d84b"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

for message in client.messages.list():
    message.body

def filtering(to_txt):
	messages = client.messages.list(
    	to=to_txt,
    	date_sent=date(2015,1,8),
	)

	for message in messages:
	    return message.body


#filtering(mbl_no)
