import os
from pathlib import Path
from google.cloud import storage
import boto3

def upload_to_s3(aws_access_key, aws_secret_key, aws_bucket_name, file_path):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )

    with open(file_path, 'rb') as data:
        s3_client.upload_fileobj(data, aws_bucket_name, os.path.basename(file_path))

def upload_to_gcs(gcs_project_id, gcs_bucket_name, file_path):
    gcs_client = storage.Client(project=gcs_project_id)
    gcs_bucket = gcs_client.bucket(gcs_bucket_name)

    blob = gcs_bucket.blob(os.path.basename(file_path))
    blob.upload_from_filename(file_path)

def upload_files(directory_path, aws_access_key, aws_secret_key, aws_bucket_name, gcs_project_id, gcs_bucket_name,
                 s3_file_types=None, gcs_file_types=None):
    s3_file_types = s3_file_types or []
    gcs_file_types = gcs_file_types or []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = Path(file).suffix[1:].lower()

            if file_extension in s3_file_types:
                upload_to_s3(aws_access_key, aws_secret_key, aws_bucket_name, file_path)

            elif file_extension in gcs_file_types:
                upload_to_gcs(gcs_project_id, gcs_bucket_name, file_path)