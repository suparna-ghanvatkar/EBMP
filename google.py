
import httplib2

from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow

# List the scopes your app requires:
SCOPES = ['https://www.googleapis.com/auth/plus.me',
          'https://www.googleapis.com/auth/plus.stream.write']

# The following redirect URI causes Google to return a code to the user's
# browser that they then manually provide to your app to complete the
# OAuth flow.
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

# For a breakdown of OAuth for Python, see
# https://developers.google.com/api-client-library/python/guide/aaa_oauth
# CLIENT_ID and CLIENT_SECRET come from your Developers Console project
flow = OAuth2WebServerFlow(client_id='326569337916-55hcpfg6neo15mgjoqb0psj684gd6prt.apps.googleusercontent.com',
                           client_secret='NJDsDmDrc1I0vncv1N3nWmxa',
                           scope=SCOPES,
                           redirect_uri=REDIRECT_URI)

auth_uri = flow.step1_get_authorize_url()

# This command-line server-side flow example requires the user to open the
# authentication URL in their browser to complete the process. In most
# cases, your app will use a browser-based server-side flow and your
# user will not need to copy and paste the authorization code. In this
# type of app, you would be able to skip the next 3 lines.
# You can also look at the client-side and one-time-code flows for other
# options at https://developers.google.com/+/web/signin/
print 'Please paste this URL in your browser to authenticate this program.'
print auth_uri
code = raw_input('Enter the code it gives you here: ')

# Set authorized credentials
credentials = flow.step2_exchange(code)

# Create a new authorized API client.
http = httplib2.Http()
http = credentials.authorize(http)
service = build('plusDomains', 'v1', http=http)


# This sample assumes a client object `service` has been created and
# that the user you want to retrieve a list of posts for is an
# authenticated user.
# To learn more about creating a client, see the OAuth 2.0 example:
#  https://developers.google.com/+/domains/authentication/

user_id = 'me'
print "hello"
activities_service = service.activities()
request = activities_service.list(
    userId=user_id,
    collection='user',
    maxResults='2')

while request is not None:
  activities_document = request.execute()
  if activities_document.get('items') is not None:
    print 'got page with %d' % len(activities_document.get('items'))
    for activity in activities_document.get('items'):
      print activity.get('id'), activity.get('object').get('content')

  request = activities_service.list_next(request, activities_document)


