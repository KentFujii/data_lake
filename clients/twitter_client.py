import os
import requests
from requests.auth import HTTPBasicAuth
import urllib.parse

class TwitterClient(object):
    def __init__(self):
        self.endpoint = os.getenv("TWITTER_ENDPOINT", "http://apisprout:8000")
        TWITTER_ACCESS_KEY = os.getenv("TWITTER_ACCESS_KEY", "data_lake")
        TWITTER_SECRET_KEY = os.getenv("TWITTER_SECRET_KEY", "password")
        auth = HTTPBasicAuth(TWITTER_ACCESS_KEY, TWITTER_SECRET_KEY)
        data = {"grant_type": "client_credentials"}
        bearer = requests.post(self.endpoint + '/oauth2/token', auth=auth, data=data).json()
        self.token = bearer['access_token']

    def fetch(self):
        headers = {'Authorization': "Bearer {token}".format(token=self.token)}
        query = urllib.parse.quote('西荻')
        url = self.endpoint + "/1.1/search/tweets.json?q={query}&count=100".format(query=query)
        requests.get(url, headers=headers).json()
        pass

    def load(self):
        pass
