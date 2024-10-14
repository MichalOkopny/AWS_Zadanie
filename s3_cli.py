import os
import re
import boto3
import argparse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

BUCKET_NAME = "developer-task"
PREFIX = "y-wing"

def list_files():
    """List all files in the S3 bucket."""
    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=PREFIX)
    if 'Contents' in response:
        for item in response['Contents']:
            print(item['Key'])
    else:
        print("No files found.")

def upload_file(file_path, destination_path):
    """Upload a local file to a defined location."""
    try:
        s3.upload_file(file_path, BUCKET_NAME, f"{PREFIX}/{destination_path}")
        print(f"Uploaded {file_path} to {PREFIX}/{destination_path} in {BUCKET_NAME}")
    except Exception as e:
        print(f"Failed to upload {file_path}: {e}")

def list_files_with_filter(pattern):
    """List files matching a regex pattern."""
    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=PREFIX)
    regex = re.compile(pattern)
    if 'Contents' in response:
        for item in response['Contents']:
            if regex.search(item['Key']):
                print(item['Key'])
    else:
        print("No files found.")

def delete_files_with_filter(pattern):
    """Delete all files matching a regex pattern."""
    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=PREFIX)
    regex = re.compile(pattern)
    to_delete = [{'Key': item['Key']} for item in response.get('Contents', []) if regex.search(item['Key'])]

    if to_delete:
        s3.delete_objects(Bucket=BUCKET_NAME, Delete={'Objects': to_delete})
        print("Deleted files:", [item['Key'] for item in to_delete])
    else:
        print("No matching files to delete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="S3 CLI Tool")
    parser.add_argument("--list", action="store_true", help="List all files in the S3 bucket")
    parser.add_argument("--upload", nargs=2, metavar=('file_path', 'destination_path'), help="Upload a file to the S3 bucket")
    parser.add_argument("--filter-list", help="List files matching a regex pattern")
    parser.add_argument("--delete", help="Delete files matching a regex pattern")

    args = parser.parse_args()

    if args.list:
        list_files()
    elif args.upload:
        upload_file(args.upload[0], args.upload[1])
    elif args.filter_list:
        list_files_with_filter(args.filter_list)
    elif args.delete:
        delete_files_with_filter(args.delete)
    else:
        parser.print_help()
