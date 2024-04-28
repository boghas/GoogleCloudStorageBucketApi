import os
import shutil
import logging
from dotenv import load_dotenv
from smth import smth

if __name__ == "__main__":
    # This loads the environment variables from the .env file
    load_dotenv()  
    bucket_name = os.environ.get('BUCKET_NAME')

    smth.load_credentials()

    print(smth.list_bucket_files(bucket_name))

