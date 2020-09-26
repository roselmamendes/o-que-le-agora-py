import unittest
from unittest.mock import Mock, patch
from o_que_le_agora.rss_feed_use_case import save_feed_url, get_posts_from_feed


class TestRSSFeedUseCase(unittest.TestCase):
    @patch('o_que_le_agora.rss_feed_use_case.store')
    def test_save_feed_url(self, mock_store):
        save_feed_url({
            'feed_identifier': 'some-feed-id',
            'feed_url': 'some-feed-url'
        })

        mock_store.save_feed_url.assert_called_with('some-feed-id', 'some-feed-url')

    def test_should_raise_error_if_there_is_missin_required_fields(self):
        result = save_feed_url({
            'feed_identifier': 'some-feed-id'
        })

        self.assertEqual(result, 'Missing required fields')

    @patch('o_que_le_agora.rss_feed_use_case.get_rss_feed_for')
    @patch('o_que_le_agora.rss_feed_use_case.store')
    def test_get_post_from_feed(self, mock_store, mock_get_rss_feed_for):
        mock_store.get_feed_url.return_value = 'http://feed-site'
        mock_get_rss_feed_for.return_value = {
            'title': 'titulo',
            'entries': [
                {'title': 'primeiro post'}
            ]
        }
        posts = get_posts_from_feed('nome-site')

        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['title'], 'primeiro post')
