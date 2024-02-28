from google.cloud import storage
import os

"""
Pre-reqs: 
1. `pip install pandas pyarrow google-cloud-storage`
2. Set GOOGLE_APPLICATION_CREDENTIALS to your project/service-account key
   export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
3. Set GCP_GCS_BUCKET as your bucket or change default value of BUCKET
"""

# switch out the bucketname
BUCKET = os.environ.get("GCP_GCS_BUCKET", "week-5")

file_name = "./2024-02-26/Names_12:13:15.csv"

def upload_to_gcs(bucket, destination_blob_name, source_file_name):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    """
    # # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # # (Ref: https://github.com/googleapis/python-storage/issues/74)
    # storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    # storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB

    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

upload_to_gcs(BUCKET, f"csv_data/Names_03_39_35.csv", "./2024-02-27/Names_03_39_35.csv")

