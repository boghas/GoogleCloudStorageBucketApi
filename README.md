# GoogleCloudStorageBucketApi

## TO RUN 

* STEP 1 INSTALL DEPENDENCIES *
cd GoogleCloudStorageBucketApi
pip install -r requirements.txt

* STEP 2 SETUP LOCAL ENVIRONMENT *
create a .env file adding the following environment variables:
GOOGLE_APPLICATION_CREDENTIALS=path_to_your_credentials_file.json -> MANDATORY
BUCKET_NAME=your_bucket_name -> MANDATORY
BUCKET_DIR=your_bucket_directory -> the directory in the bucket where the files are placed. Can be empty, in this case it will look in the root directory of the bucket, gathering all files including the files from subdirectories.
LOCAL_DIR=your_local_directory -> the local directory where the files should be downloaded. Can be empty, in this case it will download the files into the directory where the script is ran from.

* STEP 3 RUN THE SCRIPT *
python main.py