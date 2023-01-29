import os

from datetime import datetime

def timestamp_prefix(text):
    """
    Format output file name to have timestamp at the start
    """
    return f"{datetime.now().strftime('%Y%m%dT%H%M%S')}_{text}"

def get_data_dir():
    """
    Return the data directory for data files
    """
    return os.path.join(os.getcwd(),"data")

def get_data_file_path(filename):
    """
    Return the full file path for a file that is to be placed in the data
    directory
    """
    return os.path.join(get_data_dir(), filename)

def get_sensitive_dir():
    """
    Return the directory for sensitive data
    """
    return os.path.join(os.getcwd(),"sensitive")

def get_sensitive_file_path(filename):
    """
    Return the full file path for a file that is to be placed in the sensitive
    directory
    """
    return os.path.join(get_sensitive_dir(), filename)