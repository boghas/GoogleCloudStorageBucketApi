import os
from google.cloud import storage
from google.cloud.exceptions import NotFound
from google.cloud.exceptions import Forbidden


def list_bucket_files(storage_client: storage.Client, bucket_name: str, directory=None | str) -> list:
    blobs = storage_client.list_blobs(bucket_name)
    if directory is not None:
        file_names = [file.name for file in blobs if directory in file.name]
    else:
        file_names = [file.name for file in blobs]

    return file_names


def download_blobs(storage_client: storage.Client, bucket_name: str, blobs_list: list, local_download_dir='') -> None:
    try:
        bucket = storage_client.get_bucket(bucket_name)

        for blob in blobs_list:
            blob = bucket.blob(blob)
            blob.download_to_filename(os.path.join(local_download_dir, os.path.basename(blob.name)))
            print(f'Successfully downloaded {blob.name} to {os.path.join(local_download_dir, os.path.basename(blob.name))}')
    except NotFound:
        print('Bucket not found!')
    except Forbidden:
        print('You do not have permissions to perform this action!')


