#!/bin/python3

import authorization_flow

from utils import *
from googleapiclient.discovery import build

def get_photos_media_items(creds,
        output_file_name="stats_google_photos_media_items.csv",
        pageSize=100,
        delimiter=",,,,"):
    """
    Get all media items from google photos and write them to a file
    """
    with open(get_data_file_path(timestamp_prefix(output_file_name)), "w+") as writer:
        with build('photoslibrary', 'v1', credentials=creds, static_discovery=False) as service:
            photoslibrary_service = service.mediaItems()
            media_items_list_req = photoslibrary_service.list(
                pageSize=pageSize,
            )
            success = 0
            failure = 0
            writer.write(f"id{delimiter}mime_type{delimiter}name{delimiter}creation_time(Windows_Media_Created_time_or_Windows_modified_time){delimiter}product_url\n")
            while media_items_list_req is not None:
                media_items_dict = media_items_list_req.execute()
                # print(json.dumps(media_items_dict, sort_keys=True, indent=4))
                try:
                    items = media_items_dict["mediaItems"]
                    for item in items:
                        try:
                            mime_type = item["mimeType"]
                            id = item["id"]
                            product_url = item["productUrl"]
                            name = item["filename"]
                            creation_time = item["mediaMetadata"]["creationTime"]
                            line = f"{id}{delimiter}{mime_type}{delimiter}{name}{delimiter}{creation_time}{delimiter}{product_url}\n"
                            writer.write(line)
                            success+=1
                        except Exception as e:
                            print(f"Exception: '{e}' Skipping item '{item}'")
                            failure+=1
                except Exception as e:
                    pass
                media_items_list_req = photoslibrary_service.list_next(media_items_list_req, media_items_dict)
                print(f"Google Photos media items processed successfully/failed: {success}/{failure}")
    
def photos_media_items():
    """
    Wrapper to get all photos media items info
    """
    client_secrets_file = get_sensitive_file_path("./client_secrets.json")
    authorised_creds_file = get_sensitive_file_path("authorised_creds_photoslibrary.json")
    creds = authorization_flow.get_creds(
        client_secrets_file=client_secrets_file,
        scopes=["https://www.googleapis.com/auth/photoslibrary.readonly"],
        authorised_creds_file=authorised_creds_file
    )
    get_photos_media_items(creds=creds)

def get_drive_files(creds,
        output_file_name="stats_google_drive_files.csv",
        pageSize=1000,
        delimiter=",,,,"):
    """
    Get all files from google drive and write them to a file
    """
    with open(get_data_file_path(timestamp_prefix(output_file_name)), "w+") as writer:
        with build('drive', 'v3', credentials=creds) as service:
            drive_files_api = service.files()
            files_list_req = drive_files_api.list(
                pageSize=pageSize, 
                q="mimeType!='application/vnd.google-apps.folder'",
                fields="files(id,name,createdTime,modifiedTime,size,kind,webViewLink,mimeType),nextPageToken"
            )
            success = 0
            failure = 0
            writer.write(f"kind{delimiter}id{delimiter}mime_type{delimiter}name{delimiter}created_time{delimiter}modified_time{delimiter}size{delimiter}web_view_link\n")
            while files_list_req is not None:
                files_dict = files_list_req.execute()
                # print(json.dumps(files_dict, sort_keys=True, indent=4))
                try:
                    items = files_dict["files"]
                    for item in items:
                        try:
                            mime_type = item["mimeType"]
                            id = item["id"]
                            web_view_link = item["webViewLink"]
                            name = item["name"]
                            kind = item["kind"]
                            created_time = item["createdTime"]
                            modified_time = item["modifiedTime"]
                            size = item["size"]
                            line = f"{kind}{delimiter}{id}{delimiter}{mime_type}{delimiter}{name}{delimiter}{created_time}{delimiter}{modified_time}{delimiter}{size}{delimiter}{web_view_link}\n"
                            writer.write(line)
                            success+=1
                        except Exception as e:
                            print(f"Exception: '{e}' Skipping item '{item}'")
                            failure+=1
                except Exception as e:
                    pass
                files_list_req = drive_files_api.list_next(files_list_req, files_dict)
                print(f"Drive Files processed successfully/failed: {success}/{failure}")


def drive_files():
    """
    Wrapper to get all drive files info
    """
    client_secrets_file = get_sensitive_file_path("./client_secrets.json")
    authorised_creds_file = get_sensitive_file_path("authorised_creds_drive.json")
    creds = authorization_flow.get_creds(
        client_secrets_file=client_secrets_file,
        scopes=["https://www.googleapis.com/auth/drive.readonly"],
        authorised_creds_file=authorised_creds_file
    )
    get_drive_files(creds=creds)


if __name__ == "__main__":
    photos_media_items()
    drive_files()
