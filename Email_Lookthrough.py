import pyautogui # Used primarily for message/confirm boxes
import pymsgbox # Formatting for confirm boxes
import time # Used for sleeping
import msal
from msal import PublicClientApplication

# ---------------- Connecting to Microsoft Graph API ----------------------
APPLICATION_ID = '206eb2cb-a1da-4638-b98d-a5105b2dc36c'
CLIENT_SECRET = ''
authority_url = 'https://login.microsoftonline.com/consumers/'
base_url = 'https://graph.microsoft.com/v1.0/'

endpoint = base_url + 'me'
SCOPES = ['Mail.Read', 'Mail.Read.Shared', 'Mail.ReadBasic', 'Mail.ReadBasic.Shared', 'User.Read']

