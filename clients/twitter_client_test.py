import pytest
from clients.twitter_client import TwitterClient

class TestTwitterClient(object):
    @classmethod
    def setup_class(cls):
        cls.client = TwitterClient()

    def test_fetch(self):
        self.client.fetch()
        pass

    def test_load(self):
        pass
