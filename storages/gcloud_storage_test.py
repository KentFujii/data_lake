import pytest
import requests
import urllib3
import json
from storages.gcloud_storage import GcloudStorage

class TestGcloudStorage(object):
    @classmethod
    def setup_class(cls):
        cls.storage = GcloudStorage()

    def setup_method(self):
        my_http = requests.Session()
        my_http.verify = False
        urllib3.disable_warnings(
            urllib3.exceptions.InsecureRequestWarning
        )
        headers = {'Content-Type': 'text/plain'}
        data = "a text content is here"
        my_http.post('https://fake-gcs-server:4443/upload/storage/v1/b/data_lake_test/o?uploadType=media&name=sample.txt', headers=headers, data=data)


    def teardown_method(self):
        my_http = requests.Session()
        my_http.verify = False
        urllib3.disable_warnings(
            urllib3.exceptions.InsecureRequestWarning
        )
        get_req = my_http.get('https://fake-gcs-server:4443/storage/v1/b/data_lake_test/o')
        get_body = json.loads(get_req.text)
        item_names = [item['name'] for item in get_body['items']]
        for item_name in item_names:
            my_http.delete('https://fake-gcs-server:4443/storage/v1/b/data_lake_test/o/{item_name}'.format(item_name=item_name))

    def test_list(self):
        object_count = len(self.storage.list(""))
        assert object_count == 1

    def test_put(self):
        self.storage.put('test.json', json.dumps({'test_key': 'test_value'}))
        pass

    # def test_get(self):
    #     pass

    # def test_delete(self):
    #     pass
