import os
import requests
import urllib3
from google.api_core.client_options import ClientOptions
from google.auth.credentials import AnonymousCredentials
from google.cloud import storage
from google.cloud.storage.blob import Blob

class GcloudStorage:
    def __init__(self):
        GCS_EXTERNAL_URL = os.getenv("GCS_EXTERNAL_URL", "http://fake-gcs-server:4443")
        GCS_PUBLIC_HOST = os.getenv("GCS_PUBLIC_HOST", "http://storage.gcs.fake-gcs-server.nip.io:4443")
        GCS_DEFAULT_BUCKET = os.getenv("GCS_DEFAULT_BUCKET", "data_lake_test")
        storage.blob._API_ACCESS_ENDPOINT = GCS_PUBLIC_HOST
        storage.blob._DOWNLOAD_URL_TEMPLATE = u"%s/download/storage/v1{path}?alt=media" % GCS_EXTERNAL_URL
        storage.blob._BASE_UPLOAD_TEMPLATE = u"%s/upload/storage/v1{bucket_path}/o?uploadType=" % GCS_EXTERNAL_URL
        storage.blob._MULTIPART_URL_TEMPLATE = storage.blob._BASE_UPLOAD_TEMPLATE + u"multipart"
        storage.blob._RESUMABLE_URL_TEMPLATE = storage.blob._BASE_UPLOAD_TEMPLATE + u"resumable"
        self.client = storage.Client(
            credentials=AnonymousCredentials(),
            project="test",
            client_options=ClientOptions(api_endpoint=GCS_EXTERNAL_URL),
        )
        self.bucket = self.client.get_bucket(GCS_DEFAULT_BUCKET)

    def list(self, prefix):
        blobs = list(self.bucket.list_blobs(prefix=prefix))
        return [blob.name for blob in blobs]

    def put(self, object_name, object_string):
        blob = Blob(object_name, self.bucket)
        blob.upload_from_string(object_string)

    def get(self, object_name):
        blob = self.bucket.blob(object_name)
        return blob.download_as_string().decode('utf-8')

    def delete(self, object_name):
        blob = self.bucket.blob(object_name)
        blob.delete()
