import unittest
from store.store import save_rss_url, get_rss_url, clear_database

class TestStore(unittest.TestCase):
    def tearDown(self):
        clear_database()
    
    def test_save_rss_url(self):
        save_rss_url('rss-identifier', 'rss-url')

        rss_url = get_rss_url('rss-identifier')

        self.assertEqual(rss_url, 'rss-url')

    def test_return_empty_string_if_record_does_not_exist(self):
        rss_url = get_rss_url('rss-identifier')

        self.assertEqual(rss_url, '')