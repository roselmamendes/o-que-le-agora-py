import unittest
from unittest.mock import Mock
from feed.reader import get_rss_feed_for

class FeedObj:
    def __init__(self, title):
        self.title = title

class TestReader(unittest.TestCase):
    def test_get_a_feed(self):
        feed_parser = Mock()
        feed_parser.parse.return_value = FeedObj('titulo')
        
        rss_feed = get_rss_feed_for('http://site.com', feed_parser)

        feed_parser.parse.assert_called_with('http://site.com')
        self.assertEqual(rss_feed.title, 'titulo')