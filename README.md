# AWS S3 CLI Tool

## Project Description

The AWS S3 CLI Tool is a simple command-line interface (CLI) written in Python that allows users to interact with the Amazon S3 service. This tool enables basic operations on files in an S3 bucket, including:

- Listing all files in the bucket.
- Uploading local files to a specified location in the bucket.
- Listing files in the bucket that match a provided regex pattern.
- Deleting all files that match a regex pattern from the bucket.

## Requirements

- Python 3.x
- `boto3` library
- `python-dotenv` library

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/MichalOkopny/AWS_Zadanie.git
   cd AWS_Zadanie
     # Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
   
   pip install boto3 python-dotenv

  ## Usage
    ```bash
    python s3_cli.py

the command-line interface allows you to choose one of the following options:

List all files - Displays all files in the S3 bucket under the prefix y-wing/.
Upload file - Uploads a local file to the bucket.
List files matching regex - Displays files in the bucket that match a provided regex pattern.
Delete files matching regex - Deletes files from the bucket that match a provided regex pattern.
Exit - Closes the program.

