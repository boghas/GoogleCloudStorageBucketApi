import os
from google.cloud import storage
#from google.oauth2 import service_account



def load_credentials():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'credentials\duag-masc-stg-01-ops.json'


def list_bucket_files(bucket_name: str) -> list:
    storage_client = storage.Client()

    blobs = storage_client.list_blobs(bucket_name)
    file_names = [file.name for file in blobs]

    return file_names


# duag-masc-stg-01-ops-scireports
