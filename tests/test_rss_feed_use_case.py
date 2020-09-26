import unittest
from unittest.mock import Mock, patch
from o_que_le_agora import rss_use_case


class TestRSSFeedUseCase(unittest.TestCase):
    @patch('o_que_le_agora.rss_use_case.store')
    def test_save_rss_url(self, mock_store):
        rss_use_case.save_rss_url({
            'rss_identifier': 'some-feed-id',
            'rss_url': 'some-feed-url'
        })

        mock_store.save_rss_url.assert_called_with('some-feed-id', 'some-feed-url')

    def test_should_raise_error_if_there_is_missin_required_fields(self):
        result = rss_use_case.save_rss_url({
            'rss_identifier': 'some-feed-id'
        })

        self.assertEqual(result, 'Missing required fields')

    @patch('o_que_le_agora.rss_use_case.get_rss_feed_for')
    @patch('o_que_le_agora.rss_use_case.store')
    def test_get_post_from_feed(self, mock_store, mock_reader_get_rss_feed_for):
        mock_store.get_rss_url.return_value = 'http://feed-site'
        mock_reader_get_rss_feed_for.return_value = {
            'title': 'titulo',
            'entries': [
                {'title': 'primeiro post'}
            ]
        }
        posts = rss_use_case.get_posts_from_rss('nome-site')

        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['title'], 'primeiro post')

    @patch('o_que_le_agora.rss_use_case.store')
    def test_get_all_rss_identifier(self, mock_store):
        mock_store.get_all_rss_identifier.return_value = ['rss-1', 'rss-2']
        rss = rss_use_case.get_all_rss_identifier()

        self.assertEqual(2, len(rss))
        self.assertEqual('rss-1', rss[0])
        self.assertEqual('rss-2', rss[1])
