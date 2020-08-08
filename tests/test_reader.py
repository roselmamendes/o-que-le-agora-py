import unittest
from unittest.mock import Mock
from feed.reader import get_rss_feed_for

# ['title', 'title_detail', 'links', 'link', 'id', 'guidislink', 'authors', 'author', 'author_detail', 'published', 'published_parsed', 'updated', 'updated_parsed', 'content', 'summary']
class TestReader(unittest.TestCase):
    def test_get_a_feed(self):
        feed_parser = Mock()
        feed_parser.parse.return_value = {'feed': {'title': 'titulo'}}
        
        rss_feed = get_rss_feed_for('http://site.com', feed_parser)

        feed_parser.parse.assert_called_with('http://site.com')
        self.assertEqual(rss_feed['feed']['title'], 'titulo')

    def test_get_an_entry(self):
        feed_parser = Mock()
        feed_parser.parse.return_value = {
        'entries':
            [ 
                {
                    'title': 'titulo',
                    'content': '<div>content</div>'
                }
            ]}

        rss_feed = get_rss_feed_for('http://site.com', feed_parser)

        feed_parser.parse.assert_called_with('http://site.com')
        self.assertEqual(rss_feed['entries'][0]['title'], 'titulo')
        self.assertEqual(rss_feed['entries'][0]['content'], '<div>content</div>')