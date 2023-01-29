#!/bin/python3

import datetime, os

from utils import timestamp_prefix

mypaths = [
    "/mnt/p/Backup"
]

for mypath in mypaths:
    print("Path: ", mypath)
    path = os.path.normpath(mypath)

    suffix = "_".join(path.split(os.sep))
    writer_file_name = timestamp_prefix(f"stats_local_files{suffix}.csv")
    with open(writer_file_name, "w") as writer:
        DELIMITER=",,,,"
        writer.write(f"local_modified_time{DELIMITER}local_created_time{DELIMITER}local_file_dir{DELIMITER}local_file_name\n")
        for dirpath, subdirs, files in os.walk(mypath):
            for x in files:
                local_file_path = os.path.join(dirpath, x)
                local_file_name = os.path.basename(local_file_path)
                local_file_dir = os.path.dirname(local_file_path)
                local_created_time = datetime.datetime.fromtimestamp(os.path.getmtime(local_file_path)).isoformat(sep="T", timespec="milliseconds")
                local_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(local_file_path)).isoformat(sep="T", timespec="milliseconds")
                writer.write(f"{local_modified_time}{DELIMITER}{local_created_time}{DELIMITER}{local_file_dir}{DELIMITER}{local_file_name}\n")

