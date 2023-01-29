import pandas as pd
import datetime, os

from os import listdir
from os.path import isfile, join
from os import walk

pd.set_option('display.max_colwidth', None)

df_r = pd.read_csv('20230129-105213-file-stats-google-images-images.csv', sep=",,,,", engine='python')
df_l = pd.read_csv('20230129-071906-file-stats-mnt-p-Backup.csv', sep=",,,,", engine='python')

for index, row in df_l.iterrows():
    modified_time_l = datetime.datetime.strptime(row["local_modified_time"], "%Y-%m-%dT%H:%M:%S.%f").date()
    created_time_l = datetime.datetime.strptime(row["local_created_time"], "%Y-%m-%dT%H:%M:%S.%f").date()
    file_dir_l = row["local_file_dir"]
    file_name_l = row["local_file_name"]
    file_path = os.path.join(file_dir_l,file_name_l)

    try:
        df_filtered = df_r.loc[df_r['name'] == file_name_l]
        df_values = df_filtered['creation_time(Windows_Media_Created_time_or_Windows_modified_time)'].values
        if len(df_filtered) > 1:
            print("--------------------------------------------------")
            print("Multiple Entries found")
            print(df_filtered)
            print("--------------------------------------------------")

        df_value = df_values[0]
        remote_creation_time = datetime.datetime.strptime(
            df_value,
            '%Y-%m-%dT%H:%M:%SZ'
        ).date()
    except IndexError as ie:
        print(f"IndexError: Cant find local file on remote location, skipping: '{file_path}'")
        continue
    except Exception as e:
        print(f"Exception: {e} - Skipping '{file_path}'")
        continue

    timediff = (modified_time_l - remote_creation_time).days
    print(f"[{modified_time_l} - {remote_creation_time}] = {timediff:<5}: '{file_name_l}'")
