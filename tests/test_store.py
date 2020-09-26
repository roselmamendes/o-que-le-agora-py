import unittest
from store.store import save_rss_url, get_rss_url, get_all_rss_identifier, clear_database

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

    def test_return_all_rss_identifier(self):
        save_rss_url('rss-identifier', 'rss-url')
        save_rss_url('rss-identifier1', 'rss-url1')
        save_rss_url('rss-identifier2', 'rss-url2')

        rss = get_all_rss_identifier()

        self.assertEqual(3, len(rss))
        self.assertEqual('rss-identifier', rss[0])
        self.assertEqual('rss-identifier1', rss[1])
        self.assertEqual('rss-identifier2', rss[2])

    def test_return_all_rss_identifier_empty(self):
        rss = get_all_rss_identifier()

        self.assertEqual(0, len(rss))