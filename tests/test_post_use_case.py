import unittest
from unittest.mock import Mock, patch
from o_que_le_agora.post_use_case import get_post_list


class TestPostUseCase(unittest.TestCase):
    @patch('o_que_le_agora.post_use_case.get_rss_feed_for')
    @patch('o_que_le_agora.post_use_case.store')
    def test_get_post_list(self, mock_store, mock_get_rss_feed_for):
        mock_store.get_feed_url.return_value = 'http://feed-site'
        mock_get_rss_feed_for.return_value = {
            'title': 'titulo',
            'entries': [
                {'title': 'primeiro post'}
            ]
        }
        posts = get_post_list('nome-site')

        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['title'], 'primeiro post')