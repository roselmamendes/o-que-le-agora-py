import unittest
from unittest.mock import patch
from o_que_le_agora.rss_feed_use_case import save_feed_url


class TestRSSFeedUseCase(unittest.TestCase):
    @patch('o_que_le_agora.rss_feed_use_case.store')
    def test_get_post_list(self, mock_store):
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