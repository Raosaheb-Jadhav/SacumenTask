# Sacumen

SacumenTask is a Python module for uploading files to AWS S3 and Google Cloud Storage. 
It provides a simple interface for uploading images and documents to the respective cloud storage services.

## Installation

Install Sacumen using pip:

```bash
pip install sacumen-0.1.tar.gz
```

## Usage
```
from sacumen.uploader import upload_files

directory_path = '/path/to/your/files'
aws_access_key = 'your_aws_access_key'
aws_secret_key = 'your_aws_secret_key'
aws_bucket_name = 'your_s3_bucket_name'
gcs_project_id = 'your_google_cloud_project_id'
gcs_bucket_name = 'your_gcs_bucket_name'

s3_file_types = ['jpg', 'png', 'svg', 'webp']
gcs_file_types = ['doc', 'docx', 'csv', 'pdf']

upload_files(directory_path=directory_path,
             aws_access_key=aws_access_key,
             aws_secret_key=aws_secret_key,
             aws_bucket_name=aws_bucket_name,
             gcs_project_id=gcs_project_id,
             gcs_bucket_name=gcs_bucket_name,
             s3_file_types=s3_file_types,
             gcs_file_types=gcs_file_types)
```
# Configuration
You can customize the types of files to transfer to S3 and Google Cloud Storage by specifying the s3_file_types and gcs_file_types parameters when calling upload_files.

# Dependencies
google-cloud-storage
boto3
