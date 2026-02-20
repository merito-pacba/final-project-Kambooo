from azure.storage.blob import BlobServiceClient
import uuid
import os

def upload_image_to_blob(file):
    blob_service = BlobServiceClient.from_connection_string(
        os.environ["AZURE_STORAGE_CONNECTION_STRING"]
    )

    container_client = blob_service.get_container_client(
        os.environ.get("AZURE_CONTAINER_NAME", "media")
    )

    blob_name = f"{uuid.uuid4()}-{file.name}"
    blob_client = container_client.get_blob_client(blob_name)

    blob_client.upload_blob(file, overwrite=True)

    return blob_client.url