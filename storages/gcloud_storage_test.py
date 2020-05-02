import pytest
from storages.gcloud_storage import GcloudStorage

# @pytest.mark.usefixtures('tasks_db')
class TestGcloudStorage():
    def test_store(self):
        GcloudStorage()
        # """Should raise an exception if summary missing."""
        # with pytest.raises(ValueError):
        #     tasks.add(Task(owner='bob'))

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
