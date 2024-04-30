import os
import shutil
import logging
from dotenv import load_dotenv
from api import api
from server import server
from google.cloud import storage


if __name__ == "__main__":
    # This loads the environment variables from the .env file
    load_dotenv()
    GOOGLE_APPLICATION_CREDENTIALS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")  
    bucket_name = os.environ.get('BUCKET_NAME')
    bucket_dir = os.environ.get('BUCKET_DIR')
    local_download_path = os.environ.get('LOCAL_DIR')
    hostname = os.environ.get('SFTP_HOSTNAME')
    username = os.environ.get('SFTP_USERNAME')
    password = os.environ.get('SFTP_PASSWORD')
    port = os.environ.get('SFTP_PORT')
    remote_dir = os.environ.get('SFTP_DIR')

    # Setup the client
    storage_client = storage.Client()

    files = api.list_bucket_files(storage_client, bucket_name, bucket_dir)

    api.download_and_delete_blobs(storage_client, bucket_name, files, local_download_path)

    sftp = server.connect_to_sftp(hostname, username, password, int(port))

    for file in os.listdir(local_download_path):
        file_path = os.path.join(local_download_path, file)
        try:
            server.upload_file(sftp, file_path, remote_dir)
            os.remove(file_path)
        except Exception as e:
            print(e)

