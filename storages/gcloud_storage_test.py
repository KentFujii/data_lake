import pytest
import requests
import urllib3
import json
from gcloud_storage import GcloudStorage

class TestGcloudStorage(object):
    @classmethod
    def setup_class(cls):
        cls.storage = GcloudStorage()

    def setup_method(self):
        data = "a text content is here"
        requests.post('http://fake-gcs-server:4443/upload/storage/v1/b/data_lake_test/o?uploadType=media&name=sample.txt', data=data)


    def teardown_method(self):
        get_req = requests.get('http://fake-gcs-server:4443/storage/v1/b/data_lake_test/o')
        get_body = get_req.json()
        item_names = [item['name'] for item in get_body['items']]
        for item_name in item_names:
            requests.delete('http://fake-gcs-server:4443/storage/v1/b/data_lake_test/o/{item_name}'.format(item_name=item_name))

    def test_list(self):
        object_count = len(self.storage.list(""))
        assert object_count == 1

    def test_put(self):
        putting_json = {'test_key': 'test_value'}
        self.storage.put('test.json', json.dumps(putting_json))
        putted_json = requests.get('http://fake-gcs-server:4443/storage/v1/b/data_lake_test/o/test.json?alt=media').json()
        assert putted_json == putting_json

    def test_get(self):
        sample_text = self.storage.get('sample.txt')
        assert sample_text == "a text content is here"

    def test_delete(self):
        self.storage.delete('sample.txt')
        get_req = requests.get('http://fake-gcs-server:4443/storage/v1/b/data_lake_test/o')
        get_json = get_req.json()
        object_count = len(get_json['items'])
        assert object_count == 0
