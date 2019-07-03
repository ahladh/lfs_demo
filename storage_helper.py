import boto3
import botocore
import os
from azure.storage.blob import BlockBlobService
import json


BUCKET_NAME = 'swatapplicationsample' 

def download_file(key):
    if(os.getenv("CLOUD_STORAGE_TYPE"), 'aws') == 'aws':
        download_file_from_s3(key)
    else:
        download_file_from_azure(key)


def download_file_from_s3(key):
    s3 = boto3.resource('s3')
    try:
        s3.Bucket(BUCKET_NAME).download_file(key, key)
        
    except botocore.exceptions.ClientError as e:
        print(e)
        raise


def download_file_from_azure(key):
    acc_name = os.getenv("AZURE_ACCOUNT_NAME", 'swat2')
    acc_key = os.getenv("AZURE_ACCOUNT_KEY", 'CisexzKX/AOweP2v3dFw0hDIKs5K9HQjKGw1GVcuJrj5LMLjmCArBc/AU+Dpuqw+7IMDQ+JlSsuox27UFzcZzw==')
    client = BlockBlobService(account_name=acc_name, account_key=acc_key)
    client.get_blob_to_path('imageprocessing', key, key)
    




