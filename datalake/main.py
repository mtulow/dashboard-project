import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    print("Azure Blob Storage Python quickstart sample")
    # account_url = "https://<storageaccountname>.blob.core.windows.net"
    # default_credential = DefaultAzureCredential()

    # # Create the BlobServiceClient object
    # blob_service_client = BlobServiceClient(account_url, credential=default_credential)
    

    # Quickstart code goes here

except Exception as ex:
    print('Exception:')
    print(ex)