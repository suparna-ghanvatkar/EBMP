

from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "AC937af250fc201a2c44aad667cf309fa4"
AUTH_TOKEN = "6a8accce5860c8f18391bf4ec809d84b"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

	
def getVars(var1,var2,var3):
	message = client.messages.create(
	    body=var1,
	    to=var2,
	    from_=var3,
	)

getVars(one,two,three)




