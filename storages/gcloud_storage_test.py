import pytest
import requests
from storages.gcloud_storage import GcloudStorage

class TestGcloudStorage(object):
    ## TODO: setup fixture with json api
    # https://github.com/fsouza/fake-gcs-server
    # https://cloud.google.com/storage/docs/json_api/v1?hl=ja
    @classmethod
    def setup_class(cls):
        # initialize storage class
        print('setup_class')

    @classmethod
    def teardown_class(cls):
        # delete bucket
        # curl --insecure https://fake-gcs-server:4443/storage/v1/b
        # curl --insecure -X DELETE https://fake-gcs-server:4443/storage/v1/b/data_lake
        print('teardown_class')

    def setup_method(self):
        # create object
        import pdb; pdb.set_trace()
        headers = {
            'Accept': 'application/json',
        }
        data = '{"auth":{"passwordCredentials":{"username":"useruser","password":"passpasspass"},"tenantId":"123456789123456789"}}'
        response = requests.post('https://identity.tyo2.conoha.io/v2.0/tokens', headers=headers, data=data)
        print(response.text)
        print('setup_method')

    def teardown_method(self):
        # delete object
        # curl --insecure https://fake-gcs-server:4443/storage/v1/b/data_lake/o
        # curl --insecure -X DELETE https://fake-gcs-server:4443/storage/v1/b/data_lake/o/readme.md
        print('teardown_method')

    def test_list(self):
        storage = GcloudStorage()
        content = storage.put('readme.md')
        assert content == None

    def test_put(self):
        pass

    def test_get(self):
        pass

    def test_delete(self):
        pass
