import os
import requests
import urllib.parse

class TwitterClient(object):
    def __init__(self):
        TWITTER_ACCESS_KEY = os.getenv("TWITTER_ACCESS_KEY")
        TWITTER_SECRET_KEY = os.getenv("TWITTER_SECRET_KEY")
        auth = (TWITTER_ACCESS_KEY, TWITTER_SECRET_KEY)
        data = {"grant_type": "client_credentials"}
        bearer = requests.post('https://api.twitter.com/oauth2/token', auth=auth, data=data).json()
        self.token = bearer['access_token']

    def fetch(self):
        headers = {'Authorization': "Bearer {token}".format(token=self.token)}
        query = urllib.parse.quote('西荻')
        url = "https://api.twitter.com/1.1/search/tweets.json?q={query}&count=100".format(query=query)
        requests.get(url, headers=headers).json()
        pass

    def load(self):
        pass
