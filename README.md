# Google APy

Basically, Google Developer API sample code. 

Point was for me to get data from Google Photos (and maybe Google Drive) and compare it with my local media files to see if the timestamps matched up. For some they didnt as Google seems to use the `Media Created` stamp from Windows for some files and the last `Modified Times` for when the former is not present.

However figuring out how to extract the `Media Created` was too much effort for me at the moment so I ended up just writing code to pull all the relevant data from my local data and the remote (Google Photos and Drive) data and just storing that on Drive itself as something that I can refer to if I really want to verify dates.

I would like to continue on this later at some point, in the mean time please feel free to tinker around and add stuff if you know how to get the `Media Created` stamp somehow from Windows easily using python.

Also figuring this out was a pain, so hopefully this sample code helps someone.

# How to run

## Prerequisite steps

- Create a project on the [Google Developer Console](https://console.cloud.google.com/apis/dashboard) and an OAuth consent screen
    - Get added as a test user (in the consent screen settings) to be able to use the consent screen
- Enable the relevant APIs (`Drive API` and `Photos API`)
- Create an `OAuth client ID` with `Application type` as `Desktop app`
    - Download the json file and place it in the `sensitive` directory with the name `client_secrets.json`

## Setup the env
- [Setup a virtual env](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) called `env`

    ```
    sudo apt install python3.8-venv
    python3 -m pip install --user --upgrade pip
    python3 -m pip --version
    python3 -m venv env
    source env/bin/activate
    which python
    ```
- Install the requirements with `pip install -r requirements.txt`

## Running the code

- Run `./runner.sh google_apy.py`
    - This will gather data from your Google Drive and Google Photos and put it into the `data` directory

- For `local_file_stats.py`
    - Open `local_file_stats.py`
    - Change the `mypaths` var to point to the directory you wish to get information about
    - Run `./runner.sh local_file_stats.py`
    - NOTE: Not really cleaned up nor designed well

- For `compare.py`
    - Change the file names for `df_r` and `df_l` (remote and local respectively)
    - These files will be "compared"
    - NOTE: Not really cleaned up nor designed well

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
