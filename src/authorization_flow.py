import pickle
import os

from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

def auth_req(client_secrets_file, scopes):
    """
    Return the Credentials Object obtained from the Installed App OAuth flow

    Link to auth page shown in stdout
    """
    flow = InstalledAppFlow.from_client_secrets_file(
        client_secrets_file,
        scopes=scopes)
    # the server is how you can grant access
    return flow.run_local_server(open_browser=False, port=0)

def save_auth_creds(creds, pickled_filename):
    """
    Save creds into a file to avoid repeated requests
    """
    with open(pickled_filename, 'w') as token:
        token.write(creds.to_json())
    return pickled_filename


def get_creds(client_secrets_file, scopes, authorised_creds_file):
    """
    Get credentials from Google using oauth or use existing ones
    Based on https://developers.google.com/drive/api/quickstart/python
    """

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(authorised_creds_file):
        creds = Credentials.from_authorized_user_file(
            authorised_creds_file,
            scopes
        )
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = auth_req(
                client_secrets_file=client_secrets_file,
                scopes=scopes
            )
        save_auth_creds(creds, authorised_creds_file)
    return creds
