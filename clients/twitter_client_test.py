import pytest
from clients.twitter_client import TwitterClient

class TestTwitterClient(object):
    @classmethod
    def setup_class(cls):
        cls.client = TwitterClient()

    def test_fetch(self):
        self.client.fetch()
        response = self.client.data
        assert response['statuses'][0]['id'] == 1257966732230013000

    def test_load(self):
        self.client.data = {'test_key': 'test_value'}
        assert self.client.load() == '{"test_key": "test_value"}'
