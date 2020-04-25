import os
import requests
import urllib3
from google.api_core.client_options import ClientOptions
from google.auth.credentials import AnonymousCredentials
from google.cloud import storage

EXTERNAL_URL = os.getenv("EXTERNAL_URL", "https://fake-gcs-server:4443")
PUBLIC_HOST = os.getenv("PUBLIC_HOST", "storage.gcs.fake-gcs-server.nip.io:4443")

storage.blob._API_ACCESS_ENDPOINT = "https://" + PUBLIC_HOST
storage.blob._DOWNLOAD_URL_TEMPLATE = (
    u"%s/download/storage/v1{path}?alt=media" % EXTERNAL_URL
)
storage.blob._BASE_UPLOAD_TEMPLATE = (
    u"%s/upload/storage/v1{bucket_path}/o?uploadType=" % EXTERNAL_URL
)
storage.blob._MULTIPART_URL_TEMPLATE = storage.blob._BASE_UPLOAD_TEMPLATE + u"multipart"
storage.blob._RESUMABLE_URL_TEMPLATE = storage.blob._BASE_UPLOAD_TEMPLATE + u"resumable"

my_http = requests.Session()
my_http.verify = False  # disable SSL validation
urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)  # disable https warnings for https insecure certs

client = storage.Client(
    credentials=AnonymousCredentials(),
    project="test",
    _http=my_http,
    client_options=ClientOptions(api_endpoint=EXTERNAL_URL),
)

bucket = client.get_bucket('sample-bucket')
blob = bucket.blob("some_file.txt")

content = blob.download_as_string()
print (content)
