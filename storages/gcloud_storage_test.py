import pytest
from storages.gcloud_storage import GcloudStorage

class TestGcloudStorage(object):
    ## TODO: setup fixture with json api
    # https://github.com/fsouza/fake-gcs-server
    # https://cloud.google.com/storage/docs/json_api/v1?hl=ja
    @classmethod
    def setup_class(cls):
        # create bucket
        cls.storage = GcloudStorage()
        print('setup_class')

    @classmethod
    def teardown_class(cls):
        # delete bucket
        print('teardown_class')

    def setup_method(self):
        # create object
        print(self.storage)
        print('setup_method')

    def teardown_method(self):
        # create object
        print('teardown_method')

    def test_crud(self):
        storage = GcloudStorage()
        content = storage.put('readme.md')
        assert content == None

    def test_purge(self):
        pass

# @pytest.mark.parametrize('site, current_url, expected_following_url, expected_indexing_url', [
#     (
#         'sumirin',
#         'https://rent.sumirin-residential.co.jp/list.php?',
#         'https://rent.sumirin-residential.co.jp/list.php?page=1',
#         'https://rent.sumirin-residential.co.jp/detail.php?id=680529'
#     ),
#     (
#         'miyazaki',
#         'https://www.miyazaki-chintai.com/search/unit.html?district=1',
#         'https://www.miyazaki-chintai.com/search/miyazaki/unit.html?district=1&start=10',
#         'https://www.miyazaki-chintai.com/search/details_a3803.html'
#     )
# ])
# def test_to_links(site, current_url, expected_following_url, expected_indexing_url, mocker):
#     rules = ConfigDatabase(site).settings['spider_rules']
#     spider_converter = SpiderConverter(site, rules)
#     response = mocker.Mock()
#     response.url = current_url
#     response.text = open(os.path.dirname(__file__) + '/testdata/' + site + '.html', 'r').read()
#     following_urls = [link.url for link in spider_converter.to_links(response.url, response.text) if link.follow == True]
#     indexing_urls = [link.url for link in spider_converter.to_links(response.url, response.text) if link.index == True]
#     assert following_urls[0] == expected_following_url
#     assert indexing_urls[0] == expected_indexing_url
