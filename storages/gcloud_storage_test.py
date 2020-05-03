import pytest
import requests
import urllib3
from storages.gcloud_storage import GcloudStorage

class TestGcloudStorage(object):
    @classmethod
    def setup_class(cls):
        cls.storage = GcloudStorage()

    def setup_method(self):
        # curl --insecure -X POST -H "Content-Type: text/plain" "https://fake-gcs-server:4443/upload/storage/v1/b/data_lake_test/o?uploadType=media&name=test.txt"
        my_http = requests.Session()
        my_http.verify = False
        urllib3.disable_warnings(
            urllib3.exceptions.InsecureRequestWarning
        )
        headers = {'Content-Type': 'text/plain'}
        data = "a text content is here"
        my_http.post('https://fake-gcs-server:4443/upload/storage/v1/b/data_lake_test/o?uploadType=media&name=test.txt', headers=headers, data=data)


    def teardown_method(self):
        # delete object
        # curl --insecure https://fake-gcs-server:4443/storage/v1/b/data_lake_test/o
        # curl --insecure -X DELETE https://fake-gcs-server:4443/storage/v1/b/data_lake_test/o/readme.md
        # my_http = requests.Session()
        # my_http.verify = False
        # urllib3.disable_warnings(
        #     urllib3.exceptions.InsecureRequestWarning
        # )
        # headers = {'Content-Type': 'text/plain'}
        # my_http.post('https://fake-gcs-server:4443/upload/storage/v1/b/data_lake_test/o?uploadType=media&name=test.txt', headers=headers)

    def test_list(self):
        assert len(self.storage.list("")) == 1

    # def test_put(self):
    #     storage = GcloudStorage()
    #     content = storage.put('readme.md')
    #     assert content == None

    # def test_get(self):
    #     pass

    # def test_delete(self):
    #     pass
