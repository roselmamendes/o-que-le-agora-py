import unittest
from store.store import save_feed_url, get_feed_url, clear_database

class TestStore(unittest.TestCase):
    def tearDown(self):
        clear_database()
    
    def test_save_feed_url(self):
        save_feed_url('feed-identifier', 'feed-url')

        feed_url = get_feed_url('feed-identifier')

        self.assertEqual(feed_url, 'feed-url')

    def test_return_empty_string_if_record_does_not_exist(self):
        feed_url = get_feed_url('feed-identifier')

        self.assertEqual(feed_url, '')