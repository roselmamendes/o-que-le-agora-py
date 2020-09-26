from store import store
from feed.reader import get_rss_feed_for

def save_feed_url(feed):
    if('feed_identifier' in feed.keys() and 'feed_url' in feed.keys()):
        store.save_feed_url(feed['feed_identifier'], feed['feed_url'])
    else:
        return 'Missing required fields'

def get_posts_from_feed(feed_identifier):
    posts = []
    url = store.get_feed_url(feed_identifier)
    if(url):
        rss_feed = get_rss_feed_for(url)
        posts = rss_feed['entries']
    return posts