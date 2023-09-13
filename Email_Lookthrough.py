import pyautogui # Used primarily for message/confirm boxes
import pymsgbox # Formatting for confirm boxes
import time # Used for sleeping
import msal
from msal import PublicClientApplication
import webbrowser

# ---------------- Connecting to Microsoft Graph API ----------------------
APPLICATION_ID = '206eb2cb-a1da-4638-b98d-a5105b2dc36c'
CLIENT_SECRET = ''
authority_url = 'https://login.microsoftonline.com/consumers/'
base_url = 'https://graph.microsoft.com/v1.0/'

endpoint = base_url + 'me'
SCOPES = ['User.Read', 'Mail.Read'] # 'Mail.Read', 'Mail.Read.Shared', 'Mail.ReadBasic', 'Mail.ReadBasic.Shared', 

# ---------------- Login to Acquire Access Token ----------------------
app = PublicClientApplication(
    APPLICATION_ID,
    authority = authority_url
)

# accounts = app.get_accounts()
# if accounts:
#     app.acquire_token_silent(scopes=SCOPES, account=accounts[0])

flow = app.initiate_device_flow(scopes=SCOPES)
print(flow)
print(flow['message'])
webbrowser.open(flow['verification_uri'])