# Google APy

Basically, Google Developer API sample code

# How to run

## Prerequisite steps

- Create a project on the [Google Developer Console](https://console.cloud.google.com/apis/dashboard) and an OAuth consent screen
    - Get added as a test user (in the consent screen settings) to be able to use the consent screen
- Enable the relevant APIs (`Drive API` and `Photos API`)
- Create an `OAuth client ID` with `Application type` as `Desktop app`
    - Download the json file and place it in the `sensitive` directory with the name `client_secrets.json`

## Running the code

- Install the requirements with `pip install -r /path/to/requirements.txt`
- Run `./runner.sh google_apy.py`
    - This will gather data from your Google Drive and Google Photos and put it into the `data` directory

## Directory structure

- `src`
    - Will contain source code
- `logs`
    - Logs will be output here from the `runner.sh` helper script
- `sensitive`
    - Sensitive files should be placed here (and will be by the code)
    - Place the `client_secret.json` file here
- `data`
    - Data produced by the code will be placed here

# Reference material

[google-api-python-client](https://github.com/googleapis/google-api-python-client/blob/main/docs/README.md)

[photoslibrary scopes](https://developers.google.com/photos/library/reference/rest/v1/mediaItems/list)

[driveapiv3 scopes](https://developers.google.com/drive/api/v3/reference/files/list)
